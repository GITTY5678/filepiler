# Filepiler Shell 🗂️

**Filepiler** is a custom, interactive, filesystem-oriented shell built in Python.  
It focuses on **file exploration, analysis, and monitoring**, rather than acting as a general-purpose OS shell.

This project was designed to understand how shells work internally:
- command parsing
- interpreter design
- session state
- filesystem operations
- performance-aware tooling

---

## ✨ Features

- Interactive shell (REPL)
- Persistent working directory (`cwd`)
- Relative & absolute path support
- Modular command system
- Real-time filesystem monitoring
- Performance-aware directory analysis

---

## 🧠 Core Concepts

- **Interpreter-based design**
- **Session state** (current directory)
- **Explicit syntax** (no magic guessing)
- **Filesystem-first philosophy**

---

## 📁 Project Structure

filepiler/
├── filepiler.py # Shell entry point (REPL)
├── engine/
│ ├── interpreter.py # Command routing & shell state
│ └── commands/
│ ├── view.py
│ ├── find.py
│ ├── info.py
│ ├── memory_sort.py
│ ├── watch.py
│ ├── create.py
│ └── delete.py
├── docs/
│ └── syntax.md
└── examples/
└── test.fp


---

## 🚀 Getting Started

### Requirements
- Python 3.9+
- Works on Windows, Linux, macOS

### Run the shell
'''bash
python filepiler.py

you should see

Filepiler Shell v1.0
Type @help for commands
fp>

📂 Filesystem Commands
View
@view -> <path>

Lists files and folders.

Find
@find -> <path>$<name>

Search for a file or directory by name.

Info
@info -> <path>

Displays detailed metadata:
size
type
file count
folder count

Create
@create -> <directory>$<filename>

Creates a new file.

Delete
@delete -> <path>

Deletes a file or directory.

Memory Sort
@memory_sort -> <directory>$<a|d>

Sorts files and folders by size.
a → ascending
d → descending

Includes ETA for large directories

Watch (Live Monitoring)
@watch -> <path>
@watch -> <path>$r

Default: non-recursive
$r: recursive watch
Detects:
file creation
deletion
modification
Stops with Ctrl + C

🧪 Example Session
fp> @pwd
fp> @cd -> Documents
fp> @view -> .
fp> @info -> report.pdf
fp> @memory_sort -> .$d
fp> @watch -> .$r
