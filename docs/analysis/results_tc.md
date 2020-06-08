# Triangle Counting

We show two results for triangle counting (TC) on a variety of datasets across multiple GPUs: runtime (measured in ms) and runtime as a function of the number of edges. We may have application-specific notes on our [methodology page](/gunrock/methodology). The first plot and table answers the question "What is the fastest Gunrock run for a particular primitive-dataset-GPU combination?".

Tables of data for the below results, including links to JSON summaries with command lines for each experiment: [
  [TC runtime (ms) ](analysis/gunrock_primitives_tc_avg_process_time_table.md) |
  [TC runtime vs. edges](analysis/gunrock_primitives_tc_edges_table.md)
]

Note these plots (rendered with [Altair](https://altair-viz.github.io/)) are interactive (you can click, drag, and zoom; select items in the legend; and mousing over a data point shows the data associated with that point).

<script type="text/javascript">
  var svgopt = { renderer: "svg" }
  var spec_gunrock_primitives_tc_avg_process_time = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_tc_avg_process_time.json";
  vegaEmbed('#vis_gunrock_primitives_tc_avg_process_time', spec_gunrock_primitives_tc_avg_process_time, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_tc_edges = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_tc_edges.json";
  vegaEmbed('#vis_gunrock_primitives_tc_edges', spec_gunrock_primitives_tc_edges, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

## TC runtime (ms)
<div id="vis_gunrock_primitives_tc_avg_process_time"></div>

## TC runtime vs. edges
<div id="vis_gunrock_primitives_tc_edges"></div>
