# File Manager

file_manager. A Python package built by ImhimLM.
---

## Table of Contents

* [How to Import and Use](#how-to-import-and-use)
* [Features](#features)
* [Functions](#functions)
    * [Files](#files)
    * [Folders](#folders)
    * [Disk Image](#disk-image)
* [Credits](#credits)

The file_manager package is meant to edit and modify the user's local computer files. This includes creating directories and files. The package is very simple to use and understand as it has basic functions.

<div id = "how-to-import-and-use">

## How to Import and Use

Download the folder and place it into your Python project, then use the following:
```python
from file_manager import file_manager as files
```

Then use `files.` before calling any function, here's an example:
```python
from file_manager import file_manager as files

files.createFile(path)
```
</div>

<div id = "features">

## Features

* Creating, renaming, removing, cloning and moving files and directories
* Find the file size of files and directories
* Reading and writing in files
</div>

<div id = "functions">

## Functions

<div id = "files">

### Files

* `createFile(path)`, Creates a file in a specified directory. *path* is replaced with the desired path
* `removeFile(path)`, Removes a file (Warning: Files skip the trash bin!). *path* is replaced with the desired path
* `renameFile(path, name)`, Renames a file. *path* is replaced with the desired path, *name* is replaced with the desired name
* `copyFile(path, destination)`, Copies a file to another directory. *path* is replaced with the desired path, *destination* is replaced with the desired destination
* `moveFile(path, destination)`, Moves a file to another directory. *path* is replaced with the desired path, *destination* is replaced with the desired destination
* `writeFile(path, text, line = None, writeType = 'add')`, Writes in a text file. *path* is replaced with the desired path, *text* is replaced with any string, *line* (optional) defines where the text is written, *writeType* defines the way it writes (`add` adds text at the bottom, `insert` inserts text in the specified line, `replace` replaces the specified line with text)
* `readFile(path, line = None)`, Reads a text file. *path* is replaced with the desired path, *line* (optional) defines what line should be read
* `clearLine(path, line)`, Clears a line in the specified text file. *path* is replaced with the desired path, *line* defines what line should be erased
* `clearFileContent(path)`, Clears a text file's content. *path* is replaced with the desired path
* `getFileSize(path, formatted = False)`, Gives the file size of the specified file. *path* is replaced with the desired path, *formatted* (optional) formats the result (*if formatted is set to True*)
* `findFile(path)`, Says if a file exists or not, *path* is replaced with the desired path
* `getDirectory()`, Says the path of the current file (*That ran the function*)
</div>

<div id = "folders">

### Folders

* `createDirectory(path)`, Creates a directory. *path* is replaced with the desired path
* `removeDirectory(path)`, Removes a directory and its contents (Warning: The directory will skip the trash bin!). *path* is replaced with the desired path
* `renameDirectory(path, name)`, Renames a directory. *path* is replaced with the desired path, *name* is replaced with the desired name
* `copyDirectory(path, destination)`, Copies a directory to another directory. *path* is replaced with the desired path, *destination* is replaced with the desired destination
* `copyDirectoryContent(path, destination)`, Copies a directory's content to another directory. *path* is replaced with the desired path, *destination* is replaced with the desired destination
* `getDirectoryContent(path)`, Reads the content of a directory. *path* is replaced with the desired path
* `clearDirectoryContent(path, limit = 1000000)`, Clears the content of a directory. *path* is replaced with the desired path, *limit* (optional) defines the maximum amount of files that can be deleted
* `countFiles(file, path = '/')`, Counts the amount of files (with a specific name) in a directory. *file* is replaced with the file name, *path* (optional) defines the path for where to look
* `countAllFiles()`, Counts the total amount of files in the user's computer
</div>

<div id = "disk-image">

### Disk Image

* `diskStorageUsed(formatted = False)`, Says the amount of storage used on the user's computer. *formatted* (optional) formats the result (*if formatted is set to True*)
* `diskStorageFree(formatted = False)`, Says the amount of free storage on the user's computer. *formatted* (optional) formats the result (*if formatted is set to True*)
* `diskStorageTotal(formatted = False)`, Says the total storage on the user's computer. *formatted* (optional) formats the result (*if formatted is set to True*)
</div>
</div>

<div id = "credits">

## Credits

Made by ImhimLM.
</div>
