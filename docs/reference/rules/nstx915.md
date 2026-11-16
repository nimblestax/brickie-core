---
title: NSTX915 skill-edited
description: '`nstx skills update` found a Nimblestax Skill edited since Nimblestax wrote it.'
generated: true
nimblestax_version: 0.1.0
---

## What it checks

`nstx skills update` found a Nimblestax Skill edited since Nimblestax wrote it.

## Why

Each Nimblestax Skill records a digest of the text Nimblestax wrote. A skill whose text no longer matches was edited, and updating it would lose the edit, so `nstx skills update` writes nothing and shows the difference instead. Exits 2.

## Example

A step was added to `.claude/skills/nimblestax-add-model/SKILL.md`. In a project, this fails:

```console
$ nstx skills update
```

## Fix

Move your edit into a skill of your own, outside the `nimblestax-*` folders, and run `nstx skills update` again. To replace the edit, run `nstx skills update --force`.
