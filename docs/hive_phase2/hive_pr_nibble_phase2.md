# Local Graph Clustering (LGC)

The [Phase 1 writeup]((../hive/hive_pr_nibble.md)) contains a detailed description of the application.

From the Phase 1 writeup:

>>From [Andersen et al.](https://projecteuclid.org/euclid.im/1243430567):

>> A local graph partitioning algorithm finds a cut near a specified starting vertex, with a running time that depends largely on the size of the small side of the cut, rather than the size of the input graph.

>A common algorithm for local graph clustering is called PageRank-Nibble (PRNibble), which solves the L1 regularized PageRank problem. We implement a coordinate descent variant of this algorithm found in [Fountoulakis et al.](https://arxiv.org/pdf/1602.01886.pdf), which uses the fast iterative shrinkage-thresholding algorithm (FISTA).

## Scalability Summary

Bottlenecked by network bandwidth between GPUs

## Summary of Results

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## Summary of Gunrock Implementation

The Phase 1 single-GPU implementation is [here](../hive/hive_pr_nibble).

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
```
git clone  https://github.com/gunrock/gunrock -b multigpu
mkdir build
cd build/
cmake ..
make -j16 pr_nibble
```
**Verify git SHA:** `commit 3e7d4f29f0222e9fd1f4e768269b704d6ebcd02c`

### Partitioning the input dataset

Partitioning is handled automatically as Local Graph Clustering relies on Gunrock's multi-GPU `ForALL` operator and its frontier vertices are split evenly across all available GPUs. Please refer to the chapter on [Gunrock's `ForAll` Operator](#gunrocks-forall-operator) for additional information.

### Running the application (default configurations)

From the `build` directory

```
cd ../examples/pr_nibble/
./hive-mgpu-run.sh
```

This will launch jobs that sweep across 1 to 16 GPU configurations per dataset and application option as specified in `hive-pr_nibble-test.sh`.  See [Running the Applications](#running-the-applications) for additional information.


#### Datasets
**Default Locations:**

```
/home/u00u7u37rw7AjJoA4e357/data/gunrock/gunrock_dataset/mario-2TB/large
```

**Names:**

```
hollywood-2009
europe_osm
```

### Running the application (alternate configurations)

#### hive-mgpu-run.sh


Modify `OUTPUT_DIR` to store generated output and json files in an alternate location.

#### hive-geo-test.sh

Modify `APP_OPTIONS` to specify alternate `--src` and `--max-iter` values.  Please see the Phase 1 single-GPU implementation details [here](https://gunrock.github.io/docs/#/hive/hive_pr_nibble) for additional parameter information.

Please review the provided script and see "Running the Applications" chapter for details on running with additional datasets.

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

Why is scaling not ideal?

What limits our scalability?
