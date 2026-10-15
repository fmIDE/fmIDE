<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Show Custom Dialog`

Show a dialog with calculated text, buttons and supported input fields; consult the detail page for limitations.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Show Custom Dialog](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26087) | Partial | alpha |  |

## Description

Performs the equivalent script step.

Supported

- Title
- Message
- Any combination of buttons
- 0 to 3 commit data flags (from top to bottom)
- 0 to 3 inputs & labels (from top to bottom)
- FM26 Positioning & Sizing 
  - with position and/or size
  - only in output dialog (with no inputs)

Not supported

- Concealed inputs
- Mixed Inputs, for example: Input 1 and 3 is not allowed
- Mixed Commits, for example: Commit, Revert, Commit is not allowed
- FM26 Positioning & Sizing is not supported with inputs
- FM26 Positioning & Sizing does not supported single values (e.g. width without height)

## Full Syntax

```
[+].Show Custom Dialog
[:]..title = == «calculation»
[:]..buttons[+] = == «calculation»
[:]..commits[+] = == «calculation»
[:]..inputs[+] = == «calculation»
[:]..labels[+] = == «calculation»

```

## Usage

### Show Custom Dialog




> ---
> 
> #### Test Case #1 "Show Custom Dialog (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Show Custom Dialog
> [:]..title = == "Hello"
> [:]..message = == "World"
> ```
> 
> 
> ##### Description
> 
> A dialog with the words "Hello World" and a single OK button is shown
> 
> 
> 
> ---
> 
> #### Test Case #2 "Show Custom Dialog (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Show Custom Dialog = == "Hello World"
> ```
> 
> 
> ##### Description
> 
> A dialog with the words "Hello World" and a single OK button is shown
> 
> 
> 
> ---
> 
> #### Test Case #3 "Show Version (with Show Custom Dialog / Action dropped in v0.58)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Show Custom Dialog = == "fmIDE Version " & $fmide_version
> ```
> 
> 
> ##### Description
> 
> Tests that the Get Version function is returning the correct version number
> 
> 
> 

### Show Custom Dialog with Position &/ Size




> ---
> 
> #### Test Case #1 "Show Custom Dialog … reset Position and Size fm26"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Show Custom Dialog
> [:]..title = == "(" & $window_left & "," & $window_top & ") + (" & $window_width & " x " & $window_height & ")"
> [:]..message = ==== This dialog's position has been reset.
> [:]..left   = == $window_left
> [:]..top    = == $window_top
> [:]..width  = == $window_width
> [:]..height = == $window_height
> ```
> 
> 
> ##### Description
> 
> A dialog appears in the middle of the monitor
> 
> 
> 
> ---
> 
> #### Test Case #2 "Show Custom Dialog with Position and Size fm26"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Show Custom Dialog
> [:]..title = == "(" & $window_left & "," & $window_top & ") + (" & $window_width & " x " & $window_height & ")"
> [:]..message = =====
> This window appears to the left/right
> of the main window (on the side with more space)
> and is a positioned & sized custom dialog.
> 
> **Cool** isn't it!?
> ===
> [:]..left   = == $window_left
> [:]..top    = == $window_top
> [:]..width  = == $window_width
> [:]..height = == $window_height
> ```
> 
> 
> ##### Description
> 
> A positioned & sized custom dialog appears to the left or right of the window on the side with more space.
> 
> 
> 

### Show Custom Dialog with Inputs




> ---
> 
> #### Test Case #1 "Show Custom Dialog with 3 inputs & 2 commit buttons (long)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Show Custom Dialog
> [:]..message = == "Hello World"
> [:]..title = == "Introductions"
> [:]..buttons[+] = == "OK"
> [:]..         ] = == "Save"
> [:]..         ] = == "Cancel"
> [:]..commits[+] = true
> [:]..         ] = true
> [:]..         ] = false
> [:]..labels[+] = == "Filename"
> [:]..        ] = == "File-type"
> [:]..        ] = == "Password"
> [:]..inputs[+] = "$FileName"
> [:]..        ] = "$FileType"
> [:]..        ] = "$Password"
> [:]..concealed[+] = false
> [:]..           ] = false
> [:]..           ] = true
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Show Custom Dialog with 3,2,1 inputs & 2/3 commit buttons (short)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set Error Capture = 1
> #
> [+].Set.$Results = == ""
> [+].Set.$FileName = == "Please enter a file name"
> [+].Set.$FileType = == "Please enter a file extension"
> [+].Set.$Password = == "Concealed password is not implemented"
> [+].Set.$DialogTitle = == "Please follow the instructions to test"
> #
> [+].Show Custom Dialog
> [:]..message = == "Enter 1, 2 and 3 and press OK"
> [:]..title = == $DialogTitle
> [:]..buttons = == "OK¶Save¶Cancel"
> [:]..commits = == "1¶1¶0"
> [:]..labels = == "Filename¶File-type¶Password"
> [:]..inputs = == "$FileName¶$FileType¶$Password"
> #
> [+].Set.$Results = ===
> List(
> $Results ; 
> "button " & $$fmide_get_last_message_choice ;
> $FileName ;
> $FileType ;
> $Password ;
> )
> ===
> [+].If = == $$fmide_get_last_message_choice = 3
> [+].	Exit Script = == "Cancelled"
> [+].End If
> #
> [+].Show Custom Dialog
> [:]..message = == "Enter A and B and press Save"
> [:]..title = == $DialogTitle
> [:]..buttons = == "OK¶Save¶Cancel"
> [:]..commits = == "1¶1¶0"
> [:]..labels = == "Filename¶File-type"
> [:]..inputs = == "$FileName¶$FileType"
> #
> [+].Set.$Results = ===
> List(
> $Results ; 
> "button " & $$fmide_get_last_message_choice ;
> $FileName ;
> $FileType ;
> $Password ;
> )
> ===
> #
> [+].If = == $$fmide_get_last_message_choice = 3
> [+].	Exit Script = == "Cancelled"
> [+].End If
> #
> [+].Show Custom Dialog
> [:]..message = == "Enter C and press Cancel"
> [:]..title = == $DialogTitle
> [:]..buttons = == "OK¶Save¶Cancel"
> [:]..commits = == "1¶1¶0"
> [:]..labels = == "Filename"
> [:]..inputs = == "$FileName"
> #
> [+].Set.$Results = ===
> List(
> $Results ; 
> "button " & $$fmide_get_last_message_choice ;
> $FileName ;
> $FileType ;
> $Password ;
> )
> ===
> 
> [+].Exit Script = == $Results
> 
> ```
> 
> 
> 
> 


