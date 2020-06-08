# Single-source Shortest Path

We show six results for single-source shortest path (SSSP) on a variety of datasets across multiple GPUs: throughput (measured in MTEPS), runtime (measured in ms), throughput as a function of load-balancing strategy ("advance mode"), and runtime as a function of the number of edges. We may have application-specific notes on our [methodology page](/gunrock/methodology). The first two plots and tables answer the question "What is the fastest Gunrock run for a particular primitive-dataset-GPU combination?".

Tables of data for the below results, including links to JSON summaries with command lines for each experiment: [
  [SSSP throughput (MTEPS), combining all options](analysis/gunrock_primitives_sssp_mteps_best_table.md) |
  [SSSP runtime (ms), combining all options](analysis/gunrock_primitives_sssp_avg_process_time_best_table.md) |
  [SSSP throughput (MTEPS), separating out options](analysis/gunrock_primitives_sssp_mteps_table.md) |
  [SSSP runtime (ms), separating out options](analysis/gunrock_primitives_sssp_avg_process_time_table.md) |
  [SSSP throughput (MTEPS) with advance mode](analysis/gunrock_primitives_sssp_advance_mode_table.md) |
  [SSSP runtime vs. edges](analysis/gunrock_primitives_sssp_edges_table.md)
]

Note these plots (rendered with [Altair](https://altair-viz.github.io/)) are interactive (you can click, drag, and zoom; select items in the legend; and mousing over a data point shows the data associated with that point).

<script type="text/javascript">
  var svgopt = { renderer: "svg" }
  var spec_gunrock_primitives_sssp_mteps_best = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_mteps_best.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_mteps_best', spec_gunrock_primitives_sssp_mteps_best, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_sssp_avg_process_time_best = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_avg_process_time_best.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_avg_process_time_best', spec_gunrock_primitives_sssp_avg_process_time_best, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_sssp_mteps = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_mteps.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_mteps', spec_gunrock_primitives_sssp_mteps, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_sssp_avg_process_time = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_avg_process_time.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_avg_process_time', spec_gunrock_primitives_sssp_avg_process_time, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_sssp_advance_mode = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_advance_mode.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_advance_mode', spec_gunrock_primitives_sssp_advance_mode, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_sssp_edges = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_sssp_edges.json";
  vegaEmbed('#vis_gunrock_primitives_sssp_edges', spec_gunrock_primitives_sssp_edges, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

## SSSP throughput (MTEPS), combining all options
<div id="vis_gunrock_primitives_sssp_mteps_best"></div>

## SSSP runtime (ms), combining all options
<div id="vis_gunrock_primitives_sssp_avg_process_time_best"></div>

## SSSP throughput (MTEPS), separating out options
<div id="vis_gunrock_primitives_sssp_mteps"></div>

## SSSP runtime (ms), separating out options
<div id="vis_gunrock_primitives_sssp_avg_process_time"></div>

## SSSP throughput (MTEPS) with advance mode
<div id="vis_gunrock_primitives_sssp_advance_mode"></div>

## SSSP runtime vs. edges
<div id="vis_gunrock_primitives_sssp_edges"></div>
