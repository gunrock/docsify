# Results and Analysis

We are gradually adding summaries of our results to these web pages (please let us know if you would like other comparisons). These summaries also include a table of results along with links to the configuration and results of each individual run. We detail our [methodology for our measurements here](/gunrock/methodology).

## Per-primitive Gunrock 1.0+ results

First, our most recent results (on Gunrock 1.0+) on several Gunrock primitives. <b>If you are comparing against Gunrock, these pages present the most recent results</b>, generally on a variety of input datasets and GPUs. Each page also has a link to a table of results which include, for each result, the Gunrock command line used to generate that result. If for any reason you are unable to replicate our results, please let us know.

- [Breadth-first search (BFS)](/analysis/results_bfs) and also [Forward-only breadth-first search (BFS)](/analysis/results_forward_bfs)
- [Single-source shortest path (SSSP)](/analysis/results_sssp)
- [Betweenness centrality (BC)](/analysis/results_bc)
- [PageRank (PR)](/analysis/results_pr)
- [Triangle counting (TC)](/analysis/results_tc)

## Cross-primitive Gunrock 1.0+ results

The following results compare across different primitives:
- [Edges/vertices visited vs. number of edges/vertices](/analysis/results_edges_vertices)
- [Search depth](/analysis/results_search_depth)

## Comparing performance across Gunrock versions

This data is primarily for internal use so that we can identify performance issues as we make improvements to Gunrock.

- [BFS](/analysis/gunrock_version_comparison_bfs)
- [SSSP](/analysis/gunrock_version_comparison_sssp)
- [BC](/analysis/gunrock_version_comparison_bc)
- [PageRank](/analysis/gunrock_version_comparison_pr)

## Single-GPU performance results from Gunrock 0.x (2016&ndash;2017)

The following are performance results largely from our [2016 ACM PPoPP paper](http://dx.doi.org/10.1145/2851141.2851145) and [2017 ACM TOPC paper](http://dx.doi.org/10.1145/3108140), or Gunrock versions current at that time.

- [Gunrock performance compared with other engines for graph analytics](/analysis/engines_topc)
- [Setting parameters for direction-optimized BFS](http://gunrock.github.io/gunrock/doc/latest/md_stats_do_ab_random)
- [Gunrock results on different GPUs](/analysis/gunrock_gpus)
- [Comparison to Groute](/analysis/groute)

## Multi-GPU performance results from Gunrock 0.x (2017)

The following are multi-GPU performance results largely from our [2017 IEEE IPDPS paper](http://dx.doi.org/10.1109/IPDPS.2017.117).

- [Multi-GPU Gunrock Speedups](/analysis/mgpu_speedup) and [Multi-GPU Gunrock Scalability](/analysis/mgpu_scalability)
- [Multi-GPU Gunrock Partition Performance](/analysis/mgpu_partition)

## Miscellaneous results from Gunrock 0.x (2016&ndash;2017)

The following are historical results (~2017) that are not published but we found interesting. We believe a current Gunrock build would have similar characteristics.

- [Gunrock BFS throughput as a function of frontier size](/analysis/frontier_size)

For reproducibility, we maintain Gunrock configurations and results in our github [gunrock/io](https://github.com/gunrock/io/tree/master/gunrock-output) repository.

We are happy to run experiments with other engines, particularly if those engines output results in our JSON format / a format that can be easily parsed into JSON format.
