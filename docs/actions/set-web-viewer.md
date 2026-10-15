<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Web Viewer`

Navigate, reload, reset or move through a named web viewer's history.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Web Viewer](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26146) | Yes | alpha | v0.79 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Set Web Viewer
[:]..object_name = == «calculation»
[:]..action = "Go to URL"|"Reset"|"Reload"|"Go Back"|"Go Forward"
[:]..url = == «calculation»
```

## Usage

### Set Web Viewer Go to URL


Goes to the given url.

Note: If a url is supplied but no action, fmIDE defaults to `Go to URL`


> ---
> 
> #### Test Case #1 "Set Web Viewer Go to URL (long form)"
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
> [+].Set Web Viewer
> [:]..object_name = == $webviewer_name
> [:]..action = "Go to URL"
> [:]..url = == $url
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Web Viewer Go to URL (short form)"
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
> [+].Set Web Viewer.TestWebViewer = == $url
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Set Web Viewer.«name».action = Reset (short form)"
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
> [+].Set Web Viewer.TestWebViewer.action = "Reset"
> ```
> 
> 
> ##### Description
> 
> Tests that "action" doies not become part of the web viewer name
> 
> 
> 

### Set Web Viewer Action


Choose from `Reset`|`Reload`|`Go Back`|`Go Forward`|


> ---
> 
> #### Test Case #1 "Set Web Viewer Reset (long form)"
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
> [+].Set Web Viewer
> [:]..object_name = == "TestWebViewer"
> [:]..action = "Reset"
> ```
> 
> 
> 
> 


## See also

- [Perform JavaScript in Web Viewer](perform-javascript-in-web-viewer.md)
