<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Delete Record/Request`

Delete the current record or find request, with optional confirmation.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Delete Record/Request](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26009) | Yes | ok | v0.53 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Delete Record/Request
[:]..with_dialog = «boolean-expression»
```

## Usage

### Delete Record/Request




> ---
> 
> #### Test Case #1 "Delete Record/Request (short form) = default with dialog"
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
> [+].	Delete Record/Request
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Delete Record/Request (Short form without dialog)"
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
> [+].	Delete Record/Request = false
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Delete Record/Request (without dialog)"
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
> [+].	Delete Record/Request
> [:].    .with_dialog = false
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Delete Record/Request.with_dialog = false"
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
> [+].Delete Record/Request.with_dialog = false
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Delete Record/Request with_dialog (long form)"
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
> [+].Delete Record/Request
> [:]..with_dialog = true
> ```
> 
> 
> 
> 


## See also

- [Delete All Records](delete-all-records.md)
