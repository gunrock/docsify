# GraphSAGE

The [Phase 1 writeup]((../hive/hive_graphSage.md)) contains a detailed description of the application.

From the Phase 1 writeup:

> GraphSAGE is a way to fit graphs into a neural network: instead of getting the embedding of a vertex from all its neighbors' features as in conventional implementations, GraphSAGE selects some 1-hop neighbors, some 2-hop neighbors connected to those 1-hop neighbors, and computes the embedding based on the features of the 1-hop and 2-hop neighbors. The embedding can be considered as a vector containing hash values describing the interesting properties of a vertex.

## Scalability Summary

Bottlenecked by network bandwidth between GPUs

## Summary of Results

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## Summary of Gunrock Implementation

The Phase 1 single-GPU implementation is [here](../hive/hive_graphSage).

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
make -j16 sage
```
**Verify git SHA:** `commit d70a73c5167c5b59481d8ab07c98b376e77466cc`

### Partitioning the input dataset

Partitioning is handled automatically as GraphSage relies on Gunrock's multi-GPU `ForALL` operator and its frontier vertices are split evenly across all available GPUs. Please refer to the chapter on [Gunrock's `ForAll` Operator](#gunrocks-forall-operator) for additional information.

### Running the application (default configurations)

From the `build` directory

```
cd ../examples/sage/
./hive-mgpu-run.sh
```

This will launch jobs that sweep across 1 to 16 GPU configurations per dataset and application option as specified in `hive-sage-test.sh`.

  [Running the Applications](#running-the-applications) chapter for details on running with additional datasets

for additional parameter information, review the provided script, and see [Running the Applications](#running-the-applications) chapter for details on running with additional datasets.

#### Datasets
**Default Locations:**

```
/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB
/home/u00u7u37rw7AjJoA4e357/data/gunrock/gunrock_dataset/mario-2TB/large
```

**Names:**

```
pokec
dir_gs_twitter
europe_osm
```

### Running the application (alternate configurations)

#### hive-mgpu-run.sh

Modify `OUTPUT_DIR` to store generated output and json files in an alternate location.

#### hive-sage-test.sh

Modify `APP_OPTIONS` to specify alternate `--undirected` and `--batch-size` options.  Please see the Phase 1 single-GPU implementation details [here](https://gunrock.github.io/docs/#/hive/hive_graphSage) for additional parameter information, review the provided script, and see [Running the Applications](#running-the-applications) chapter for details on running with additional datasets.

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

Why is scaling not ideal?

What limits our scalability?
