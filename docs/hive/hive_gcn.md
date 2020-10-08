# Graph Convolutional Network

The most promising use case is in Semi-supervised Learning where we are given a set of nodes, each with some observed numeric attributes x<sub>i</sub>.

Now, we `predict an output/label for each node` based on partial observations i.e. labels for some, but not all, of the nodes.

We might also be given a set of weighted edges, summarised by an adjacency matrix A. The main assumption is that when predicting the output yi for node i, the attributes and connectivity of nearby nodes provide useful side information or additional context.


## Summary of Results

-- Talk to JDO about this. Write it last, probably.

## Summary of Gunrock Implementation

The implementation has been hugely guided by

- http://proceedings.mlr.press/v97/wu19e.html
- https://arxiv.org/abs/1609.02907


### The GCN algorithm can be mapped into the following steps:

1. Initialization
-   Data Reading/Parsing
-   Parameter Initialization
-   [Random initialization of weight matrices](https://github.com/achalagarwal/gunrock/blob/d0202e3bbb88560bc97666675c0a94aa9e491c9c/gunrock/app/GuNNrock/gcn_problem.cuh#L225) W<sub>0</sub> and W<sub>1</sub>

[comment]: <> (Forward propagation and Backpropagation are explained for a single epoch, the same process is iterated for --num_iterations)

<sup><sub>__Forward Propagation__</sub></sup>

2. Edge Dropout
  - [With probability `p`, mask (disable) an edge value](https://github.com/achalagarwal/gunrock/blob/d0202e3bbb88560bc97666675c0a94aa9e491c9c/gunrock/app/GuNNrock/dropout/dropout.cuh#L53)
  - Results in new edge values
3. Edge Weight Sparse Multiplication
  - [Multiplication of edge values with trainable weights](https://github.com/achalagarwal/gunrock/blob/d0202e3bbb88560bc97666675c0a94aa9e491c9c/gunrock/app/GuNNrock/sparseMatMul/sparseMatMul_enactor.cuh#L89)
  - Summing the result from the multiplication to result in the XW<sub>0</sub> matrix
4. Graph Neighbor Sum 
  - [Summing the neighbour vectors for each vertex](https://github.com/achalagarwal/gunrock/blob/d0202e3bbb88560bc97666675c0a94aa9e491c9c/gunrock/app/GuNNrock/graphsum/graphsum_enactor.cuh#L99)
  - Results in the AXW<sub>0</sub> matrix
5. ReLU
  - on the AXW<sub>0</sub> matrix
6. Dropout
  - on the rectified AXW<sub>0</sub> matrix
7. Multiplication of W<sub>1</sub> weight matrix
  - results in AXW<sub>0</sub>W<sub>1</sub>
8. Repeat Graph Neighbor Sum 
  - [Summing the neighbour vectors for each vertex](https://github.com/achalagarwal/gunrock/blob/d0202e3bbb88560bc97666675c0a94aa9e491c9c/gunrock/app/GuNNrock/graphsum/graphsum_enactor.cuh#L99)
  - Results in the AAXW<sub>0</sub>W<sub>1</sub> matrix
9. Cross Entropy Loss
  - Compute training loss and likewise gradients of AAXW<sub>0</sub>W<sub>1</sub> matrix
  - Start Backprop
  
<sup><sub>__Backward Propagation__</sub></sup>

10. `backprop 8.` 
  - Results in the gradients of AXW<sub>0</sub>W<sub>1</sub> matrix
11. `backprop 7.` 
  - Compute the gradients of W<sub>1</sub> matrix and stores it to update the W<sub>1</sub> weight matrix later
  - Results in the gradients of AXW<sub>0</sub> matrix
12. `backprop 6.` 
  - Results in the updated gradients of AXW<sub>0</sub> matrix
13. `backprop 5.` 
  - Results in the updated gradients of AXW<sub>0</sub> matrix
14. `backprop 4.` 
  - Results in the updated gradients of XW<sub>0</sub> matrix
15. `backprop 3.`
  - Compute the gradients of W<sub>0</sub> matrix and stores it to update the W<sub>0</sub> weight matrix later
[16.]: <> (backprop 2 does not exist as that computation does not involve any trainable weight)
16. Update weight matrices W<sub>0</sub> and W<sub>1</sub>
  - Use the new weight matrices in the next epoch (iteration)

<sup><sub>__End of training__</sub></sup>

17. Export the trained weight matrices along with the loss/accuracy/runtime metrics

### The description of the lower level operators used to implement some of the steps described above:

The 17 steps above share computation patterns

1. To update an Array1D, the `ForEach` op has been used

```CUDA
 GUARD_CU (arr.ForEach (
          [params]__host__ __device__(ValueT &x) {
            x = update(x, params);
          }
      ))
```

2. To multiply dense matrix (X: nodes * features) with dense matrix (W<sub>0</sub>: features * dimension_0):

```CUDA
auto denseMM =
        [X, output, dimension_0, W0] __host__ __device__(
            const VertexT &src, VertexT &dest, const SizeT &edge_id,
            const VertexT &input_item, const SizeT &input_pos,
            SizeT &output_pos) -> bool {
      for (int i = 0; i < dimension_0; i++) {
        atomicAdd(output + src * dimension_0 + i, W0[edge_id] * X[dest * dimension_0 + i]);
      }
      return true;
    };
   
GUARD_CU(oprtr::Advance<oprtr::OprtrType_V2V> (
            graph.csr (), &local_vertices, null_ptr, oprtr_parameters,
            denseMM));
```

3. 

What was implemented with respect to the entire workflow?


## How To Run This Application on DARPA's DGX-1


### Prereqs/input

1. Build Gunrock -- https://github.com/gunrock/gunrock/pull/805
2. Make sure the following datafiles are available:
  - feature file (edge weights / node vectors)
  - split file (for each vertex, a value 0/1/2 to specify train/test/validation node
  - graph file (adjacency list format)
  
### Running the application

<!-- <code> -->
```bash
# build gunrock 

# cd to bin folder
cd ./build/bin

# run gcn binary
./gcn --feature_file <featurefile> --graph_file <graphfile> --split_file <splitfile>

# vary parameters like: Number of training iterations, silent run, etc. 
```
<!-- </code> -->

Note: This run / these runs are faster on DARPA's DGX-1.

### Output

1. Relevant data is printed per epoch:

- Training loss/acc
- Validation loss/acc
- Time taken

2. Output after training:

- test loss/acc
- time taken by various operators

#### To extract weights:

How do you make sure your output is correct/meaningful? (What are you comparing against?)

The operators have tests that are verified internally and the backpropagation has been verified using python scripts with the theoretical implementation

## Performance and Analysis

### runtime
### metrics

### Implementation limitations

e.g.:

- Size of dataset that fits into GPU memory (what is the specific limitation?)
- Restrictions on the type/nature of the dataset

### Comparison against existing implementations

- Reference implementation (python? Matlab?)
- OpenMP reference

Comparison is both performance and accuracy/quality.



### Performance limitations

e.g., random memory access?

## Next Steps

### Alternate approaches

If you had an infinite amount of time, is there another way (algorithm/approach) we should consider to implement this?

### Gunrock implications

What did we learn about Gunrock? What is hard to use, or slow? What potential Gunrock features would have been helpful in implementing this workflow?

### Notes on multi-GPU parallelization

What will be the challenges in parallelizing this to multiple GPUs on the same node?

Can the dataset be effectively divided across multiple GPUs, or must it be replicated?

### Notes on dynamic graphs

(Only if appropriate)

Does this workload have a dynamic-graph component? If so, what are the implications of that? How would your implementation change? What support would Gunrock need to add?

### Notes on larger datasets

What if the dataset was larger than can fit into GPU memory or the aggregate GPU memory of multiple GPUs on a node? What implications would that have on performance? What support would Gunrock need to add?

### Notes on other pieces of this workload

Briefly: What are the important other (non-graph) pieces of this workload? Any thoughts on how we might implement them / what existing approaches/libraries might implement them?
