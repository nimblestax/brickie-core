---
title: NSTX102 unknown-kind
description: A `kind` isn't one Nimblestax knows.
generated: true
nimblestax_version: 0.1.0
---

## What it checks

A `kind` isn't one Nimblestax knows.

## Why

Nimblestax checks each file against its Kind's schema. A misspelt `kind` has no schema, so nothing in the file can be checked. `nstx schema` reports this Rule too when it's asked for a Kind that doesn't exist, and exits 2, because the mistake is on the command line.

## Example

Write this file into the project `nstx init` creates, and `nstx validate` fails:

`domains/sales/sources/orders.yaml`:

```yaml
kind: sauce
version: 1
path: /Volumes/{env}_sales/bronze/landing/orders
format: json
```

## Fix

Use one of the Kinds: `model`, `platform`, `seed` or `source`. `nstx schema <kind>` prints a Kind's fields.
