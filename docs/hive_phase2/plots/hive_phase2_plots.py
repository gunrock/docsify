#!/usr/bin/env python3.8

# run from gunrock-docs/docs/hive_phase2/plots

import altair as alt
import pandas as pd
import numpy
import datetime
import sys

sys.path.insert(1, "../../../../gunrock-io/scripts")

from fileops import save, getChartHTML
from filters import *
from logic import *

alt.data_transformers.disable_max_rows()

df = filesToDF(roots=["../results"], fnFilterInputFiles=[fileEndsWithJSON])
# df["num-gpus"] = df["jsonfile"].str.extract(r"GPU(\d+)")
# df["num-gpus"] = pd.to_numeric(df["num-gpus"])
df.rename({"walkmode": "variant"}, axis="columns", inplace=True)

# this next for loop unpacks the "tag" column into separate columns
for col in ["num-gpus", "variant"]:
    df[col] = [
        [tag.split(":")[1] for tag in l if tag.split(":")[0] == col] for l in df["tag"]
    ]
    df[col] = df[col].explode()  # list to scalar
for col in ["num-gpus"]:  # numeric cols only
    df[col] = pd.to_numeric(df[col])

df = df.sort_values(by=["primitive", "dataset", "variant", "num-gpus"]).reset_index(
    drop=True
)
dfs = {}
tables = {}

prims = df["primitive"].unique()
for prim in prims:
    dfs[prim] = df[df["primitive"] == prim]
    dfs[prim] = dfs[prim].dropna(axis=1, how="all")  # drop columns if all n/a

    cols = ["primitive", "dataset", "avg-process-time", "num-gpus"]
    has_variants = "variant" in dfs[prim].columns  # multiple variants
    if has_variants:
        cols.append("variant")
    tables[prim] = dfs[prim][cols]
    tables[prim].to_markdown(buf=f"../tables/{prim}.md", index=False)
    if has_variants:
        for variant in dfs[prim]["variant"].unique().tolist():
            name = prim + "_" + variant
            tables[name] = dfs[prim][dfs[prim]["variant"] == variant][cols]
            tables[name].to_markdown(buf=f"../tables/{name}.md", index=False)
