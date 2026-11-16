---
title: NSTX909 project-already-exists
description: '`nstx init` was run in a folder that already holds `nimblestax.platform.yaml`.'
generated: true
nimblestax_version: 0.1.0
---

## What it checks

`nstx init` was run in a folder that already holds `nimblestax.platform.yaml`.

## Why

`nstx init` writes a new project. Writing it over an existing one would replace the Platform Contract and every starter file you've edited, so it writes nothing instead. Other files in the folder are fine, so a new Git repo with a README works.

## Example

In a project, this fails:

```console
$ nstx init
```

## Fix

Run `nstx init` in another folder, or give it one, as `nstx init <folder>`.
