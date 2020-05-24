# Edges/vertices visited vs. number of edges/vertices

How many edges or vertices do we actually visit across our primitives as a function of the number of edges or vertices in the graph? These results are measured on an NVIDIA Tesla V100 GPU.

Tables of data for the below results, including links to JSON summaries with command lines for each experiment: [
[Edges visited vs. number of edges](analysis/gunrock_primitives_all_V100_edges_visited_vs_num_edges_table.md) |
[Vertices visited vs. number of vertices]((analysis/gunrock_primitives_all_V100_vertices_visited_vs_num_vertices_table.md))
]

Note these plots (rendered with [Altair](https://altair-viz.github.io/)) are interactive (you can click, drag, and zoom; and mousing over a data point shows the data associated with that point).

<script type="text/javascript">
  var spec_gunrock_primitives_all_V100_edges_visited_vs_num_edges = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_all_V100_edges_visited_vs_num_edges.json";
  vegaEmbed('#vis_gunrock_primitives_all_V100_edges_visited_vs_num_edges', spec_gunrock_primitives_all_V100_edges_visited_vs_num_edges).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_primitives_all_V100_vertices_visited_vs_num_vertices = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_primitives_all_V100_vertices_visited_vs_num_vertices.json";
  vegaEmbed('#vis_gunrock_primitives_all_V100_vertices_visited_vs_num_vertices', spec_gunrock_primitives_all_V100_vertices_visited_vs_num_vertices).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);
</script>

<div id="vis_gunrock_primitives_all_V100_edges_visited_vs_num_edges"></div>
<div id="vis_gunrock_primitives_all_V100_vertices_visited_vs_num_vertices"></div>
