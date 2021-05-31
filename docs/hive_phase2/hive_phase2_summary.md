# HIVE Phase 2 Report&colon; Executive Summary

This report is also located online at the following URL: <https://gunrock.github.io/docs/#/hive_phase2/hive_phase2_summary>. Links currently work better in the PDF version than the HTML version.

Herein UC Davis produces the following deliverables that it promised to deliver in Phase 2:

- Implementation of DARPA HIVE v0 apps as single-node, multi-GPU applications using the [Gunrock](https://gunrock.github.io/) framework
- Performance characterization of these applications across multiple GPUs
- Analysis of the limits of scalability for these applications

In our writeup, we first [describe how to reproduce our results](#running-the-applications) and then [describe the scalability behavior of our ForAll operator](#gunrocks-forall-operator).

We begin with a table that summarizes the scalability behavior for each application, then a longer description of each application:

| Application | Scalability behavior |
| ----------- | -------------------- |
| Application Classification | Bottlenecked by network bandwidth between GPUs |
| GraphSAGE | Bottlenecked by network bandwidth between GPUs |
## [App: Scan Statistics](#scan-statistics) ([HTML](hive_phase2/hive_SS_phase2))

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## [App: Application Classification](#application-classification) ([HTML](hive_phase2/hive_ac_phase2))

We re-forumlate the `application_classification` workload to improve memory locality and admit a natural multi-GPU implementation.  We then parallelized the core computational region of `application_classification` across GPUs.  For the kernels in that region that do not require communication between GPUs, we attain near-perfect scaling.  Runtime of the entire application remains bottlenecked by network bandwidth between GPUs.  However, mitigating this bottleneck should be possible further optimization of the memory layout.

## [App: Geolocation](#geolocation) ([HTML](hive_phase2/hive_geolocation_phase2))

We rely on a Gunrock's multi-GPU `ForALL` operator to implement Geolocation as the entire behavior can be described within a single-loop like structure. The core computation focuses on calculating a spatial median, and for multi-GPU `ForAll`, that work is split such that each GPU gets an equal number of vertices to process. We see a minor speed-up on a DGX-A100 going from 1 to 3 GPUs on a twitter dataset, but in general, due to the communication over the GPU-GPU interconnects for all the neighbors of each vertex, there's a general pattern of slowdown going from 1 GPU to multiple GPUs, and no scaling is observed.

## [App: GraphSAGE](#graphsage) ([HTML](hive_phase2/hive_graphSage_phase2))

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## [App: Community Detection (Louvain)](#community-detection-louvain) ([HTML](hive_phase2/hive_louvain_phase2))

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## [App: Local Graph Clustering (LGC)](#local-graph-clustering-lgc) ([HTML](hive_phase2/hive_pr_nibble_phase2))

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## [App: Graph Projections](#graph-projections) ([HTML](hive_phase2/hive_proj_phase2))

We implemented a multi-GPU version of sparse-sparse matrix multiplication, based on chunking the rows of the left hand matrix.  This yields a communication-free implementation with good scaling properties.  However, our current implementation remains partially limited by load imbalance across GPUs.

## [App: GraphSearch](#graphsearch) ([HTML](hive_phase2/hive_rw_phase2))

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

## [App: Seeded Graph Matching (SGM)](#seeded-graph-matching-sgm) ([HTML](hive_phase2/hive_sgm_phase2))

Multi-GPU SGM experiences considerable speed-ups over single GPU implementation with a near linear scaling if the dataset being processed is large enough to fill up the GPU. We notice that ~$1$ million nonzeros sparse-matrix is a decent enough size for us to show decent scaling as we increase the number of GPUs. The misalignment for this implementation is also synthetically generated (just like it was for Phase 1, the bottleneck is still the `|V|x|V|` allocation size).

## [App: Sparse Fused Lasso](#sparse-fused-lasso) ([HTML](hive_phase2/hive_sparse_graph_trend_filtering_phase2))

Sparse Fused Lasso (or Sparse Graph Trend Filtering) relies on a Maxflow algorithm. As highlighted in the Phase 1 report, a sequential implementation of Maxflow outperforms a single-GPU implementation, and the actual significant core operation of SFL is a serial normalization step that cannot be parallelized to single-GPU let a lone be scaled to multiple GPUs. Therefore, we refer readers to phase 1 report for this workload.


## [App: Vertex Nomination](#vertex-nomination) ([HTML](hive_phase2/hive_vn_phase2))

One or two sentences that summarize "if you had one or two sentences to sum up your whole effort, what would you say". I will copy this directly to the high-level executive summary in the first page of the report. Talk to JDO about this. Write it last, probably.

---

We also produce web versions of our [scalability plots](hive_phase2/plots/) and [scalability tables of results](hive_phase2/tables/).
