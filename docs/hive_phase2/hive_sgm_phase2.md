# Seeded Graph Matching (SGM)

Phase 1 report can be found [here](https://gunrock.github.io/docs/#/hive/hive_sgm).

From [Fishkind et al.](https://arxiv.org/pdf/1209.0367.pdf):

> Given two graphs, the graph matching problem is to align the two vertex sets so as to minimize the number of adjacency disagreements between the two graphs. The seeded graph matching problem is the graph matching problem when we are first given a partial alignment that we are tasked with completing.

That is, given two graphs `A` and `B`, we seek to find the permutation matrix `P` that maximizes the number of adjacency agreements between `A` and `P * B * P.T`, where `*` represents matrix multiplication.  The algorithm Fishkind et al. propose first relaxes the hard 0-1 constraints on `P` to the set of doubly stochastic matrices (each row and column sums to 1), then uses the Frank-Wolfe algorithm to minimize the objective function  `sum((A - P * B * P.T) ** 2)`.  Finally, the relaxed solution is projected back onto the set of permutation matrices to yield a feasible solution.

## Summary of Results

Multi-GPU SGM experiences considerable speed-ups over single GPU implementation with a near linear scaling if the dataset being processed is large enough to fill up the GPU. We notice that ~$1$ million nonzeros sparse-matrix is a decent enough size for us to show decent scaling as we increase the number of GPUs. The misalignment for this implementation is also synthetically generated (just like it was for Phase 1, the bottleneck is still the `|V|x|V|` allocation size).

## Summary of Gunrock Implementation

The Phase 1 single-GPU implementation is [here](../hive/hive_sgm).

We parallelize across GPUs by scaling the per-iteration linear assignment problem. In our multi-GPU implementation we ignore the preprocessing step of sparse general matrix multiplication of given input matrices and the trace of matrix products at the very end. For the assignment problem, we use the auction algorithm (also described in the Phase 1 report), where each CUDA block gets a row of the cost matrix and does parallel reductions across the entries of the row using all available threads (with the help of NVIDIA’s CUB library). This allows us to map our rows to each block and explore parallelism within a single row of the matrix in a single-GPU, and split the number of rows across multiple GPUs. Our auction algorithm is implemented using a 2-step process (2-kernels with one fill operation to reset the maximum bids):

1. **Bidding:** Each bidder chooses an object  which brings him/her the best value (benefit-price).
2. **Assign:** Each object chooses a bidder which has the highest bid, and assigns itself to him/her as well as increases the object’s price.

Our experiments conclude that this “bidding” step was the bottleneck for our auction algorithm, and is the only kernel needed to be parallelized across multiple GPUs. For our assignment kernel, it was more effective to use one block to do the final assignment and use one volatile variable to compute the convergence metric.

### Differences in implementation from Phase 1

We now assign each row of the matrix to an entire block instead of a CUDA thread, and process the row in parallel instead of sequentially.

## How To Run This Application on DARPA's DGX-1

### Prereqs/input

(e.g., "build Gunrock's `dev-refactor` branch with hash X", "this particular dataset needs to be in this particular directory")

Include a github hash for the version you're using.

### Partitioning the input dataset

How did you do this? Command line if appropriate.

<code>
include a transcript
</code>

### Running the application

#### Datasets

Provide their names. We will probably make a separate page for them so you can just use their names.

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

No change from Phase 1.

### Performance limitations

Our multi-GPU implementation does not consider the SpGEMM preprocessing step. As SpGEMM is one of the core computations for many other algorithms, one future opportunity will be to scale a load-balanced SpGEMM to a multi-GPU system using merge-based decomposition. CUDA’s new virtual memory APIs also allow us to map and unmap physical memory chunks to a contiguous virtual memory array, which can be used to perform and store SpGEMM in its sparse-format without relying on an intermediate dense representation and a conversion to sparse output.

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

We observe great scaling for our bidding kernel as we increase the number of GPUs. If the input matrix is large enough, the rows can be easily split across multiple GPUs, and each GPU processes its equal share of rows, where within a GPU, each CUDA block processes one complete row.
