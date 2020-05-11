# Publish Documentation Checklist
To make changes to **gunrock/docs**, follow the steps below. Docsify documentation (this repository) is different from doxygen, and can be updated as needed. Whereas, doxygen changes are usually only pushed online on release. Feel free to add, remove content as you desire to this repository and push it online when ready.

!> [docsify/docsify](https://docsify.js.org/#/quickstart) does a great job at documenting on how to write and publish docs, please read those for more detail. This write up will focus on Gunrock specific docs.

#### Install docsify-cli
```bash
npm i docsify-cli -g
```

#### Clone and enter gunrock/docs repository
```bash
git clone git@github.com:gunrock/docs.git
cd docs
```

#### Start an interactive docsify server
```bash
docsify serve docs
```
!> Note it is `serve` **not** `server`. And `docs` here is not the root of the repository, but the subfolder called `docs` within `gunrock/docs` repo.

An interactive session will be available at http://localhost:3000.

#### Already cloned? Pull latest changes
```bash
git pull
```

#### Directory structure
Find where you may want to add your new documentation, the following directory structure will help you decide and familiarize you with the site files and their purpose.
```python
.
│
... # [EVERYTHING ELSE] Irrelevant.
├── docs # [Docs] Gunrock documentation directory.
│   ├── _coverpage.md # Cover page settings.
│   ├── _images # [IMAGES] Dump images here that you would like to upload and include in docs.
│   ├── _media # [MEDIA] PDFs, attachments, text files?
│   │   ├── attachments
│   │   ├── favicon.ico
│   │   ├── logo.png
│   │   └── logo_full.png
│   ├── _navbar.md # [TOP NAVBAR] Modify navbar.
│   ├── _sidebar.md # [SIDEBAR] Manually add links to side bar.
│   ├── analysis  # [PERF] Results and analysis related pages.
│   │   └── ...
│   ├── devs  # [DEV] Developer's guide and related docs.
│   │   ├── README.md # Acts as an index.html (default page) for devs directory.
│   │   └── ...
│   ├── gunrock # [CORE] Core gunrock docs, quick start, programming model, etc.
│   │   └── ....
│   ├── hive # [HIVE] All things hive (DARPA).
│   ├── index.html # [INDEX] Main index.html page, includes lots of site settings and used for adding plugins, scripts, vega, mathjax includes, etc.
│   ├── notes # [NOTES] Any unsorted notes.
│   └── projects # [PROJECTS] Ongoing or future ideas.
...

51 directories, 319 files
```

!> Feel free to add your own subdirectory under `docs` and include it in the `_sidebar.md`. You are not limited by the directories already in the repo, organize to your liking!

#### Actually writing docs
Simply write in markdown (`.md`) and add to the directories above, include it in the `_sidebar.md` if you want. :tada:

#### How do I edit the home page?
In the `index.html`, we have linked the "home page" or the first content you see to the `README.md` file in the main repository. This way, we only have to manage one `README.md` file:
```html
...
// Fetch README.md from gunrock/gunrock repository
homepage: 'https://raw.githubusercontent.com/gunrock/gunrock/master/README.md',
...
```

#### How do I view my changes from the test build?
If you have `docsify serve` running, you can view all your changes **live** on localhost:3000 in any browser. Any minor change in the files is instantly updated on the browser!


#### Everything looks good, how do I push everything online?

1. add and commit all the new or changed files:
```bash
git add /path/to/modified/files
git commit -m "your commit message, make it useful!"
git push origin develop
```
2. Your changes are now in `develop` branch of the repo, to make them live on the internet, create a pull request from develop to master branch: [master..develop](https://github.com/gunrock/docs/compare/master...gunrock:develop)

#### Screwed up? Would like to revert?
Just revert your git changes/commits in the `master` and `dev` branch.

#### Add files but don't want them live on the website?
Anything outside `docs` directory is not online on the website but will be in the github `gunrock/docs` repository if pushed. I recommend pushing these files to an `offline` folder (create one if it doesn't exists).

#### Add vega graphs to the website
vega graphs are simply published as `<div id=""><script> (vega json dump) </script></div>` in the markdown files.