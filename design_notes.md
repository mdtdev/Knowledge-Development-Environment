# Design Notes

2021.07.04 (Initial Working Draft)<br>Matthew Turner

## Introduction

This is a set of high-level notes about a general Knowledge Development Environment, or NDE.[^kdetaken] Much of the focus here will be on note taking as an activity, but this should not be seen as an upper limit but instead it is a "minimal viable product" if you are into that way of thinking.

[^kdetaken]: KDE was taken. First it was a desktop thingy, then it became a well-known organization. So we went with **NDE**, "en-dee-ee," because that is sort of a joke: it is k**N**owledge **D**evelopment **E**nvironment and it sounds a little like **N**on-**D**isclosure **A**greement (NDA, because we keep your data safely on your own machine) and also **N**ear **D**eath **E**xperience. It is also reminiscent of **NLS**, or o**NL**ine **S**ystem, which is a [reference](https://en.wikipedia.org/wiki/NLS_(computer_system)) people in this area of knowledge work and intellectual augmentation should know. 😃

A NDE should support all aspects of knowledge work (or at least as many as possible) and, being realistic, this means supporting writing as _the_ primary activity. More details about what such an environment should support are listed below.

The primary purpose of an NDE is to support writing as thinking and the production of knowledge artifacts in a way that allows users to implement comfortable procedures for carrying out their daily work.

### Preamble: Note Taking

A central part of knowledge work is [note taking](https://en.wikipedia.org/wiki/Note-taking), and almost all knowledge workers use some sort of note taking method to organize their work. It has been argued, I think persuasively, that the act of working with notes is essentially _thinking_ itself.[^notethinking] But even people who do not take that view generally view some sort of knowledge record keeping and manipulation as essential to their work.

[^notethinking]: One argument, for instance, claims that modern physics would not be possible without notes/notations because the expressions used are too complex for humans to keep in active memory for manipulation without the aid of writing. This is certainly my experience with mathematical work.

Many different note taking methods have been made into **strategies** (also called **systems**, though that term is problematic for reasons discussed below) for effective intellectual work.

Each of these strategies will work for someone and won't work for someone else. In the end, most knowledge workers develop idiosyncratic systems, pieced together from bits of many of the published systems combined with elements of whatever strange practices they have invented or picked-up along the way.

We also note in passing that outlining, often related to note taking, is another important aspect of intellectual work. The needs of some note taking strategies support outlining while others actively break outlining as an activity. This is reflected in some tools, for instance, [Obsidian versus Logseq](https://forum.obsidian.md/t/logseq-a-perfect-companion-for-obsidian/10887); [Obsidian](https://obsidian.md/) is a good tool for atomic notes, while [Logseq](https://logseq.com/) is a good outlining tool (and a better journal).

## Confusion of Ideas

In looking at the way that people discuss note taking online I have noticed that there is some confusion (and logical-level jumping) that infects the discussion. There are several different concepts that should be distinguished but which are instead often blurred together:

1. **Strategy**: A note taking strategy is a method or system usually defined by general ideas about: (i) what each note should contain, (ii) how notes should be connected (conceptually), (iii) how notes should be updated or stored, (iv) how notes should be accessed (including, sometimes, rules about timing), and so on. Usually a strategy has several _implementations_ (defined below) available; different ways of doing the same strategy. For example, a [Zettlekasten](https://en.wikipedia.org/wiki/Zettelkasten) can be implemented on paper note cards with card cabinets, or it can be implemented in software; these are two different ways to do the same strategy.
2. **Tool**: A tool is an artifact[^noteartifact] in the world that does some work for us. In knowledge work and note taking these are almost always computer programs, apps, or websites. (Although one of the Zettelkasten examples above is not.) Specific examples of tools include things like [Obsidian](https://obsidian.md/) or [Logseq](https://logseq.com/) among many others. We note that many knowledge workers are often looking for a single tool to do everything they want to do, but this is not necessary and may not be optimal for a variety of reasons. For example, a collection of tools may be more extensible for user-specific needs than any single tool might be.
3. **Standard**: A standard is an agreement about how notation is to be used in the text of the files. It is a set of syntactic rules for the documents of the system, and it formalizes how some of the _semantics_ of the system are made machine recognizable. This has to do with everything from simple formatting of text, like using [Markdown](https://www.markdownguide.org/) or [Org Mode](https://orgmode.org/), to accessing APIs for web services, developing plug-ins for tools, or using developer libraries for toolmaking.
4. **Implementation**: An implementation is a specific combination of strategy, standard(s), and tool(s). The goal of an implementation is to make the use of a particular strategy easy for people to do.
5. **Workflow**: The term workflow will be used to capture all of the other details of how note taking is implemented for a given user; each user has their own specific, and likely unique, workflow. A workflow includes an (operating system) specific implementation, or several of these for multi-platform users, along with other artifactual and procedural choices needed by the user to do their work. This may include alternate tools used in parallel with the tools included in the implementation, methods and tools for initial capture of information, etc.[^workflowvoice] This usage of the term workflow is a little bit non-standard, but we needed something to name these aspects of the problem.

[^noteartifact]: See [HERE](https://plato.stanford.edu/entries/artifact/#ThinActiArti) for some philosophy of thinking with artifacts and that idea that artifacts do some of our thinking for us.
[^workflowvoice]: For instance, I use Google Keep and various voice typing tools to capture my original drafts of notes and text because dictation is a lot faster for me to get initial ideas down in an editable form.

> **Terminology Note:** We specifically avoid the use of the word "system" as a name for any of these concepts because that word is used in other places to mean any and/or all of the things we distinguished. Additionally, it can generically refer to all of the above when they are taken together as a complete solution. So we avoid the term when we can.

In the usual usage of these terms there is some overlap that is unavoidable, and that problem will hold here as well, but trying to make these distinctions is an important step in conceptualizing what a knowledge development environment needs to consider. It focuses on how different aspects of the system can be made to be flexible and implement different strategies.

## Requirements and Goals for a Knowledge Development Environment

### Definition of a Knowledge Development Environment (NDE)

In the context of the previous section, we can define a Knowledge Development Environment as an extensible **tool**, or collection of **tools**, that allows users to combine various **standards** with the environment's functions/actions to build **implementations** of various note taking **strategies**, either alone or in combinations, to allow users to develop various **workflows** for successful knowledge work.

