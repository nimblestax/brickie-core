---
title: NSTX916 unknown-example
description: '`nstx init --example` names an example Nimblestax doesn''t ship.'
generated: true
nimblestax_version: 0.1.0
---

## What it checks

`nstx init --example` names an example Nimblestax doesn't ship.

## Why

`nstx init --example` writes one of the example projects that ship inside Nimblestax, so the example always matches the Nimblestax you have installed. The diagnostic lists the examples there are. It exits 2, because the command line needs a change.

## Example

In a project, this fails:

```console
$ nstx init --example teapot
```

## Fix

Name an example the diagnostic lists, such as `nstx init --example kettle`.
