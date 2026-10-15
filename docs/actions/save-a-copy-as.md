<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Save a Copy as`

Save a copy, clone, compacted copy or self-contained copy of the database. Supply an explicit file path for unattended backups.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Save a Copy as](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26037) | Partial | alpha | v0.83 |

## Description

Saves a copy of the database to the given file path.

Great, or rather necessary, for making a backup before an AI-agent is let loose on your system.



Supported

- by
- file_path
- create_folders

Not fully Supported

- no file_path (you getz an error message before being able to choose the file)

## Full Syntax

```
[+].Save a Copy as
[:]..by = "copy"(default)|"clone"|"compacted"|"self-contained"
[:]..create_folders = == «boolean»
[:]..file_path = == «calculation»
```

