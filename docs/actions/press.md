<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Press`

Send one or more key combinations through the supported keyboard automation.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.12 |

## Description

Send literal key characters, optionally with modifiers, to the current keyboard focus. Select the intended field or Script Workspace step first. This action changes the UI; it does not evaluate `key` or `command_key` as calculations.

- `key`: literal characters, processed in order. The scalar short form supplies this parameter.
- `command_key`: literal characters used when `key` is empty; a non-empty value also enables the Command/Control modifier.
- `shift`, `option`: runtime calculations controlling the additional modifiers.
- `times`: runtime repeat count, with a minimum/default of one.
- `pause`: runtime duration in seconds after each key. When omitted, the implementation pauses for 0.001 seconds to let FileMaker process the event.
- `delay`: currently read but never applied; do not rely on it to defer execution. See [issue #205](https://github.com/fmIDE/fmIDE/issues/205).

On macOS, the executing FileMaker application must be enabled in System Settings → Privacy & Security → Accessibility. [MBS documents this requirement](https://www.mbsplugins.eu/RemoteControlPressKey.shtml). A newer FileMaker installation may have a separate permission entry. Do not change security permissions without the user's approval.

For special characters, fmJAML can construct the literal character before the action runs: `Press.key = Char ( 8 )` sends backspace. `Press.key = == Char ( 8 )` would instead supply the expression text as keys.

Verified on FileMaker Pro 26.0.3 with MBS 16.4.0.08: Command-A selected all ten steps of the Hello World script while fmIDE was running. With Accessibility disabled, the same action returned -2 and MBS “Failed to send key”; enabling it restored error 0 and correct selection. This verifies selection, not unattended script editing. Capture errors immediately after Press.

## Full Syntax

```
[+].Go to Script
[:]..script_name = "Hello World"
[:]..script_step_number = 2
[+].Press
[:]..command_key = "a"
[:]..shift = == 0
[:]..option = == 0
[:]..times = == 1
[:]..pause = == 1 / 1000
```

## Usage

### Press.key




> ---
> 
> #### Test Case #1 "Press.key = "hello" (in a field)"
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
> [+].Press.key = == hello
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Press = "hello" (in a field) (short form)"
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
> [+].Press = == hello
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Press.key = tab (char(9)) & "hello" (in a field)hello"
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
> [+].	Press.key = char(9)
> [+].		Press.key = == hello
> ```
> 
> 
> 
> 

### Press.command_key




> ---
> 
> #### Test Case #1 "Press CMD-A (in a field)"
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
> [+].Go to Field = == fmIDE_Test::_gTest2
> [+].Press.command_key = "A"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Press CMD-SHIFT-N (in a field)"
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
> [+].Go to Field = == fmIDE_Test::_gTest
> [+].Press
> [:]..command_key = "N"
> [:]..shift = true
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Press CMD-A, BS = clear all (in a field)"
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
> [+].Press.key = Char(8) /* BS */
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Press CMD-A (in a script)"
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
> [+].	Press.command_key = "A"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Press CMD-A (in two scripts)"
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
> [+].Press.command_key = "A"
> [+].Press.command_key = "A"
> ```
> 
> 
> 
> 


