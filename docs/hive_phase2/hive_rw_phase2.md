# GraphSearch

The Phase 1 report for GraphSearch can be found [here](https://gunrock.github.io/docs/#/hive/hive_graphsearch).

> The graph search (GS) workflow is a walk-based method that searches a graph for nodes that score highly on some arbitrary indicator of interest.

>The use case given by the HIVE government partner was sampling a graph: given some seed nodes, and some model that can score a node as "interesting", find lots of "interesting" nodes as quickly as possible. Their algorithm attempts to solve this problem by implementing several different strategies for walking the graph.

## Scalability Summary

Bottlenecked by network bandwidth between GPUs

## Summary of Results

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## Summary of Gunrock Implementation

The Phase 1 single-GPU implementation is [here](https://gunrock.github.io/docs/#/hive/hive_graphsearch).

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
make -j16 rw
```
**Verify git SHA:** `commit d70a73c5167c5b59481d8ab07c98b376e77466cc`

### Partitioning the input dataset

How did you do this? Command line if appropriate.

<code>
include a transcript
</code>

### Running the application (default configurations)

From the `build` directory

```
cd ../examples/rw/
./hive-mgpu-run.sh
```

This will launch jobs that sweep across 1 to 16 GPU configurations per dataset and application option as specified across three different test scripts:

* `hive-rw-undirected-uniform.sh`
* `hive-rw-directed-uniform.sh`
* `hive-rw-directed-greedy.sh`

Please see [Running the Applications](#running-the-applications) for additional information.

#### Datasets
**Default Locations:**

```
/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB/graphsearch
```

**Names:**

```
dir_gs_twitter
gs_twitter.values
```
### Running the application (alternate configurations)

#### hive-mgpu-run.sh

Modify `OUTPUT_DIR` to store generated output and json files in an alternate location.

#### Additional hive-rw-*.sh scripts

This application relies on Gunrock's random walk `rw` primitive. Modify `WALK_MODE` to control the application's `--walk-mode` parameter and specify `--undirected` as `true` or `false`. Please see the Phase 1 single-GPU implementation details [here](https://gunrock.github.io/docs/#/hive/hive_graphsearch) for additional parameter information.


#### Single-GPU (for baseline)

<code>
include a transcript
</code>

#### Multi-GPU

<code>
include a transcript
</code>

### Output

No change from Phase 1.


## Performance and Analysis

No change from Phase 1.


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

**Single-GPU:** No change from Phase 1.

**Multiple-GPUs:** Performance bottleneck is the remote memory accesses from one GPU to another GPU's memory through NVLink. **SDP can we say anything else once we have the graphs?**

## Scalability behavior

**THIS IS REALLY THE ONLY IMPORTANT THING**

Why is scaling not ideal?

What limits our scalability?
