# High Level Goals

As noted elsewhere this is an evolutionary project that will, for instance, likely use [Obsidian](https://obsidian.md/) as a supporting application until that can be replaced.

There are (too many) documents coving other topics here, but these are the highest level goals:

+ **Note Taking Software:** An integrated note-taking system that allows the writing of notes in a variety of note-taking strategies (see `design_notes.md` for more on this). With "wiki-style" links.
+ **Markdown By Default:** The starting point is markdown as the core document markup language, only leaving this as is absolutely necessary to make other features available; and, whenever possible, having features that _fail_ in a markdown-friendly way.
+ **Sensible Front Matter:** There needs to be a way to include relevant information to be encoded not as part of the main text.
+ **Document Creation and Editing Software:** Generic support (_via_ `pandoc`) for the writing of long-form documents (scientific papers, novels, etc.)
+ **Outlining Tools:** An "opposite end of the spectrum" tool from atomic or evergreen notes.
+ **Full, Fast, Sensible Search:** Fully integrated search across an entire constellation of documents that are part of the collection. (This should be near-real-time but possibly extended with routine re-indexing/maintenance.) Search should be intelligent with respect to different document types, not indexing meta-data that is not relevant to the document's meaning.
+ **Code Blocks:** The ability to embed code blocks in the Markdown that can be differentially processed from the surrounding text (_a la_ some of `obsidian`'s features). Possibly extended with something akin to [Hugo](https://gohugo.io/) "shortcodes."
+ **Relevant Exclusions:** The ability to exclude some document types from some types of processing. For instance, the main use case here is the full inclusion of live documents and computing notebooks, like `jupyter`, `pluto`, or RMarkdown (`Rmd`), in the collection without letting these break the flow of the note-taking and document processing tools, but still allowing these live documents to be stored appropriately and linked with other sorts of documents.



---
2021.10.02 (Initial Working Draft)<br>Matthew Turner
