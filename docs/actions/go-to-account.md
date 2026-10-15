<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Account`

Open Manage Security and prepare an account name in the fmAutoMate keyboard buffer for manual selection.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.10 |

## Description

Goes to the given account.

1. Stores the account name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Manage Security` dialog

## Full Syntax

```
[+].Go to Account
[:]..account_name = «account_name»
[:]..by = "name"|"selected"
```

## Usage

### Go to Account




> ---
> 
> #### Test Case #1 "Go to Account (Script does not continue - use Hiatus)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test ⛔️ HALTS 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Account = == "user"
> ```
> 
> 
> 
> 


## See also

- [Go to Privilege Set](go-to-privilege-set.md)
