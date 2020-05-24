# Breadth-First Search

We show four results for direction-optimized BFS on a variety of datasets across multiple GPUs: throughput (measured in MTEPS), runtime (measured in ms), throughput as a function of load-balancing strategy ("advance mode"), and runtime as a function of the number of edges. We may have application-specific notes on our [methodology page](/gunrock/methodology).

Tables of data for the below results, including links to JSON summaries with command lines for each experiment: [
  [DOBFS throughput (MTEPS)](analysis/gunrock_primitives_dobfs_mteps_table.md) |
  [DOBFS runtime (ms) ](analysis/gunrock_primitives_dobfs_avg_process_time_table.md) |
  [DOBFS throughput with advance mode](analysis/gunrock_primitives_dobfs_advance_mode_table.md) |
  [DOBFS runtime vs. edges](analysis/gunrock_primitives_dobfs_edges_table.md)
]

Note these plots (rendered with [Altair](https://altair-viz.github.io/)) are interactive (you can click, drag, and zoom; and mousing over a data point shows the data associated with that point).

<script type="text/javascript">
  var spec_gunrock_primitives_dobfs_mteps = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_mteps.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_mteps', spec_gunrock_primitives_dobfs_mteps).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_dobfs_avg_process_time = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_avg_process_time.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_avg_process_time', spec_gunrock_primitives_dobfs_avg_process_time).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_dobfs_advance_mode = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_advance_mode.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_advance_mode', spec_gunrock_primitives_dobfs_advance_mode).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_dobfs_edges = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_edges.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_edges', spec_gunrock_primitives_dobfs_edges).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

<div id="vis_gunrock_primitives_dobfs_mteps"></div>
<div id="vis_gunrock_primitives_dobfs_avg_process_time"></div>
<div id="vis_gunrock_primitives_dobfs_advance_mode"></div>
<div id="vis_gunrock_primitives_dobfs_edges"></div>
