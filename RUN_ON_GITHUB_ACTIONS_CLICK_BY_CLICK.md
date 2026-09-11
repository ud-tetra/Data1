# Run UD P4-ER1 Free on GitHub Actions — Click by Click

**Package:** `UD_P4_ER1_GITHUB_ACTIONS_REPO_v0.2.zip`  
**Required locally:** only a web browser and a free GitHub account  
**Docker on your Windows PC:** not required  
**Physical promotion:** `0`

## Part A — Create the GitHub repository

1. Download `UD_P4_ER1_GITHUB_ACTIONS_REPO_v0.1.zip`.
2. In Windows Explorer, right-click the ZIP and choose **Extract All**.
3. Open GitHub in your browser and sign in.
4. Click the **+** button at the upper-right and choose **New repository**.
5. Repository name: use something simple, for example:

   `ud-p4-er1-runner`

6. Choose **Public** if you are comfortable making this operational test harness public. Standard GitHub-hosted Actions runners are free for public repositories.
7. Do **not** add a README, `.gitignore`, or license on the creation screen; this package already contains a README.
8. Click **Create repository**.

## Part B — Upload the package

1. On the new empty repository page, click **uploading an existing file**.

   If the repo is not empty, use **Add file → Upload files**.

2. In Windows Explorer, open the extracted package directory.
3. Select **all contents inside the directory**, including:

   - `.github`
   - `p4`
   - `controller`
   - `config`
   - `scripts`
   - `governance`
   - `docs`
   - `README.md`

4. Drag the selected **files and folders** onto GitHub's upload page.

   Important: upload the *contents* of the package, not the outer package folder. At repository root GitHub must show a `.github` folder.

5. Wait until GitHub finishes listing the uploaded files.
6. In **Commit changes**, use:

   `Add frozen UD P4-ER1 external runner`

7. Commit directly to the default branch.
8. Click **Commit changes**.

## Part C — Confirm the workflow exists

1. Return to the repository **Code** tab.
2. Open:

   `.github/workflows/p4-er1-bmv2.yml`

3. If that file is visible, the workflow is installed correctly.

## Part D — Run it

1. Click the **Actions** tab.
2. If GitHub asks whether to enable Actions for the repository, enable them.
3. In the left sidebar click:

   **UD P4-ER1 External BMv2 Receipt Run**

4. Click **Run workflow**.
5. Leave the default branch selected.
6. Click the green **Run workflow** button.
7. A workflow run should appear within several seconds.
8. Click that run to watch progress.

The first run pulls public P4 compiler / BMv2 / P4Runtime images and may take several minutes.

## Part E — What success looks like

The job should finish green.

Open the job log. Near the end you should see:

`P4_ER1_EXTERNAL_CORPUS_PASS`

then:

`receipt_count=18`

and later:

`EXTERNAL_CORPUS_VERIFICATION_PASS`

followed by:

`P4_ER1_GITHUB_ACTIONS_PASS`

## Part F — Download the evidence

1. Return to the workflow run summary page.
2. Scroll to **Artifacts**.
3. Click:

   `UD_P4_ER1_EXTERNAL_RECEIPT_BUNDLE`

4. GitHub downloads a ZIP.
5. Upload that ZIP back into the UD ChatGPT project.

Do not edit the files before returning them.

The most important files inside are:

- `results/P4_ER1_EXTERNAL_SOURCE_ONLY_RECEIPTS.jsonl`
- `results/P4_ER1_EXTERNAL_CORPUS_MANIFEST.json`
- `results/VERIFY_EXTERNAL_CORPUS.txt`
- `results/RUNTIME_IMAGES.txt`
- `results/GITHUB_RUNNER_PROVENANCE.txt`
- `logs/simple_switch_grpc.log`
- `build/p4er1.p4info.txt`
- `build/p4er1.json`

## If the run fails

Download the artifact anyway if GitHub provides one. The workflow uses `if: always()` for artifact upload, so partial diagnostics should survive many failure modes.

If there is no artifact, send a screenshot of the red workflow step and its last 30–50 log lines.

## Why this run is scientifically useful

The source plan is frozen before the cloud run and contains no hidden Theta endpoint.

The cloud runner independently executes:

`P4Runtime PacketOut → BMv2 simple_switch_grpc → PacketIn`

The collector then requires:

- exactly 18 switch-returned receipts;
- event sequence exactly `1..18`;
- exact switch echo of the frozen source metadata;
- no unexplained sequence gaps;
- a valid append-only SHA-256 record chain.

A PASS therefore closes the *external operational receipt acquisition* gate for this test carrier.

It does **not** prove that network packets are Theta objects or physical UD carriers.

**Physical promotion remains 0.**


## v0.2 repair after the first external run

The first external run reached the P4Runtime configuration stage and exposed a build-path defect. p4c produced the BMv2 JSON inside an output directory, but v0.1 passed that directory to the controller instead of the JSON file.

v0.2 fixes only that executable path.

If your repository already contains v0.1, the easiest update is:

1. extract `UD_P4_ER1_GITHUB_ACTIONS_PATCH_v0.2.zip`;
2. in GitHub choose **Add file → Upload files**;
3. drag the patch contents into the repository root;
4. commit with message:
   `Repair P4-ER1 BMv2 device config path v0.2`
5. return to **Actions** and run **UD P4-ER1 External BMv2 Receipt Run** again.

The source plan and receipt law are unchanged.
