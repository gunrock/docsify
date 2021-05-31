#!/usr/bin/env python3

# run from gunrock-docs/docs/hive_phase2
# ./hive_phase2.py && open report/hive_phase2darpa.pdf

import os
import tempfile
import subprocess
import re

files = sorted(
    [
        f
        for f in os.listdir("./")
        if (
            (
                f.startswith("hive_")
                and f.endswith(".md")
                and f != "hive_datasets.md"
                and f != "hive_template_phase2.md"
                and f != "hive_phase2_summary.md"
                and f != "hive_forall_phase2.md"
            )
        )
    ]
)

# I put this back since it doesn't get included in the PDF otherwise
# files.append("hive_scaling.html.md")

print(
    """---
title: HIVE Phase 2 Report&colon; Executive Summary

toc_footers:
  - <a href='https://github.com/gunrock/gunrock'>Gunrock&colon; GPU Graph Analytics</a>
  - Gunrock &copy; 2021 The Regents of the University of California.

search: true

full_length: true
---

# HIVE Phase 2 Report&colon; Executive Summary

This report is located online at the following URL: <https://gunrock.github.io/docs/hive_phase2/hive_phase2_summary.html>.

Herein UC Davis produces the following deliverables that it promised to deliver in Phase 2:

_list_

Specific notes on applications and scaling follow:

""",
    file=open("hive_phase2_summary.md", "w"),
)

with open("hive_phase2_summary.md", "a") as dest:
    for f in files:
        fname = f[:-3]
        print(f)
        with open(f) as file:
            contents = file.read()
            title = re.search("# (.*)\n", contents).group(1)
            summary = re.search("\n## Summary of Results\n\n([^#]*)\n\n#", contents)
            if summary == None:
                summary = re.search("\n## Summary of Results\n\n([^#]*)", contents)
            summary = summary.group(1)
            dest.write(
                f"## {title} \n**[{title}](https://gunrock.github.io/docs/{fname})** \n{summary}\n\n"
            )

pandoc_cmd = [
    "pandoc",
    "--template=report/hive_phase2_template.tex",
    "--variable",
    "title=A Commodity Performance Baseline for HIVE Graph Applications:\\\\Phase 2 Report",
    "--variable",
    "subtitle=31 May 2021",
    "--variable",
    "author=Ben Johnson \\and Muhammad Osama \\and John D. Owens \\and Serban Porumbescu",
    "--variable",
    "postauthor=UC Davis",
    "--variable",
    "documentclass=memoir",
    "--variable",
    "fontsize=10pt",
    "--variable",
    "classoption=oneside",
    # '--variable', 'classoption=article',
    "--variable",
    "toc-depth=0",
    "--toc",
    "-o",
    "report/hive_phase2.pdf",
    # '-o', 'darpa.tex',
]

# make a couple of temporary files
spacer_tempfile = tempfile.NamedTemporaryFile(mode="w+", suffix=".md")
spacer_tempfile.write("\n")
table_tempfile = tempfile.NamedTemporaryFile(mode="w+", suffix=".md")
table_tempfile.write("\n\n# Tables of Performance Results\n\n")

# list of input files
mdfiles = ["hive_phase2_summary.md", "hive_forall_phase2.md"]
for file in files:
    mdfiles.append(file)
    # format is hive_X_phase2.md
    app = re.search("hive_(.*)_phase2.md", file)
    if app:  # if there's a writeup
        plotfile = f"plots/{app.group(1)}_plots.md"
        if os.path.isfile(plotfile):
            mdfiles.append(plotfile)
mdfiles.extend([table_tempfile.name])  # section heading for tables
# now add (table file, spacer), repeat
flatten = lambda t: [item for sublist in t for item in sublist]
mdfiles.extend(
    flatten(
        map(
            lambda x: ["tables/" + x, spacer_tempfile.name],
            sorted(os.listdir("tables")),
        )
    )
)


pandoc_cmd.extend(mdfiles)

print(pandoc_cmd)

subprocess.run(pandoc_cmd)

spacer_tempfile.close()
table_tempfile.close()
