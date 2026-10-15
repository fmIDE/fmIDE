<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Refresh Window`

Redraw the current window, optionally flushing cached join results and external data.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Refresh Window](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26080) | Yes | beta |  |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Refresh Window
[:]..flush_cached_external_data = == «boolean_expression»
[:]..flush_cached_join_results = == «boolean_expression»
[:]..flush = == «boolean_expression» // convenience parameter to flush both

```

## Usage

### Refresh Window




> ---
> 
> #### Test Case #1 "Refresh Window (short form)"
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
> [+].Refresh Window
> ```
> 
> 
> ##### Description
> 
> This test uses the $$ variable $$fmide_test_file_refresh_counter to test if the layout has been refreshed.
> Between Freeze Window and Refresh Window the refresh counter should not change, but after the Refresh Window it should be increased
> 
> 
> 
> ---
> 
> #### Test Case #2 "Refresh Window = flush_cached_join_results and flush_cached_external_data (long form)"
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
> [+].Refresh Window
> [:]..flush_cached_join_results = 1
> [:]..flush_cached_external_data = 1
> ```
> 
> 
> ##### Description
> 
> This test uses the global variable $$fmide_test_file_refresh_counter to test if the layout has been refreshed.
> Between Freeze Window and Refresh Window the refresh counter should not change, but after the Refresh Window it should be increased
> 
> 
> 

### Refresh Window flush (convenience parameter)




> ---
> 
> #### Test Case #1 "Refresh Window = flush (short convenience form)"
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
> [+].Refresh Window
> [:]..flush = 1
> ```
> 
> 
> ##### Description
> 
> This test uses the global variable $$fmide_test_file_refresh_counter to test if the layout has been refreshed.
> Between Freeze Window and Refresh Window the refresh counter should not change, but after the Refresh Window it should be increased
> 
> 
> 


