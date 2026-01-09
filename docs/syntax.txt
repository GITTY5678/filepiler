# Filepiler Language Syntax

Filepiler is a lightweight, file-system–oriented scripting language.
It is designed to inspect and manipulate files using simple, readable commands.

Each instruction is written on a separate line and executed sequentially.

---

## General Syntax Rules

- Every command starts with `@`
- Arguments are passed using `->`
- Commands are case-sensitive
- Empty lines are ignored
- Whitespace around operators is ignored
- Errors are reported with line numbers and do not crash execution

---

## 1. @view — View Files and Directories

### Syntax

@view -> <path>


---

### Description
Displays information about the given path.

- If `<path>` is a directory, its contents are listed
- If `<path>` is a file, basic file information is displayed

---

### Behavior
- Differentiates between directories and files
- Handles permission errors safely
- Supports both relative and absolute paths

---

### Examples

View the current directory:

@view -> .


View a specific directory:
@view -> C:/Users/HARIHARA SUTHAN/Downloads

View a file
@view -> filepiler.py