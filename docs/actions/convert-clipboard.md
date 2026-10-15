<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Convert Clipboard`

Convert supported FileMaker clipboard content between its available representations.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta |  |

## Description

Converts the Clipboard between FileMaker objects and xml.

## Full Syntax

```
[+].Convert Clipboard
[:]..to = "xml"|"object"
```

## Usage

### Convert Clipboard to «type»


The clipboard is converted to the given type


> ---
> 
> #### Test Case #1 "Convert Clipboard to obj ( xml ) → obj"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Convert Clipboard.to = "object"
> ```
> 
> 
> ##### Description
> 
> Automatically converts the fmxmlsnippet XML to a FileMaker object
> 
> 
> 
> ---
> 
> #### Test Case #2 "Convert Clipboard.to xml ( obj ) → xml"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Convert Clipboard.to = "xml"
> ```
> 
> 
> ##### Description
> 
> Automatically converts the copied FileMaker object to fmxmlsnippet XML
> 
> 
> 
> ---
> 
> #### Test Case #3 "Convert Clipboard.to xml ( xml ) → xml"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Convert Clipboard.to = "xml"
> ```
> 
> 
> ##### Description
> 
> Source and target types are the same -> does nothing
> 
> 
> 

### Convert Clipboard = toggle


With no parameter the clipboard is toggled between xml and objects


> ---
> 
> #### Test Case #1 "Convert Clipboard ( xml ) → obj"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Convert Clipboard
> ```
> 
> 
> ##### Description
> 
> Automatically converts fmxmlsnippet to FileMaker object(s)
> 
> 
> 


