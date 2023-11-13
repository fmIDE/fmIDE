# fmIDE-Services

fmIDE-Services provide the glue between fmIDE and the FileMaker GUI.

 There are two fmIDE-Services - macOS Services to integrate fmIDE seamlessly into your FileMaker workflows on your Mac:

- `fmIDE > Store Clipboard to Keyboard Buffer`
  - Places the current clipboard text into the fmIDE keyboard buffer (file in the documents folder)
- `fmIDE > Retype Keyboard Buffer`
  - Retypes the content of the fmIDE keyboard buffer

## Contents

- Installing fmIDE-Services
- Setting up fmIDE-Services
- Using fmIDE-Services
- Deinstalling fmIDE-Services
- fmIDE-Services Reference



## Installing fmIDE-Services

You can install the fmIDE-Services simply from the Finder.

The Services files are in the fmIDE-Services / fmIDE-Services folder

Just 

- double-click the file to automatically install it.

Note:

- This will *move* the file to the Services folder (~/Library/Services).
- If you would like to keep a copy of the file, then 
  1. First copy the files you want to install to a subfolder,
  2. and then double click them

## Setting up the fmIDE-Services

To set up the fmIDE Services you need to bind them to a keystroke.

The recommended keys are

|   Key | fmIDE Service
|-------|---------------------------------------
|   F12 | fmIDE > Retype Keyboard Buffer
| ⌘ F12 | fmIDE > Store Clipboard to Keyboard Buffer

Of course, you can bind the services to any key you wish, however, note that since the `Retype Keyboard Buffer` service re-types the contents of the Keyboard Buffer file, it must be triggered by a simple key with no modifiers to avoid the modifier keys interfering with the reytyping!

To bind the services to a key:

1. Open System Preferences
2. Navigate to the Keyboard section
3. Navigate to the Shortcuts section
4. Select the Services tab
5. Scroll until you find the fmIDE services listed
6. Bind each service to the desired key

## Using fmIDE-Services with fmIDE

When you use fmIDE to jump to a specific object in the FileMaker IDE, such as a field in the database definition, fmIDE can only automatically take the user _part of the way_ there. 

Once a GUI dialog is open fmIDE can no longer control the GUI.

For example, when jumping to a field definition, 

1. fmIDE can jump to the correct layout context 
2. and can open the database definition dialog,
3. but it _cannot_ automatically click on the fields tab, if it is not selected,
4. and it _cannot_ automatically spring to the desired field.

The last stage needs the user to perform one or two manual steps, to reach the final destination:

1. If it is not already in focus, change to the field tab
2. Click in the field list
3. Press F12 to retype the fields name
   - This retypes the field name
4. If necessary, check and adjust the selected item


### Example use case

The user wants to 

FIXME


## Using fmIDE-Services with the clipboard

Sometimes it can be useful to use the fmIDE Keyboard Buffer instead of the clipboard, or to free up the clipoard for some other content

When you have the name

1. Press ⌘12 to store the current clipboard into the fmIDE Keyboard Buffer
2. Copy some other content to the clipboard
3. Navigate to the place in the FileMaker GUI
4. Paste the clipboard contents
5. Press 

 ### Example use case

The user wants to …FIXME

## What about Windows?

fmIDE is potentially usable on Windows - atz least to some extent.

With an appropriate keyboard macro programme we can probably achieve similar results.

If you are interested in helping devloping fmIDE on the Windows platform, please contact me.

## More Help

FIXME

## Deinstalling fmIDE-Services

fmIDE-Services not what you need?

Then just…

- Open the Services folder (~/Library/Services).
- Delete any files you don't want
  - or move them back to the fmIDE-Service folder

## fmIDE-Services Reference



 `Services > fmIDE > Retype Keyboard Buffer`

Retypes whatever is on the clipboard. Similar to pasting, but a tab character will jump to the next field.



`Services > fmIDE > Store Clipboard to Keyboard Buffer`

Places the current clipboard text into the fmIDE keyboard buffer (file in the documents folder)