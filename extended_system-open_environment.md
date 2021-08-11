# Open Environment

There is a meta-system to the basic system described in the main design document; we call this the "Open Environment" or **OE** system. The open environment is the system that surrounds the core note-taking application we have described elsewhere.

The main points of the OE system are to:

1. Integrate the work of writing paper-length and book-length projects into the same system used for note-taking.
   1. Specifically, all documents in the OE are indexed and searched as part of the general background note-taking activities; in essence, any document in the system is treated as a note. Obviously notes have special status, but this is implemented via a **standard** not in software (a **tool** or **implementation**). In software, all documents are the same in terms of the API. For instance, all documents are searchable, are indexed, are transformable by general text transforms (that do not require a given standard), etc.
   2. Functions exist for turning notes into outlines and then into drafts. If possible, tools should exist to turn draft documents into notes and outlines as well, but this problem is not necessarily invertible (in the functional decomposition sense).
   3. Allow drafts to act as notes and vice-versa.
2. Integration of other tools for thought. This is complex, but the basic ideas are like this:
   1. Over recent years a number of powerful programming language tools have been integrated into Markdown documents:
      1. [RMarkdown](https://rmarkdown.rstudio.com/) allows the making of notebooks with live R code and/or paper and book length documents with integrated data analysis code.
      2. [Jupyter Notebooks](https://jupyter.org/) originally for the Python language, but opened up to dozens of other languages over time. These notebooks allow the integration of notes (in Markdown) with code in many different languages (although only one language per notebook easily). These are live documents that can be modified and run by readers, but also they can be compiled and exported in locked formats like PDF or html.
      3. [BeakerX](http://beakerx.com/), originally a polyglot notebook system for mixing languages (to fix this limitation in Jupyter) but eventually abandoned as a separate project and turned into Jupyter extensions.
      4. [Pluto](https://github.com/fonsp/Pluto.jl) a fully "reactive" live coding environment for the Julia language. The systems above allow the code and underlying computational model to get out of sync; Pluto fixes this by using a reactive programming paradigm _a la_ the Javascript model.
   2. These tools allow for the following to be done:
      1. Integration of computer generated graphics with formatted explanatory text and the bundling of the corresponding data and code, so that these stay together.
      2. **Aside:** Note that the item above is integral to the open science movement!
      3. More or less full use of the computational tools listed above in the format of a notes or notebooks. For me, and I would imagine many other people, these tools are integral to the work we do/our thinking process.
3. 




---
2021.08.11 (Initial Working Draft)<br>Matthew Turner