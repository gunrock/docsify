# Geolocation

From Phase 1. report:
> Infers user locations using the location (latitude, longitude) of friends through spatial label propagation. Given a graph `G`, geolocation examines each vertex `v`'s neighbors and computes the spatial median of the neighbors' location list. The output is a list of predicted locations for all vertices with unknown locations.

## Summary of Results

We rely on a Gunrock's multi-GPU `ForALL` operator to implement Geolocation as the entire behavior can be described within a single-loop like structure. The core computation focuses on calculating a spatial median, and for multi-GPU `ForAll`, that work is split such that each GPU gets equal number of vertices to process. We see a minor speed-up on a DGX-A100 going from 1 to 3 GPUs on a twitter dataset, but in general, due to the communication over the GPU-GPU interconnects for all the neighbors of each vertex, there's a general pattern of slowdown going from 1 GPU to multiple GPUs, and no scaling is observed.

## Summary of Gunrock Implementation

The Phase 1 single-GPU implementation is [here](https://gunrock.github.io/docs/#/hive/hive_geolocation).

We parallelize across GPUs by using multi-GPU `ForAll` operator that splits the latitude and longitude arrays of Geolocation algorithm equally over multiple devices. For more detail on how `ForAll` was written to be multi-GPU can be found "Gunrock's `ForAll` Operator" section of the report. One optimization that we experimented with was using `BlockLoads` and shared memory (fast memory), to collectively load and process latitudes and longitudes in fast memory.

### Differences in implementation from Phase 1

No change from Phase 1.

## How To Run This Application on NVIDIA's DGX-2

### Prerequisites
```
git clone https://github.com/gunrock/gunrock -b mgpu-geo
mkdir build
cd build/
cmake ..
make -j16 geo
```
**Verify git SHA:** `commit b6e928b118f7ce792f82291cee5aa5d32547aaa3`

**Dataset locations:**

```
/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB/geolocation/twitter/graph
/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB/geolocation/instagram/graph
```

### ~~Partitioning the input dataset~~

How did you do this? Command line if appropriate.

<code>
include a transcript
</code>

### Running the application

From the `build` directory

```
cd ../examples/geo/
./hive-mgpu-run.sh  
```

This will launch jobs that sweep across 1 to 16 GPU configurations per dataset and option configuration as specified in `hive-geo-test.sh`.
 
**Option:** to run on a different partition and/or less GPUs, specify parameters to the script above as follows: 
```
./hive-mgpu-run.sh  [num-gpus] [slurm-partion-name]
```


#### Datasets
**Locations:**

```
/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB/geolocation/twitter/graph
/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB/geolocation/instagram/graph
```

**Names:**

```
twitter
instagram
```

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

### Implementation limitations

No change from Phase 1.

### Performance limitations

**Single-GPU:** No change from Phase 1.
**Multiple-GPUs:** Performance bottlneck is the remote memory accesses from one GPU to another GPU's memory through NVLink. What we observed was if we simply extend `ForAll` fromn single to multiple GPUs, the remote memory accesses to neighbor's latitude and longitude arrays cause NVLink's network bandwidth to be the bottleneck for the entire application.

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

Scaling is not ideal because we perform too many remote memory accesses causing the GPU to be constantly waiting to compute, therefore wasting the potential that GPU's throughput offers us. We require an efficient way to broadcast the latitudes and longitudes of a vertex to all other GPUs local memory in between each iteration, which can help mitigate this issue and may result in better scaling characteristics. One possible way to achieve this in the future works is by not using a `ForAll` and instead more specialized operators, designed with access patterns of these applications in mind.
