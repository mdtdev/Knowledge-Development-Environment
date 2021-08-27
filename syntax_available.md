# Syntax Available

If note taking strategies are to be implemented with standards, it is important to know what syntax is available for use in the standards.

In the note-taking community there is some confusion of terms, so this document is designed to give working definitions for this project.

## Annotated Terms List

Based on the prevalence of note-taking systems in this work, we start with the idea of the note. We observe that this is actually from a different level of analysis than much of the rest of this, but it is helpful.

+ Note
  + In note-taking systems the **note** is the basic unit of analysis
  + Most note-taking systems encourage notes to have certain properties:
    + Notes should be _atomic_. (Atomicity.) A note should be a short block of text expressing a single idea.
    + Notes should be revised and updated regularly or as needed. (Evergreen?)
    + Notes should be _individually addressable_. That is, linkable, no matter how they are implemented in terms of documents (see below).
    + Notes should be immediately and rapidly _searchable_. This may require two parallel systems, such as markdown files and a graph database to implement this.

While it may not be obvious, the note is related to a **document** in an ambiguous way; that is, there is more than one way to make a note out of a document.

+ Document
  + A document is a single _written text_ within the system (see below)
  + It is synonymous with "file" in our usage
    + It is often overloaded with the term note, but this is based on the **strategy** you are using. (See `design_notes.md` for "strategy.")
      + A note may be a single file or it may exist with other notes within a file.
      + In this system we definitely want to make any uploaded texts first-class citizens of the search and linking functions. (For example, drafts of blog posts or drafts of scientific papers would be treated by the system in the same way that notes would be. If notes _must_ be distinguished, then they can be tagged in some way or distinguished with metadata.)
+ Location
  + A location is a unique place within a document
  + A document itself may be a location (the coarsest grained location in the system?)
  + A _part_ of a document may also be a location
    + The most common parts of documents used as locations are _headers_ (_a la_ Obsidian's linking system)
  + We observe that _in any system that we are aware of_, any note must be able to be made into a location given the individually addressable requirement of notes. That is the linking of notes requires that notes be locations:

> Every note must be a location, but it is not necessary that every location **is** a note.
  +



+ Link
  + A link is a connector between documents
  + There are a variety of links
    + Hard (Forward) Links -- These are manually inserted links between documents

ttt

+ Written Text
  + We treat "written text" as synonymous, usually, with Markdown or a direct extension of Markdown.
    + Direct extension being one of the markdown flavors generally available or the addition of other (interpreted or uninterpreted) syntax, for instance, LaTeX or a diagramming language.
    + Tools should pass over these embedded syntaxes in silence if the tool cannot interpret the extra features of the syntax.

    +

## Syntax

+ Markdown
  + At it's root, this is a Markdown based system, and Markdown is mostly **plain text**.
  + This is done for various reasons:
    + **Future-proofing**: Text (Markdown) files are always human readable.
    + **Simplicity**: People can learn enough of Markdown to use it productively in much less than an hour.
    + **Visual Appeal**: Most people can read "uncompiled" Markdown without requiring CSS or other formatting. Additionally tools exist for some live translation of Markdown in an editor context (_a la_ VSC's live Markdown "semi-preview.")
    + **Easy translation**: Via `pandoc` and other tools, Markdown is easy to use to create other document formats like LaTeX and Microsoft Word, etc.
    +
+ Links
  + Wiki-style links are the default in most of these systems
    + We enforce these over markdown links which are also allowed but not processed by the enhanced features of the system.
    + Links are **not** tags.
+ Tags
  + Markdown syntax seems to allow for hashtags
  + These natively conflict with the default header styles, but this is not a problem for most systems, that treat strings beginning with hashtags as tags, and those beginning with the string "`# `" (pound sign followed by space) as headers.
