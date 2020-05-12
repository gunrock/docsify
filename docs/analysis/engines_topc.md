
# Comparison with Other Engines

We compared Gunrock against several other engines for graph analytics:

- [CuSha (GPU)](http://farkhor.github.io/CuSha/)
- [Galois (CPU)](http://iss.ices.utexas.edu/?p=projects/galois)
- Hardwired (primitive-specific) (GPU)
- [Ligra (CPU)](http://jshun.github.io/ligra/)
- [MapGraph (GPU)](https://www.blazegraph.com/mapgraph-technology/)
- [nvGRAPH (GPU)](https://developer.nvidia.com/nvgraph)

Below are comparative results on 5 primitives times 9 datasets in terms
of graph throughput (millions of edges per second, MTEPS) ...

<!-- I would like to do some form of this: -->
<!-- [mteps_graph](/mteps_graph.html ':include :type=iframe width=100% height=500px') -->

<!-- But it isn't working, so I have to use <iframe> -->
<iframe width="100%" height="500px" src="/analysis/engines_topc/mteps_graph.html"></iframe>

... and elapsed time (ms).

<!-- [elapsed_graph](elapsed_graph.html ':include :type=iframe width=100% height=500px') -->
<iframe width="100%" height="500px" src="/analysis/engines_topc/elapsed_graph.html"></iframe>

Here's a "Small Multiple Dot Plot" ([design by Joe Mako](https://policyviz.com/hmv_post/run-time-column-chart/)) that shows Gunrock speedup over different engines on different primitives and datasets:

<!-- [speedup_graph](speedup_graph.html ':include :type=iframe') -->
<iframe width="100%" height="900px" src="/analysis/engines_topc/speedup_graph.html"></iframe>

[Source data](/analysis/engines_topc/engines_topc_table.md), with links to the output JSON for each run
