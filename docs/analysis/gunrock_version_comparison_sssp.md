# Comparing Gunrock Versions on Single-Source Shortest Path

These results are primarily for internal use. We normalize the performance of every Gunrock version against Gunrock 1.0+ so that we can identify performance regressions. These results are shown in two ways: first, fastest Gunrock run on this primitive/dataset combination; second, with options separated out into different rows. We present these comparisons on two different GPUs (Tesla K40/K80 and Tesla V100).

Tables of data for the below results, including links to JSON summaries with command lines for each experiment: [
  [SSSP fastest results, combining all options, Tesla V100](analysis/gunrock_version_compare_sssp_Tesla_V100_all_table.md) |
  [SSSP fastest results, separating all options, Tesla V100](analysis/gunrock_version_compare_sssp_Tesla_V100_undirected_markpred_table.md) |
  [SSSP fastest results, combining all options, Tesla K40/80](analysis/gunrock_version_compare_sssp_Tesla_K40_80_all_table.md) |
  [SSSP fastest results, separating all options, Tesla K40/80](analysis/gunrock_version_compare_sssp_Tesla_K40_80_undirected_markpred_table.md)
]

Note these plots (rendered with [Altair](https://altair-viz.github.io/)) are interactive (you can click, drag, and zoom; select items in the legend; and mousing over a data point shows the data associated with that point).

<script type="text/javascript">
  var svgopt = { renderer: "svg" }
  var spec_gunrock_version_compare_sssp_Tesla_V100_all = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_version_compare_sssp_Tesla_V100_all.json";
  vegaEmbed('#vis_gunrock_version_compare_sssp_Tesla_V100_all', spec_gunrock_version_compare_sssp_Tesla_V100_all, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_version_compare_sssp_Tesla_V100_undirected_markpred = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_version_compare_sssp_Tesla_V100_undirected_markpred.json";
  vegaEmbed('#vis_gunrock_version_compare_sssp_Tesla_V100_undirected_markpred', spec_gunrock_version_compare_sssp_Tesla_V100_undirected_markpred, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_version_compare_sssp_Tesla_K40_80_all = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_version_compare_sssp_Tesla_K40_80_all.json";
  vegaEmbed('#vis_gunrock_version_compare_sssp_Tesla_K40_80_all', spec_gunrock_version_compare_sssp_Tesla_K40_80_all, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

  var spec_gunrock_version_compare_sssp_Tesla_K40_80_undirected_markpred = "https://raw.githubusercontent.com/gunrock/io/master/plots/gunrock_version_compare_sssp_Tesla_K40_80_undirected_markpred.json";
  vegaEmbed('#vis_gunrock_version_compare_sssp_Tesla_K40_80_undirected_markpred', spec_gunrock_version_compare_sssp_Tesla_K40_80_undirected_markpred, opt=svgopt).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
  }).catch(console.error);

</script>

## SSSP fastest results, combining all options, Tesla V100
<div id="vis_gunrock_version_compare_sssp_Tesla_V100_all"></div>

## SSSP fastest results, separating all options, Tesla V100
<div id="vis_gunrock_version_compare_sssp_Tesla_V100_undirected_markpred"></div>

## SSSP fastest results, combining all options, Tesla K40/80
<div id="vis_gunrock_version_compare_sssp_Tesla_K40_80_all"></div>

## SSSP fastest results, separating all options, Tesla K40/80
<div id="vis_gunrock_version_compare_sssp_Tesla_K40_80_undirected_markpred"></div>
