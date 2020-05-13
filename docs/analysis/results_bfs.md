# Breadth-First Search

We show four results for direction-optimized BFS on a variety of datasets across multiple GPUS: throughput (measured in MTEPS), runtime (measured in ms), throughput as a function of load-balancing strategy ("advance mode"), and throughput as a function of the number of edges. We may have application-specific notes on our [methodology page](/gunrock/methodology).

<div id="vis_gunrock_primitives_dobfs_mteps"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_mteps.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_mteps', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_mteps_table.html ':include :type=markdown')

<div id="vis_gunrock_primitives_dobfs_avg_process_time"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_avg_process_time.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_avg_process_time', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_avg_process_time_table.html ':include :type=markdown')

<div id="vis_gunrock_primitives_dobfs_advance_mode"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_advance_mode.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_advance_mode', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_advance_mode_table.html ':include :type=markdown')

<div id="vis_gunrock_primitives_dobfs_edges"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_edges.json";
  vegaEmbed('#vis_gunrock_primitives_dobfs_edges', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_dobfs_edges_table.html ':include :type=markdown')
