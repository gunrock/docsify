# Gunrock's `ForAll` Operator
Gunrock's `ForAll` operator is a `compute` operator type, meaning, it takes in an input array and applies user-defined function on every element of the input in **parallel**. This input for the `ForAll` operator can in a sense be any elements of an array, vertices or edges of a frontier, or all the vertices or edges of the entire graph.
In HIVE's phase I, due to the intuitive nature and simple implementation of the the parallel `ForAll` operator, we found that the operator was very useful in implementing single-GPU versions of several of the HIVE application workloads such as Geolocation, Graph Search, Random Walk, GraphSAGE, computation elements of Local Graph Clustering, Louvain, and Graph Trend Filtering.

The following pseudocode shows a simple-sequential implementation of the `ForAll` operator:
```cpp
template <typename ArrayT, typename ApplyLambda>
void ForAll(ArrayT* array, ApplyLambda apply, std::size_t size) {
  for(std::size_t i = 0; i < size; ++i)
    apply(array, i);
}
```

## Gunrock Implementation
### Approach to Single-GPU
CUDA-based implementation of a parallel `ForAll` operator is a simple extension to the sequential version described above, where instead of looping over the array in a sequential loop, we launch `ceil_div(size, BLOCK_SIZE)` blocks, with $128$ or $256$ threads per block, and each element of the array gets processed by each thread of the parallel CUDA grid launch.
This effectively makes a simple loop-operator, a parallel operator with the ability to apply any aribitary user-defined operator on every element of the array. Given a single-GPU parallel `ForAll` operator, the users working on the graph algorithms can then write their custom user-defined operators to implement the apps. One example of an application implemented entirely using `ForAll` is Geolocation (described in detail [here](https://gunrock.github.io/docs/#/hive/hive_geolocation)). The following snipper is the CUDA-kernel call for Gunrock's `ForAll` operator.

```cpp
template <typename ArrayT, typename ApplyLambda>
__global__ void ForAll_Kernel(ArrayT array, ApplyLambda apply, std::size_t size) {
  const std::size_t STRIDE = blockDim.x * gridDim.x;
  auto thread_idx = blockDim.x * blockIdx.x + threadIdx.x;
  while (thread_idx < size) {
    apply(array, thread_idx);
    i += STRIDE;
  }
}
```

### Approach to Multi-GPU

## Scalability Analysis
### Expected Scaling
### Observed Scaling
### Performance limitations

## Special Cases
## Optimizations and Future-Work
