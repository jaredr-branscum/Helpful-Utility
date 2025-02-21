# Project to Text Merger (project_to_text_merger.py)

This Python utility script combines the contents of all files within a specified directory (and its subdirectories) into a single text file.  It offers options to ignore specific files or directories and excludes the script itself and the output file from the combined text.

## Features

* **Recursive Directory Traversal:** Combines files from the specified directory and all its subdirectories.
* **Ignore List:** Allows you to specify files and directories to exclude from the combined output.  Ignores recursively.
* **Output File Specification:** Lets you define the name of the output text file.
* **UTF-8 Encoding:** Handles a wide range of characters through UTF-8 encoding.

## Installation

1. Save the Python script (e.g., `project_to_text_merger.py`).
2. Ensure you have Python 3 installed.

## Usage

```bash
python project_to_text_merger.py [directory] [options]