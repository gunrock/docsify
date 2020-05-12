
# Scalability on multiple GPUs

Scalability of DOBFS, BFS, and PR. {Strong, weak edge, weak vertex} scaling use rmat graphs with {2<sup>24</sup>, 2<sup>19</sup>, 2<sup>19</sup>&nbsp;&times;&nbsp;|GPUs|} vertices and edge factor {32, 256&nbsp;&times;&nbsp;|GPUs|, 256} respectively. DOBFS runs have idempotence disabled, though results with idempotence enabled have similar runtimes.

While providing both weak-vertex and -edge scaling, DOBFS doesn"t have good strong scaling, because its computation and communication are both roughly on the order of O(|V<sub>i</sub>|). This effect is more obvious on P100, as computation is faster but inter-GPU bandwidth stays mostly the same. BFS and PR achieve almost linear weak and strong scaling from 1 to 8 GPUs.

## DOBFS

<iframe width="100%" height="500px" src="analysis/mgpu/mgpu_scalability_DOBFS_graph.html"></iframe>

## BFS

<iframe width="100%" height="500px" src="analysis/mgpu/mgpu_scalability_BFS_graph.html"></iframe>

## PageRank

<iframe width="100%" height="500px" src="analysis/mgpu/mgpu_scalability_PageRank_graph.html"></iframe>


[[DOBFS source data](/analysis/mgpu/mgpu_scalability_DOBFS_table.md)] [[BFS source data](/analysis/mgpu/mgpu_scalability_BFS_table.md)] [[PageRank source data](/analysis/mgpu/mgpu_scalability_PageRank_table.md)], with links to the output JSON for each run<br/>
