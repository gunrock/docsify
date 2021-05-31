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

### ~~Partitioning the input dataset~~

How did you do this? Command line if appropriate.

<code>
include a transcript
</code>

### Running the application (default configurations)

From the `build` directory

```
cd ../examples/geo/
./hive-mgpu-run.sh  
```

This will launch jobs that sweep across 1 to 16 GPU configurations per dataset and application option as specified in `hive-geo-test.sh` (see below for [alternate configurations](#alt-configs)).
 
**Option:** to run on a different partition and/or less GPUs, specify parameters to the script above as follows: 
```
./hive-mgpu-run.sh  [num-gpus] [slurm-partion-name]
```


#### Datasets
**Default Locations:**

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

## <a name="alt-configs"></a> Running the application (alternate configurations)

To facilitate test sweeps across 1 to 16 GPUs, multiple application options, and datasets we make use of two bash scripts: `hive-mgpu-run.sh` and `hive-geo-test.sh`.

#### hive-mgpu-run.sh
This script configures SLURM with `NUM_GPUS` to sweep across on a chosen `PARTITION_NAME`. Running the script with no parameters is equivalent to: `./hive-mgpu-run.sh 16 dgx2` (i.e., 1 to 16 GPUs on the machine partition named "dgx2").

Modify `GEO_ITER` and `SPATIAL_ITER` to change the values of `--geo-iter` and `--spatial-iter`, respectively, passed to `hive-geo-test.sh`. Please see the Phase 1 single-GPU implementation details [here](https://gunrock.github.io/docs/#/hive/hive_geolocation) for additional parameter information.

Modify `OUTPUT_DIR` to store generated output and json files in an alternate location.


```
#!/bin/bash

NUM_GPUS=${1:-"16"}
PARTITION_NAME=${2:-"dgx2"}

APP_SCRIPT="./hive-geo-test.sh"
GEO_ITER[0]=10
GEO_ITER[1]=100

SPATIAL_ITER[0]=1000
SPATIAL_ITER[1]=10000

OUTPUT_DIR="geo_eval_mgpu/$PARTITION_NAME"
mkdir -p $OUTPUT_DIR

for gi in {0..1} #geo_iter
do
   for si in {0..1} #spatial_iter
   do
      for (( i=1; i<=$NUM_GPUS; i++))
      do
          # prepare and run SLURM command
          SLURM_CMD="srun --cpus-per-gpu 1 -G $i -p $PARTITION_NAME -N 1 "
          $SLURM_CMD $APP_SCRIPT $OUTPUT_DIR $i ${GEO_ITER[$gi]} ${SPATIAL_ITER[$si]} &
      done
   done
done
```

#### hive-geo-test.sh
This script is called repeatedly by `hive-mgpu-run.sh` to sweep across multiple numbers of GPU configurations and application parameters. That aside, this script can be run in isolation when it is undesirable to perform configuration sweeps. Running this script with no parameters is equivalent to the following command:

`./hive-geo-test.sh eval_mgpu 1 10 1000`

The command saves resulting output and json files to `OUTPUT_DIR` named `eval_mgpu`, runs on 1 `NUM_GPUS` with values of `--geo-iter` (`GEO_ITER)` and `--spatial-iter` (`SPATIAL_ITER`) set to 10 and 1000, respectively. **Please note** that when running this script outside of a SLURM environment, `NUM_GPUS` does not control the number of GPUs actually utilized because the application will always attempt to use all GPUs visible to the system. Alternatively, modify `for (( i=1; i<=$NUM_GPUS; i++))` in `hive-mgpu-run.sh` to limit device sweeps.

To use additional or **alternate datasets**, you need to modify or add elements to the `DATA_PREFIX` (path to directory containing desired dataset), `NAME`(name of dataset.mtx and dataset.labels), and `GRAPH` (aggregated options for the chosen graph and label files to pass to the application) arrays. **Please note** that you must update the for loop index if you add items to the arrays mentioned.


```
#!/bin/bash

APP_NAME="geo"
BIN_PREFIX="../../build/bin/"

DATA_PREFIX[0]="/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB/geolocation/twitter/graph"
DATA_PREFIX[1]="/home/u00u7u37rw7AjJoA4e357/data/gunrock/hive_datasets/mario-2TB/geolocation/instagram/graph"

NAME[0]="twitter"
NAME[1]="instagram"

GRAPH[0]="market ${DATA_PREFIX[0]}/${NAME[0]}.mtx --labels-file=${DATA_PREFIX[0]}/${NAME[0]}.labels"
GRAPH[1]="market ${DATA_PREFIX[1]}/${NAME[1]}.mtx --labels-file=${DATA_PREFIX[1]}/${NAME[1]}.labels"

OUTPUT_DIR=${1:-"eval_mgpu"}
NUM_GPUS=${2:-"1"}
JSON_FILE=""

GEO_ITER=${3:-"10"}
SPATIAL_ITER=${4:-"1000"}
APP_OPTIONS="--geo-iter=${GEO_ITER} --spatial-iter=${SPATIAL_ITER} --quick"

VARIANT="geo-${GEO_ITER}_spatial-${SPATIAL_ITER}"
TAG="variant:$VARIANT,num-gpus:$NUM_GPUS"

SUB_DIR=${VARIANT}
mkdir -p "$OUTPUT_DIR/$SUB_DIR"

for i in {0..1}
do
   # prepare output json file name with number of gpus for this run
   JSON_FILE="geo__${NAME[$i]}__GPU${NUM_GPUS}"	

   #echo \
   $BIN_PREFIX$APP_NAME \
   ${GRAPH[$i]} \
   $APP_OPTIONS \
   --tag=$TAG \
   --jsonfile="$OUTPUT_DIR/$SUB_DIR/$JSON_FILE.json" \
   > "$OUTPUT_DIR/$SUB_DIR/$JSON_FILE.output.txt"
done

```