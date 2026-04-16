---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3
  language: python
  name: python3
title: Installation
abstract: ""
authors:
  - name: Author Name
exports:
  - format: typst
    template: lapreprint-typst
    output: _build/exports/typst/
---

# Installation

This chapter covers how to set up your environment.

## Prerequisites

List the prerequisites here.

## Installation Steps

```bash
pip install numpy matplotlib
```

## Verifying the Installation

```{code-cell} ipython3
import sys
print(f"Python version: {sys.version}")
```
