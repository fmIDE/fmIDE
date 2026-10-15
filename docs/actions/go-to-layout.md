<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Layout`

Navigate to a layout by name, number, ID or original layout; shorthand text denotes a name and shorthand numbers denote a layout number.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to Layout](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26006) | Yes | beta | v0.1 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Go to Layout
[:]..by: "original" | "selection" | "name" | "number" | "id"
[:]..layout_name: «string» or «calculation» 
[:]..layout_number: «number» or «calculation»
[:]..layout_id: «number» or «calculation»
[:]..with_dialog: «boolean» or «calculation»

```

## Usage

### Go to Layout original layout


Returns to the layout that was active at the start of the fmIDE Action Script


> ---
> 
> #### Test Case #1 "Go to Layout.by = "original layout""
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
> [+].Go to Layout.by = "original layout"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Layout = ( short form = go to original layout )"
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
> [+].Go to Layout = 
> ```
> 
> 
> 
> 

### Go to Layout selected layout


Goes to the layout with the given layout_name


> ---
> 
> #### Test Case #1 "Go to Layout = «selected layout» (short form)"
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
> [+].Go to Layout = "Home"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Error: Go to Layout"
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
> [+].Go to Layout="this layout does not exist"
> ```
> 
> 
> 
> 

### Go to Layout by layout name


Goes to the layout with the calculated layout_name


> ---
> 
> #### Test Case #1 "Go to Layout.by = "name""
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
> [+].Go to Layout
> [:]..by = "name"
> [:]..layout_name = == $layout_name
> ```
> 
> 
> ##### Description
> 
> FIXME: Go to Layout.by="name" BUT Perform Script.specified= "By name"
> 
> 
> 

### Go to Layout by layout number


Goes to the layout with the calculated layout_number


> ---
> 
> #### Test Case #1 "Go to Layout = «layout_number» (short form)"
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
> [+].Go to Layout = 1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Layout = «layout_number»+1"
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
> [+].Go to Layout
> [:]..by = "number"
> [:]..layout_number = == Get( LayoutNumber ) + 1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Go to Layout.by="number""
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
> [+].Go to Layout
> [:]..by = "number"
> [:]..layout_number  = == $layout_number
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Go to Layout.by="number" -1 = last Layout (long form)"
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
> [+].Go to Layout
> [:]..by = "number"
> [:]..layout_number  = -1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Go to Layout ( short form = go to original layout )"
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
> [+].Go to Layout
> ```
> 
> 
> 
> 

### Go to Layout by layout id


Goes to the layout with the calculated layout_id


> ---
> 
> #### Test Case #1 "Go to Layout.by="id""
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
> [+].Go to Layout
> [:]..by = "id"
> [:]..layout_id  = == $layout_id
> ```
> 
> 
> 
> 


