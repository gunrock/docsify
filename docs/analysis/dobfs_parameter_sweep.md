# Parameter Sweep for Direction-Optimized Breadth-First Search

Gunrock's direction-optimized BFS is parameterized by two values we call `do_a` and `do_b`. These control when our BFS switches between push and pull. We describe these in more detail in our [2017 TOPC paper](https://escholarship.org/uc/item/9gj6r1dj), section 5.1.4.

Gunrock's performance substantially depends on our settings of `do_a` and `do_b`. In general this is also true for other direction-optimized implementations. To help us understand this behavior, we ran experiments over a full set of `do_a` and `do_b` parameters for the datasets below.

Tables of data for the below datasets, including links to JSON summaries with command lines for each experiment: [ [hollywood-2009](analysis/gunrock_dobfs_heatmaps_hollywood-2009_do_ab_table.md) |
[indochina-2004](analysis/gunrock_dobfs_heatmaps_indochina-2004_do_ab_table.md) |
[rmat_n24_e16](analysis/gunrock_dobfs_heatmaps_rmat_n24_e16.000000_do_ab_table.md) |
[road_usa](analysis/gunrock_dobfs_heatmaps_road_usa_do_ab_table.md) |
[soc-LiveJournal1](analysis/gunrock_dobfs_heatmaps_soc-LiveJournal1_do_ab_table.md) |
[soc-orkut](analysis/gunrock_dobfs_heatmaps_soc-orkut_do_ab_table.md)
]

Note these plots (rendered with [Altair](https://altair-viz.github.io/)) are interactive (you can click, drag, and zoom; select items in the legend; and mousing over a data point shows the data associated with that point).

<script type="text/javascript">
  var spec_gunrock_dobfs_heatmaps_hollywood_2009_do_ab = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_dobfs_heatmaps_hollywood-2009_do_ab.json";
  vegaEmbed('#vis_gunrock_dobfs_heatmaps_hollywood_2009_do_ab', spec_gunrock_dobfs_heatmaps_hollywood_2009_do_ab).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_dobfs_heatmaps_indochina_2004_do_ab = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_dobfs_heatmaps_indochina-2004_do_ab.json";
  vegaEmbed('#vis_gunrock_dobfs_heatmaps_indochina_2004_do_ab', spec_gunrock_dobfs_heatmaps_indochina_2004_do_ab).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_dobfs_heatmaps_rmat_n24_e16_000000_do_ab = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_dobfs_heatmaps_rmat_n24_e16.000000_do_ab.json";
  vegaEmbed('#vis_gunrock_dobfs_heatmaps_rmat_n24_e16_000000_do_ab', spec_gunrock_dobfs_heatmaps_rmat_n24_e16_000000_do_ab).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_dobfs_heatmaps_road_usa_do_ab = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_dobfs_heatmaps_road_usa_do_ab.json";
  vegaEmbed('#vis_gunrock_dobfs_heatmaps_road_usa_do_ab', spec_gunrock_dobfs_heatmaps_road_usa_do_ab).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_dobfs_heatmaps_soc_LiveJournal1_do_ab = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_dobfs_heatmaps_soc-LiveJournal1_do_ab.json";
  vegaEmbed('#vis_gunrock_dobfs_heatmaps_soc_LiveJournal1_do_ab', spec_gunrock_dobfs_heatmaps_soc_LiveJournal1_do_ab).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_dobfs_heatmaps_soc_orkut_do_ab = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_dobfs_heatmaps_soc-orkut_do_ab.json";
  vegaEmbed('#vis_gunrock_dobfs_heatmaps_soc_orkut_do_ab', spec_gunrock_dobfs_heatmaps_soc_orkut_do_ab).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

</script>

<div id="vis_gunrock_dobfs_heatmaps_hollywood_2009_do_ab"></div>
<div id="vis_gunrock_dobfs_heatmaps_indochina_2004_do_ab"></div>
<div id="vis_gunrock_dobfs_heatmaps_rmat_n24_e16_000000_do_ab"></div>
<div id="vis_gunrock_dobfs_heatmaps_road_usa_do_ab"></div>
<div id="vis_gunrock_dobfs_heatmaps_soc_LiveJournal1_do_ab"></div>
<div id="vis_gunrock_dobfs_heatmaps_soc_orkut_do_ab"></div>
