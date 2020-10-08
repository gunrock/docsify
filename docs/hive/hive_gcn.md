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


The GCN algorithm can be mapped into the following steps:

1. Initialization
-   Data Reading/Parsing
-   Parameter Initialization
-   [Random weight initialisation](https://github.com/achalagarwal/gunrock/blob/d0202e3bbb88560bc97666675c0a94aa9e491c9c/gunrock/app/GuNNrock/gcn_problem.cuh#L225) W<sub>1</sub> and W<sub>2</sub>

<sup><sub>__Forward Propagation__</sub></sup>

2. Edge Dropout
  - [With probability `p`, mask (disable) an edge value](https://github.com/achalagarwal/gunrock/blob/d0202e3bbb88560bc97666675c0a94aa9e491c9c/gunrock/app/GuNNrock/dropout/dropout.cuh#L53)
3. Edge Weight Sparse Multiplication
  - Multiplication of edge values with trainable weights
4. Graph Sum
5. ReLU
6. Dropout
7. Matrix Multiplication
8. Graph Sum
9. Cross Entropy Loss

<sup><sub>__Backward Propagation__</sub></sup>


The description of the lower level operators used to implement some of the steps described above:

1. 

2. 

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

<code>
// building gunrock 
// cd to build/bin folder

./gcn --feature_file <featurefile> --graph_file <graphfile> --split_file <splitfile>

// can decide a fixed number of training iterations 

</code>

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
