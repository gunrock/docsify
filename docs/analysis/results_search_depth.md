# Search depth

How many iterations does it take to complete a primitive? These results are measured on an NVIDIA Tesla V100 GPU.

Table of data for the below results, including links to JSON summaries with command lines for each experiment: [
[Runtime vs. search depth]((analysis/gunrock_primitives_all_V100_search_depth_table.md)
]

Note this plot (rendered with [Altair](https://altair-viz.github.io/)) is interactive (you can click, drag, and zoom; and mousing over a data point shows the data associated with that point).

<div id="vis_gunrock_primitives_all_V100_search_depth"></div>
<script type="text/javascript">
  var spec_gunrock_primitives_all_V100_search_depth = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_all_V100_search_depth.json";
  vegaEmbed('#vis_gunrock_primitives_all_V100_search_depth', spec_gunrock_primitives_all_V100_search_depth).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>
