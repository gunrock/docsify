# Single-source Shortest Path

We show four results for single-source shortest path on a variety of datasets across multiple GPUS: throughput (measured in MTEPS), runtime (measured in ms), throughput as a function of load-balancing strategy ("advance mode"), and throughput as a function of the number of edges. We may have application-specific notes on our [methodology page](/gunrock/methodology).

<div id="vis_gunrock_primitives_sssp_mteps"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_mteps.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_mteps', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_mteps_table.html ':include :type=markdown')

<div id="vis_gunrock_primitives_sssp_avg_process_time"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_avg_process_time.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_avg_process_time', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_avg_process_time_table.html ':include :type=markdown')

<div id="vis_gunrock_primitives_sssp_advance_mode"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_advance_mode.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_advance_mode', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_advance_mode_table.html ':include :type=markdown')

<div id="vis_gunrock_primitives_sssp_edges"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_edges.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_edges', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries for each experiment](https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_edges_table.html ':include :type=markdown')
