---
title: Bioanalytical Procedures
author: Josh Morimoto
---

# How this works

Procedures are written in markdown (.md) and then converted to .html, .pdf, and
.docx using pandoc. This allows one file to control a web page, an easily
printable document, and an easily editable document.

## Document structure

Each instrument has its own folder. These folders contain images used in the
procedure and the full instrument manual, if available.

The templates folder holds styling files for making outputs look better.

The make_docs.bat file will convert the md files to all necessary outputs when
run.
