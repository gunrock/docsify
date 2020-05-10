# Publish Documentation Checklist
To make changes to **gunrock/docs**, follow the steps below. An important note here that slate documentation (this repository) is different from doxygen, and can be updated as needed. Whereas, doxygen changes are usually only pushed online on release. Feel free to add, remove content as you desire to this repository and push it online when ready.

#### Install system dependencies
```bash
sudo apt-get install zlib1g-dev build-essential ruby-full
```

- zlib1g-dev for nokogiri
- build-essential to compile some gems
- ruby-full for ruby-dev

#### Install bundler
If it yells at you about a specific bundler version, just install that (type `bundler:1.15.4` instead of `bundler`).
```bash
sudo gem install bundler
```

#### Clone and enter gunrock/docs repository
```bash
git clone git@github.com:gunrock/docs.git
cd docs
```

#### Use bundler to install gems we need
In the docs directory.
> It's possible to run the following without sudo (i think):
```bash
sudo bundle install
```

#### Already cloned? Pull latest changes
```bash
git pull
```

#### Directory structure
Find where you may want to add your new documentation, the following directory structure will help you decide and familiarize you with the site files and their purpose.
```python
.
├── CHANGELOG.md
├── CHECKLIST.md
├── CODE_OF_CONDUCT.md
├── Gemfile
├── Gemfile.lock
├── LICENSE
├── README.md
├── SLATEREADME.md
├── config.rb
├── deploy.sh # [DEPLOY] main deploy script to build, test and publish the website
├── font-selection.json
├── lib
│   ├── multilang.rb
│   ├── nesting_unique_head.rb
│   ├── toc_data.rb
│   └── unique_head.rb
└── source
    ├── apps
    │   └── # notes on various gunrock applications
    ├── attachments
    │   └── # dump attachments here
    ├── fonts
    ├── hive
    │   └── # hive project related documents
    │
    ├── images
    │   └── # images hosted on the website (logo, etc.)
    │
    ├── includes
    │   ├── # [INCLUDES] Markdown files (extension: .md) to be included in main pages using -includes: in the page header (see more info below)
    │   ├── README.md # auto fetched from <gunrock/gunrock>/README.md on build
    │   ├── ...
    │   └── writing_googletests.md
    │
    ├── javascripts
    │   └── # javascripts: search functionality, code-syntax highlight, terms of cond
    │
    ├── layouts
    │   └── layout.erb  # [LAYOUT] heart of the website, layout of the actual website is defined here and is populated using the markdown files
    │
    ├── pdf
    │   └── # dump PDFs here
    │
    ├── stylesheets
    │   ├── # [STYLE] customizing website's style using css
    │   ├── _icon-font.scss
    │   ├── _normalize.scss
    │   ├── _rtl.scss
    │   ├── _variables.scss # adjust minor settings using css variables
    │   ├── print.css.scss
    │   └── screen.css.scss # main style sheet
    │
    ├── tables
    │   └── # [GRAPHS] dump performance tables from vega/altair here.
    │
    │
    ├── file.html.md # [PAGE] files with extenstion *.html.md will be turned into html pages on the main website path, for example: `developers.html.md` -> `https://gunrock.github.io/docs/developers.html`
    │
    │
    ├── directory/file.html.md # [SUBDIR/PAGE] will be turned into a webpage inside the respective subdirectory, for example: `hive/hive_geolocation.html.md` -> `https://gunrock.github.io/docs/hive/hive_geolocation.html`
    │
    │
    └── index.html.md # [HOMEPAGE] gunrock's home page at gunrock.github.io/docs

```

#### Configure your page using slate page header
Every page (with extension `.html.md`) pushed to the website will have some flavor of the following header at the very top, this header lets you configure few things for your doc:
```markdown
---
# title of the page
title: <Gunrock-Page-Title>

# full length page (just text) or two sections (text + code section)?
full_length: true 

# add a language tab, doesn't work with full_length set to true
# must be one of https://git.io/vQNgJ
language_tabs:
  - shell
  - ruby
  - python
  - javascript

# page footer
toc_footers:
  - <a href='https://github.com/gunrock/gunrock'>Gunrock; GPU Graph Analytics</a>
  - Gunrock &copy; 2018 The Regents of the University of California.

# Files listed here should be added to <root>/source/includes
# Do not need to include `.md` extenstion for the files here, just the names
includes:
  - <filetoinclude>
  - <filetoinclude>

# include search bar in the left menu? Makes the page searchable.
search: true
---
```

#### Add your webpage
Now that you have created a webpage with `.html.md` file format, and added the header. Where do you actually place it? There's two options:

1. https://gunrock.github.io/docs/page.html, your page needs to be in `source` directory (not in its subdirectories) for it to appear in the link: `docs/page.html`.
2. https://gunrock.github.io/docs/directory/page.html, your page needs to be in `source/directory` for it to appear in the link: `docs/directory/page.html`.

As mentioned in the header file, you can also dump your markdown `.md` files inside `source/includes` directory an just include them in the header of any of the `.html.md` pages. They will be appended to the top of the page in the order listed in the header, for example `index.html.md`:
```markdown
...

includes:
  - README
  - overview
  - programming_model
  - gunrock_applications
  - building_gunrock
  - methodology
  - results
  - publications_and_presentations
  - road_map
  - potential_projects
  - developers
  - frequently_asked_questions
  - release_notes
  - acknowledgements

...
```
This header will append `README` then `overview`, then `programming_model`, etc. 

#### Deploy options (--help)
```bash
<root>/deploy --help
```
##### Output
```bash
neoblizz@Ares:~/docs (master)*$ ./deploy.sh --help
Usage: deploy.sh [-c FILE] [<options>]
Deploy generated files to a git branch.

Options:

  -h, --help               Show this help information.
  -v, --verbose            Increase verbosity. Useful for debugging.
  -e, --allow-empty        Allow deployment of an empty directory.
  -m, --message MESSAGE    Specify the message used when committing on the
                           deploy branch.
  -n, --no-hash            Don't append the source commit's hash to the deploy
                           commit's message.
      --source-only        Only build but not push
      --push-only          Only push but not build
```

#### I have added all of my pages, how do I *test* the build?
```bash
<root>/deploy --source-only
```
##### Output will be some variation of the following:
```bash
    ...
     updated  build/interesting_research.html
     updated  build/mgpu_partition.html
     updated  build/mgpu_scalability.html
     updated  build/mgpu_speedup.html
     updated  build/sandbox.html
   identical  build/tables/engines_topc_table.html
   identical  build/tables/frontier_size_table.html
   identical  build/tables/groute_table.html
   identical  build/tables/gunrock_gpus_table.html
   identical  build/tables/mgpu_partition_table.html
   identical  build/tables/mgpu_scalability_BFS_table.html
   identical  build/tables/mgpu_scalability_DOBFS_table.html
   identical  build/tables/mgpu_scalability_PageRank_table.html
   identical  build/tables/mgpu_speedup_all_table.html
   identical  build/tables/mgpu_speedup_geomean_table.html
Project built successfully.
```

#### How do I view my changes from the test build?
Under `<root>/build` you will find all of the HTML files and the entire webpage build as if it will appear online once the changes are pushed. Just open `index.html` on Google Chrome (or your favorite browser) and start navigating through to look at your changes. 


#### Everything looks good, how do I push everything online?

1. add and commit all the new or changed files:
```bash
git add /path/to/modified/files
git commit -m "your commit message, make it useful!"
git push origin master
```
2. run `deploy` again with no parameters (if you already committed your changes before the test build, and everything was ok in the test build you can just skip step 1. and issue deploy with `--push-only`, which will push the current build in the `build` directory online.)
```
./deploy.sh
```

Script will automatically checkin your html files to `gh-pages` branch, which is linked to the domain name `gunrock.github.io`.

#### Screwed up? Would like to revert?
Just revert your git changes in the `master` branch and `deploy` again!

#### Add files but don't want them live on the website?
Anything outside `source` directory is not online on the website but will be in the github `gunrock/docs` repository if pushed. I recommend pushing these files to the `offline` folder.
BUT, also, if you really wanted to put something in `source` or its subdirectories, and didn't want it live. Just make sure it does not have the extenstion `.html.md` and if it is a `.md` file it is not in `source/includes` and included anywhere in the page headers.

#### Add vega graphs to the website
vega graphs are simply published as `<div id=""><script> (vega json dump) </script></div>` in the markdown files.