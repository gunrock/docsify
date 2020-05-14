# PageRank

We show four results for PageRank on a variety of datasets across multiple GPUs: throughput (measured in MTEPS), runtime (measured in ms), throughput as a function of load-balancing strategy ("advance mode"), and throughput as a function of the number of edges.

<div id="vis_gunrock_primitives_pr_mteps"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_pr_mteps.json";
  vegaEmbed('#vis_gunrock_primitives_pr_mteps', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_pr_mteps_table.md)

<div id="vis_gunrock_primitives_pr_avg_process_time"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_pr_avg_process_time.json";
  vegaEmbed('#vis_gunrock_primitives_pr_avg_process_time', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_pr_avg_process_time_table.md)

<div id="vis_gunrock_primitives_pr_advance_mode"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_pr_advance_mode.json";
  vegaEmbed('#vis_gunrock_primitives_pr_advance_mode', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_pr_advance_mode_table.md)

<div id="vis_gunrock_primitives_pr_edges"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_pr_edges.json";
  vegaEmbed('#vis_gunrock_primitives_pr_edges', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_pr_edges_table.md)
