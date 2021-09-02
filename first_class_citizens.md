# First Class Citizens in the Open Environment

## The Ideal

What we would like to exist, _at some point_, is an open environment (OE) where any document of interest would open in a way that is natively usable while also being indexed, linked, etc., with every other document in the OE. So notes open Jupyter notebooks or Julia Pluto notebooks, and when clicking on local links in those notebooks you end up seeing notes in a native view for editing.

This ideal is unlikely to happen any time soon, so maybe keep dreaming.

## The Real

The most critical aspects of working with a heterogeneous collection of documents is that the indexing, searching, and linking all work. Additionally, viewing in context should be the first goal, followed later by editing/compiling/changing in context, but for the moment we can push that off.

## First-Class Citizens

The current list of (target) first-class citizen documents is:

+ Markdown files (`.md`)
+ Julia Pluto notebooks (`.jl`)
+ Jupyter notebooks (`ipynb`)
  + Worth noting: JupyterLab may be too complex to support, but keep tabs on it.
+ Rmarkdown documents (notebooks, `.Rmd`)
+ Some form of outlining tool, likely embedded in Markdown
  + Not Org-mode, at least not for me. If others want to implement Org-mode compatibility that is fine and it should be supported but I hate Org-mode!

Another view of this list is:

+ Note files (in Markdown)
+ Outline files (in Markdown?)
+ General documents (in Markdown)
+ "Live" documents (`Rmd`, `ipynb`, `jl`, etc.?)

Markdown is the main unifying feature of all of these file types.
