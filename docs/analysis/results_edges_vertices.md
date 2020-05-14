# Edges/vertices visited vs. number of edges/vertices

How many edges or vertices do we actually visit across our primitives as a function of the number of edges or vertices in the graph? These results are measured on an NVIDIA Tesla V100 GPU.

<div id="vis_gunrock_primitives_all_V100_edges_visited_vs_num_edges"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_all_V100_edges_visited_vs_num_edges.json";
  vegaEmbed('#vis_gunrock_primitives_all_V100_edges_visited_vs_num_edges', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_all_V100_edges_visited_vs_num_edges_table.md)

<div id="vis_gunrock_primitives_all_V100_vertices_visited_vs_num_vertices"></div>
<script type="text/javascript">
  var spec = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_all_V100_vertices_visited_vs_num_vertices.json";
  vegaEmbed('#vis_gunrock_primitives_all_V100_vertices_visited_vs_num_vertices', spec).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

[Table of data for the above results, including links to JSON summaries with command lines for each experiment](analysis/gunrock_primitives_all_V100_vertices_visited_vs_num_vertices_table.md)
