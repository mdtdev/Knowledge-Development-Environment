# Design Notes

## Introduction

This is a set of notes about a general Knowledge Development Environment, or NDE. Much of the focus here will be on note taking as an activity, but this should not be seen as an upper limit but instead it is a "minimal viable product" if you are into that way of thinking.

>**Naming Note:** Obviously, KDE was already taken. First it was a desktop thingy, then it became a well-known organization. So we went with **NDE**, "en-dee-ee," because that is sort of a joke: it is k**N**owledge **D**evelopment **E**nvironment and it sounds a little like **N**on-**D**isclosure **A**greement (NDA, because we keep your data safely on your own machine) and also **N**ear **D**eath **E**xperience (make of that what you will). It is also reminiscent of **NLS**, or o**NL**ine **S**ystem, which is a [reference](https://en.wikipedia.org/wiki/NLS_(computer_system)) people in this area of knowledge work and intellectual augmentation should know. 😃

A NDE should support all aspects of knowledge work (or at least as many as possible) and, being realistic, this means supporting writing as _the_ primary activity. More details about what such an environment should support are listed below.

The primary purpose of an NDE is to support writing as thinking and the production of knowledge artifacts in a way that allows users to implement comfortable procedures for carrying out their daily work.

### Preamble: Note Taking

A central part of knowledge work is [note taking](https://en.wikipedia.org/wiki/Note-taking), and almost all knowledge workers use some sort of note taking method to organize their work. It has been argued, I think persuasively, that the act of working with notes is essentially _thinking_ itself. But even people who do not take that view generally view some sort of knowledge record keeping and manipulation as essential to their work.

>**Notes as Thought:** One argument, for instance, claims that modern physics would not be possible without notes/notations because the expressions used are too complex for humans to keep in active memory for manipulation without the aid of writing. This is certainly my experience with mathematical work.

Many different note taking methods have been made into **strategies** (also called **systems**, though that term is problematic for reasons discussed below) for effective intellectual work.

Each of these strategies will work for someone and won't work for someone else. In the end, most knowledge workers develop idiosyncratic systems, pieced together from bits of many of the published systems combined with elements of whatever strange practices they have invented or picked-up along the way.

We also note in passing that outlining, often related to note taking, is another important aspect of intellectual work. The needs of some note taking strategies support outlining while others actively break outlining as an activity. This is reflected in some tools, for instance, [Obsidian versus Logseq](https://forum.obsidian.md/t/logseq-a-perfect-companion-for-obsidian/10887); [Obsidian](https://obsidian.md/) is a good tool for atomic notes, while [Logseq](https://logseq.com/) is a good outlining tool (and a better journal).

## Confusion of Ideas

In looking at the way that people discuss note taking online, I have noticed that there is some confusion (and logical-level jumping) that infects the discussion. There are several different concepts that should be distinguished but which are instead often blurred together:

1. **Strategy**: A note taking strategy is a method usually defined by general ideas about: (i) what each note should contain, (ii) how notes should be connected (conceptually), (iii) how notes should be updated or stored, (iv) how notes should be accessed (including, sometimes, rules about timing), and so on. The key thing to understand about a strategy is that it has several _implementations_ (defined below) available; different ways of doing the same strategy. For example, a [zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) can be implemented on paper note cards with card cabinets, or it can be implemented in software; these are two different ways to do the same strategy.
2. **Tool**: A tool is an _artifact_ in the world that does some work for us. In knowledge work and note taking these are almost always computer programs, apps, or websites. (Although one of the zettelkasten examples above is not.) Specific examples of tools include things like [Obsidian](https://obsidian.md/) or [Logseq](https://logseq.com/) among many others.

We note that many knowledge workers are often looking for a _single_ tool to do everything they want to do, but this is not necessary and may not be optimal for a variety of reasons. For example, a _collection of tools_ may be more extensible for user-specific needs than any single tool might be.

>**Tools and Artifacts:** See [HERE](https://plato.stanford.edu/entries/artifact/#ThinActiArti) for some philosophy of thinking with artifacts and that idea that artifacts do some of our thinking for us.

3. **Standard**: A standard is an agreement about how notation (or syntax) is to be used in the text of the files. It is a set of syntactic rules for the documents that make up the strategy, and it formalizes how some of the _semantics_ of the strategy are made machine recognizable. This has to do with everything from simple formatting of text, like using [Markdown](https://www.markdownguide.org/) or [Org Mode](https://orgmode.org/), to accessing APIs for web services, developing plug-ins for tools, or using developer libraries for toolmaking.

A key feature of a **standard** is that it be well-defined.

Well-defined standards allow the development of software tools to check the validity of a document written to the standard. It also allows software to modify, process, or otherwise change the documents in the standard; eating standardized documents and emitting transformed standardized documents back.

**We also note that where there is one standard there can be two standards just as easily, as long as the design makes appropriate allowances for defining standards outside of the code used to process it**.

That is, standards should be defined by meta-data (XML, JSON) and the code that processes the standard should use such external definitions. This allows three things: changes to the standard to be made without requiring code updates, the implementation of multiple standards that can be used in parallel, and the modification of a given standard to be made by users to make the standards work better for them.

_We also note that personal modifications of the standard, made in meta-data, would be intrinsically shareable without the need to modify the core system_.

4. **Implementation**: An implementation is a specific combination of strategy, standard(s), and tool(s) to get some type of intellectual work done. The goal of an implementation is to make the use of a particular strategy easy for people to do.
5. **Workflow**: The term workflow will be used to capture all of the other details of how note taking is implemented for a given user; each user has their own specific, and likely unique, workflow. A workflow includes a (computer operating system specific) implementation, or several of these for multi-platform users, along with other artifactual and procedural choices needed by the user to do their work. This may include alternate tools used in parallel with the tools included in the implementation, methods and tools for initial capture of information, etc. This usage of the term workflow is a little bit non-standard, but we needed something to name these aspects of the problem.

>**Terminology Note:** We specifically avoid the use of the word "system" as a name for any of these concepts because that word is used in other places to mean any and/or all of the things we distinguished. Additionally, it can generically refer to all of the above when they are taken together as a complete solution. So we avoid the term when we can.

In the usual usage of these terms there is some overlap that is unavoidable, and that problem will hold here as well, but trying to make these distinctions is an important step in conceptualizing what a knowledge development environment needs to consider. It focuses on how different aspects of the system can be made to be flexible and implement different strategies.

## Requirements and Goals for a kNowledge Development Environment

### Definition of a kNowledge Development Environment (NDE)

In the context of the previous section, we can define a knowledge development environment as an extensible **tool**, or collection of **tools**, that allows users to combine various **standards** with the environment's functions/actions to build **implementations** of various note taking **strategies**, either alone or in combinations, to allow users to develop personal **workflows** for successful knowledge work.

### NDE as a Tool

Thought of as a tool, a NDE must meet the following requirements for it to be acceptable:

+ It must be **open source** and **free** in the various senses of those terms used in software development. We believe that building tools to support thinking and reasoning and then putting them behind paywalls, or otherwise limiting their use, is unethical. The only way to guarantee free usage for everyone is to use the open source model.
+ It must support user **privacy** by allowing the user to keep their data entirely local or to use any combination of tools to keep their data private (eg. [WebDAV](https://en.wikipedia.org/wiki/WebDAV), etc.).
+ It must be **extensible** and allow the user to implement different strategies through different standards. More importantly, it should be an **open system** that plays well with other systems (**interoperable**) to allow more complex workflows to be implemented.
	+ Ideally, standards should be implementable using well-defined and isolated settings files of some sort.
	+ "Plays well" includes both interoperability and import/export functions that allow users to move their data into NDE and out of it.
+ It must treat **Linux as a first-class operating system** and/or be **platform neutral**.
+ While not a strict requirement, allowing for a **plug-in architecture** allows multiple implementations and workflows and it should ideally support multiple user-interfaces.
+ It should support **writing as the primary activity** of knowledge work.
+ It should support the **creation of audio-visual media** at least via plug-ins, or interoperability with other software, if not natively.
	+ The expectation is that simple graphical things may be plug-in or built-in, but substantial media work is expected to be external. (Not looking for "photoshop" level of graphics editing to be built in.)
	+ This can be part of the open system specification allowing for the calling of other, unrelated, programs to create such media, allowing people to use their favorite tools in this area as integrated parts of the system.
	+ Note that extensive support for external programs encourages the construction of **system monitoring functions** such as directory watching.
+ It should support **local hosting of various kinds of media** and have close integration with media creating tools of various types as part of the larger open system architecture.
+ It should **render media from the web** similarly to how it renders and processes local media. That is, when reading a rendered document in the NDE, web based media should feel like local media in terms of interactions.

Some of these items are "obvious."

### Scale

Several of the tools available now use Markdown files in a directory as the primary data structure; it is currently open to question if this is going to scale when the number of note files hit 10,000 or 100,000 orders of magnitude. Certainly some OS's do not like folders with masses of tiny files; on Windows, for instance, the minimum file size is much larger than a zettelkasten style atomic note.

## Bootstrap Approach

Following the methods of the developers of [Foam](https://foambubble.github.io/foam/) we intend to use as many other programs and platforms as possible to alleviate the demand to create new tools _sui generis_.

Central to the development is a Markdown editor and there are plenty to choose from; programmer's editors are a good choice as most of them allow plug-ins to be developed that operate within the window of the editor. Foam uses [Visual Studio Code](https://code.visualstudio.com/) as its host program, and that one is reasonable as it allows running processes from within the IDE.

It is reasonable to assume that much of the development will depend on a client server model _a la_ [JupyterLab](https://jupyter.org/) or something along the lines of [Electron](https://www.electronjs.org/).

We are also interested in making command-line tools as these have the ability to serve as both function libraries for other GUI applications to call as well as form a collection of scriptable tools to use for maintenance of the strategies developed.

### "Route 1"

We are expecting to start by using a tool like [Obsidian](https://obsidian.md/) as a primary program to allow us to start working now. We will start with implementations of zettelkasten functions as command-line scripts (in Python) just to confirm that we have the right ideas about how to implement the needed functions in case the commercial and closed source projects (like Obsidian) go dark.

---
2021.08.01 (Initial Working Draft)<br>Matthew Turner
