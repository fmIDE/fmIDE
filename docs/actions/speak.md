<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Speak`

Speak calculated text with the default voice, optionally waiting for speech to finish.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Speak](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26066) | Partial | beta | v0.86 |

## Description

Performs the equivalent script step - in the default voice.

Supported

- message
- wait

Not Supported

- voices

## Full Syntax

```
[+].Speak
[:]..message = == «calculation»
[:]..wait = «boolean-calculation»
```

## Usage

### Speak




> ---
> 
> #### Test Case #1 "Speak (short form)"
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
> [+].Speak = == "Hello Martin"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Speak (long form)"
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
> [+].Speak
> [:]..message = == "Long form"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Speak don't wait (long form)"
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
> [+].Speak
> [:]..message = == "one"
> [:]..wait = false
> [+].Speak
> [:]..message = == "er two"
> [:]..wait = false
> [+].Speak
> [:]..message = == "er er three"
> [:]..wait = false
> 
> ```
> 
> 
> 
> 


