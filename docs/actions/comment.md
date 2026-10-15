<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `#`

Add a comment to an action script; fmIDE ignores its content.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | ok | v0.3 |

## Description

A comment step. Ignored by fmIDE.

Beware using the deprecated legacy format!

- It is tempting, because it looks more like FileMaker step text,
- however, it can - and will one day - break your JSON (for example if it contains a double dot `..`)!

## Full Syntax

```
[+].# = «comment»

# or

# legacy format - DEPRECATED AND NOT RECOMMENDED

[+].# «comment»

```

## Usage

### # legacy format




> ---
> 
> #### Test Case #1 "# (legacy format comment)"
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
> [+].# This is the legacy comment syntax
> ```
> 
> 
> ##### Description
> 
> This legacy convenience form is not for use with "."s in the comment text
> 
> 
> 
> ---
> 
> #### Test Case #2 "Error: # (legacy format)"
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
> [+].# This legacy comment contains characters … [{6]}} … that form an invalid JSON path!
> ```
> 
> 
> ##### Description
> 
> This test  shows how an unlucky comment can lead to the entire JSON getting trashed 
> 
> 
> 

### # = == text value format




> ---
> 
> #### Test Case #1 "# (= format comment)"
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
> [+].# = == This is the prefered way to encode a comment. // It can contain dots!
> ```
> 
> 
> ##### Description
> 
> A comment is encoded as a "#" key whose value is the text of the comment.
> 
> 
> 


