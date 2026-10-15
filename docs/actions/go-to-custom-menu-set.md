<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Custom Menu Set`

Open Manage Custom Menus and prepare a menu-set name in the fmAutoMate keyboard buffer; final selection is manual.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | alpha | v0.12 |

## Description

Goes to the given Custom Menu Set, if possible(1).

1. Stores the custom_menu_set_name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Manage Custom Menus` dialog

You must manually:

- select the Custom Menu Sets view
- click in the list
- press the fmAutoMate keyboard shortcut to retype the name

(1) Note: It is only possible to jump to custom privilege sets (because "[" cannot be typed in the list).

## Full Syntax

```
[+].Go to Custom Menu Set
```

## Usage

### Go to Custom Menu Set




> ---
> 
> #### Test Case #1 "Go to Custom Menu Set"
> 
> ##### Status
> 
> 🏧 automatic test 
> 
> 
> 
> 


## See also

- [Go to Custom Menu](go-to-custom-menu.md)
- [Go to Custom Menu Item](go-to-custom-menu-item.md)
