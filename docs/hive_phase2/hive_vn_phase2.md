# Vertex Nomination

!> JDO notes, delete these when you copy this to `hive_yourworkflowname`: The goal of this report is to be useful to DARPA and to your colleagues. This is not a research paper. Be very honest. If there are limitations, spell them out. If something is broken or works poorly, say so. Above all else, make sure that the instructions to replicate the results you report are good instructions, and the process to replicate are as simple as possible; we want anyone to be able to replicate these results in a straightforward way.

One-paragraph summary of application, written at a high level.

## Summary of Results

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## Summary of Gunrock Implementation

The Phase 1 single-GPU implementation is [here](../hive/hive_yourworkflowname).

We parallelize across GPUs by ...

The multi-GPU implementation differs from the single-GPU implementation in the following way:

- A
- B
- C


Take as long as you need, but this might be short. Don't provide info that is already in the Phase 1 report.

### Differences in implementation from Phase 1

(If any.)

## How To Run This Application on NVIDIA's DGX-2

### Prerequisites

The setup process assumes [Anaconda](https://www.anaconda.com/products/individual) is already installed.

```
git clone  git clone https://github.com/porumbes/mgpu_sssp -b main
cd mgpu_sssp
bash install.sh # downloads and compiles NVIDIA's nccl library
make
```
**Verify git SHA:** `commit 4f93307e7a0aa7f71e8ab024771e950e40247a4e`

### Partitioning the input dataset

Ben comment

### Running the application (default configurations)

```
./hive-mgpu-run.sh
```

This will launch jobs that sweep across 1 to 16 GPU configurations per dataset and application options as specified in `hive-vn-test.sh` **(see `hive_run_apps_phase2.md` for more info)**.


#### Datasets
**Default Locations:**

```
/home/u00u7u37rw7AjJoA4e357/data/gunrock/gunrock_dataset/mario-2TB/large
```

**Names:**

```
chesapeake
rmat18
rmat20
rmat22
rmat24
enron
hollywood-2009
indochina-2004
```

### Running the application (alternate configurations)

#### hive-mgpu-run.sh

Modify `NUM_SEEDS` to specify the number of seed locations to be used by `hive-vn-test.sh`.

Modify `OUTPUT_DIR` to store generated output and json files in an alternate location.

#### hive-vn-test.sh

Please see the Phase 1 single-GPU implementation details [here](https://gunrock.github.io/docs/#/hive/hive_vn) for additional parameter information, review the provided script, and see [Running the Applications](#running-the-applications) chapter for details on running with additional datasets.

#### Single-GPU (for baseline)

<code>
include a transcript
</code>

#### Multi-GPU

<code>
include a transcript
</code>

### Output

(Only include this if it's different than Phase 1. Otherwise: "No change from Phase 1.")

What is output when you run? Output file? JSON? Anything else? How do you extract relevant statistics from the output?

How do you make sure your output is correct/meaningful? (What are you comparing against?)

## Performance and Analysis

(Only include this if it's different than Phase 1. Otherwise: "No change from Phase 1.")

How do you measure performance? What are the relevant metrics? Runtime? Throughput? Some sort of accuracy/quality metric?

### Implementation limitations

(Only include this if it's different than Phase 1. Otherwise: "No change from Phase 1.")

e.g.:

- Size of dataset that fits into GPU memory (what is the specific limitation?)
- Restrictions on the type/nature of the dataset

### Comparison against existing implementations

(Delete this if there's nothing different from Phase 1.)

- Reference implementation (python? Matlab?)
- OpenMP reference

Comparison is both performance and accuracy/quality.

### Performance limitations

(Only include this if it's different than Phase 1. Otherwise: "No change from Phase 1.")

e.g., random memory access?

## Scalability behavior

**THIS IS REALLY THE ONLY IMPORTANT THING**

| GPUs | Runtime (ms) | Speedup over single-GPU version |
|------|--------------|---------------------------------|
| 1    |              |                                 |
| 2    |              |                                 |
| 3    |              |                                 |
| 4    |              |                                 |
| 5    |              |                                 |
| 6    |              |                                 |
| 7    |              |                                 |
| 8    |              |                                 |

Why is scaling not ideal?

What limits our scalability?
