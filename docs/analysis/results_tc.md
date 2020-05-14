# Triangle Counting

We show two results for triangle counting on a variety of datasets across multiple GPUs: runtime (measured in ms) and throughput as a function of the number of edges. We may have application-specific notes on our [methodology page](/gunrock/methodology).

<div id="vis_gunrock_primitives_tc_avg_process_time"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_tc_avg_process_time.json";
  vegaEmbed('#vis_gunrock_primitives_tc_avg_process_time', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_tc_avg_process_time_table.md)

<div id="vis_gunrock_primitives_tc_edges"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_tc_edges.json";
  vegaEmbed('#vis_gunrock_primitives_tc_edges', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_tc_edges_table.md)
