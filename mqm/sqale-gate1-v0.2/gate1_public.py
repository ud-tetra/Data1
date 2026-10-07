"""MQM × Sqale Gate 1 public runnable release v0.2.

Physical promotion: 0.
No hardware advantage claimed.

The comparison uses separate encodings on the same eight-site footprint.
"""
from itertools import product
from collections import defaultdict

CENTER=["IIIXXZZI","IIIYIYZZ","IIIXZIXZ","XXXXYYIX"]
GAUGE=CENTER+["XIIIIIII","ZIIIIIIZ","IXIIIIII","IZIIIIIZ","IIXIIIII","IIZIIIIZ"]
XL="IIIYZIZI"; ZL="IIIXIZIZ"
K4_VERTICES=(1,2,3,8)
K4_EDGES=((1,2),(1,3),(1,8),(2,3),(2,8),(3,8))
K4_PARITIES=("ZZIIIIII","ZIZIIIII","ZIIIIIIZ","IZZIIIII","IZIIIIIZ","IIZIIIIZ")
PM={"I":(0,0),"X":(1,0),"Z":(0,1),"Y":(1,1)}
PI={(0,0):"I",(1,0):"X",(0,1):"Z",(1,1):"Y"}

def pb(s):
    x=z=0
    for i,c in enumerate(s):
        a,b=PM[c]; x|=a<<i; z|=b<<i
    return x,z
def ps(p):
    x,z=p
    return "".join(PI[((x>>i)&1,(z>>i)&1)] for i in range(8))
def mul(a,b): return a[0]^b[0],a[1]^b[1]
def comm(a,b): return (((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())&1)
def wt(p): return (p[0]|p[1]).bit_count()
def syn(p): return "".join(str(comm(p,pb(g))) for g in CENTER)
def span(gs):
    S={(0,0)}
    for g in [pb(x) if isinstance(x,str) else x for x in gs]:
        S|={mul(s,g) for s in list(S)}
    return S

GG=span(GAUGE); CG=span(CENTER); lx=pb(XL); lz=pb(ZL); ly=mul(lx,lz)
LC=[GG,{mul(lx,g) for g in GG},{mul(lz,g) for g in GG},{mul(ly,g) for g in GG}]
def lclass(p):
    for i,C in enumerate(LC):
        if p in C:return i
    return -1
def rank(rows):
    a=[x|(z<<8) for x,z in rows];r=0
    for b in range(15,-1,-1):
        k=next((i for i in range(r,len(a)) if (a[i]>>b)&1),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        for i in range(len(a)):
            if i!=r and ((a[i]>>b)&1):a[i]^=a[r]
        r+=1
    return r

ALL=[pb("".join(t)) for t in product("IXYZ",repeat=8)]
single=[(0,0)]
for i in range(8):
    for c in "XYZ":
        s=["I"]*8;s[i]=c;single.append(pb("".join(s)))
by=defaultdict(list)
for e in single:by[syn(e)].append(e)
DEC={}
for sy,errs in by.items():
    good=[r for r in ALL if syn(r)==sy and all(lclass(mul(e,r))==0 for e in errs)]
    m=min(wt(r) for r in good)
    DEC[sy]=sorted(ps(r) for r in good if wt(r)==m)[0]

def erasure_group(site1):
    G=list(GAUGE)
    for c in "XZ":
        s=["I"]*8;s[site1-1]=c;G.append("".join(s))
    return span(G)
def eclass(p,site1):
    E=erasure_group(site1)
    for k,r in enumerate([(0,0),lx,lz,ly]):
        if p in {mul(r,g) for g in E}:return k
    return -1
def erasure_decoder(site1):
    cand=[((0,0),"I")]
    for j in range(1,9):
        if j==site1:continue
        for c in "XYZ":
            s=["I"]*8;s[j-1]=c;cand.append((pb("".join(s)),f"{c}{j}"))
    d={}
    for e,label in cand:d.setdefault(syn(e),label)
    for sy in {syn(e) for e,_ in cand}:
        items=[e for e,_ in cand if syn(e)==sy];ref=items[0]
        assert all(eclass(mul(ref,e),site1)==0 for e in items)
    return d

S832=["XXXXXXXX","ZZZZIIII","IIIIZZZZ","ZZIIZZII","ZIZIZIZI"]
LX832=["XXXXIIII","XXIIXXII","XIXIXIXI"]
LZ832=["ZIIIZIII","ZIZIIIII","ZZIIIIII"]
S833_CANON=["XYYXZIIZ","ZXIZXIZZ","XZZIIXZZ","YIYZIZXZ","YZXIZZIY"]

def parity_reconstruct(out,lost):
    p=1
    for i,x in enumerate(out):
        if i!=lost:p*=x
    y=list(out);y[lost]=p
    return y
def logical_x832(x):
    sups=((0,1,2,3),(0,1,4,5),(0,2,4,6));vals=[]
    for s in sups:
        p=1
        for i in s:p*=x[i]
        vals.append(p)
    return tuple(vals)

def exact_algebra():
    cr=rank([pb(g) for g in CENTER]); gr=rank([pb(g) for g in GAUGE])
    central=[p for p in ALL if all(comm(p,pb(g))==0 for g in CENTER)]
    d=min(wt(p) for p in central if p not in GG)
    single_bad=0
    for i in range(8):
        for c in "XYZ":
            s=["I"]*8;s[i]=c;e=pb("".join(s));r=pb(DEC[syn(e)])
            single_bad += lclass(mul(e,r))!=0
    fw_bad=0
    for vals in product("IXYZ",repeat=4):
        s=["I"]*8
        for i,c in zip((0,1,2,7),vals):s[i]=c
        e=pb("".join(s));r=pb(DEC[syn(e)])
        fw_bad += lclass(mul(e,r))!=0
    return {"center_rank":cr,"gauge_rank":gr,"dressed_distance":d,
            "single_pauli_failures":single_bad,"firewall_failures":fw_bad}

def microtest():
    sq_bad=0
    for lost in range(8):
        for flip in range(8):
            if flip==lost:continue
            out=[1]*8;out[lost]=None;out[flip]=-1
            sq_bad += logical_x832(parity_reconstruct(out,lost))!=(1,1,1)
    mqm_bad=mqm_hold=0
    for lost in range(1,9):
        d=erasure_decoder(lost)
        for flip in range(1,9):
            if flip==lost:continue
            s=["I"]*8;s[flip-1]="Z";e=pb("".join(s));label=d.get(syn(e))
            if label is None:mqm_hold+=1;continue
            if label=="I":r=(0,0)
            else:
                rr=["I"]*8;rr[int(label[1:])-1]=label[0];r=pb("".join(rr))
            mqm_bad += eclass(mul(e,r),lost)!=0
    return {"sqale_wrong_logical_x":sq_bad,"mqm_bad":mqm_bad,"mqm_hold":mqm_hold}

def census_176():
    n=bad=0
    for lost in range(1,9):
        d=erasure_decoder(lost);cases=[(0,0)]
        for j in range(1,9):
            if j==lost:continue
            for c in "XYZ":
                s=["I"]*8;s[j-1]=c;cases.append(pb("".join(s)))
        for e in cases:
            n+=1;label=d.get(syn(e))
            if label is None:bad+=1;continue
            if label=="I":r=(0,0)
            else:
                rr=["I"]*8;rr[int(label[1:])-1]=label[0];r=pb("".join(rr))
            bad += eclass(mul(e,r),lost)!=0
    return n,bad

def sqale_error(p):
    supports=((0,1,2,3),(0,1,4,5),(0,2,4,6));vals=[]
    for lost in range(8):
        surv=[i for i in range(8) if i!=lost];bad=0.0
        for bits in product((0,1),repeat=7):
            w=sum(bits);pr=p**w*(1-p)**(7-w);e=[0]*8
            for i,b in zip(surv,bits):e[i]=b
            e[lost]=w&1
            bad+=pr*any(sum(e[i] for i in s)&1 for s in supports)
        vals.append(bad)
    return sum(vals)/8

EC={};RD={}
for lost in range(1,9):
    E=erasure_group(lost);cm={}
    for k,r in enumerate([(0,0),lx,lz,ly]):
        for g in E:cm[mul(r,g)]=k
    EC[lost]=cm;rd={}
    for sy,label in erasure_decoder(lost).items():
        if label=="I":rd[sy]=(0,0)
        else:
            s=["I"]*8;s[int(label[1:])-1]=label[0];rd[sy]=pb("".join(s))
    RD[lost]=rd

def mqm_effective_receipt(p,q):
    sf=[(b,q**sum(b)*(1-q)**(4-sum(b))) for b in product((0,1),repeat=4)]
    K=B=H=0.0
    for lost in range(1,9):
        surv=[i for i in range(1,9) if i!=lost]
        for bits in product((0,1),repeat=7):
            w=sum(bits);pe=p**w*(1-p)**(7-w);s=["I"]*8
            for i,b in zip(surv,bits):
                if b:s[i-1]="Z"
            e=pb("".join(s));sy=syn(e)
            for f,pf in sf:
                obs="".join(str(int(x)^y) for x,y in zip(sy,f));pr=pe*pf/8
                if obs not in RD[lost]:H+=pr;continue
                K+=pr;B+=pr*(EC[lost].get(mul(e,RD[lost][obs]),-1)!=0)
    return K,B/K,H

def break_even():
    p=(0.002+0.023)/2;b=sqale_error(p);lo,hi=0,0.05
    for _ in range(45):
        m=(lo+hi)/2
        if mqm_effective_receipt(p,m)[1]<b:lo=m
        else:hi=m
    q=(lo+hi)/2
    return {"p_measure":p,"sqale_logical_x_error":b,
            "mqm_syndrome_bit_break_even":q,
            "mqm_at_break_even":mqm_effective_receipt(p,q)}

def run_all():
    print("MQM CENTER:",CENTER)
    print("MQM GAUGE:",GAUGE)
    print("MQM logical X/Z:",XL,ZL)
    print("K4:",K4_VERTICES,list(zip(K4_EDGES,K4_PARITIES)))
    print("decoder:",DEC)
    a=exact_algebra(); print("algebra:",a)
    m=microtest(); print("microtest:",m)
    c=census_176(); print("one-erasure + <=1 Pauli:",c)
    b=break_even(); print("exploratory break-even:",b)
    assert a=={"center_rank":4,"gauge_rank":10,"dressed_distance":3,
               "single_pauli_failures":0,"firewall_failures":0}
    assert m=={"sqale_wrong_logical_x":56,"mqm_bad":0,"mqm_hold":0}
    assert c==(176,0)
    return {"algebra":a,"microtest":m,"census":c,"break_even":b}

if __name__=="__main__":
    run_all()
