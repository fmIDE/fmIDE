<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Save a Copy as XML`

Export a file's design as XML to a calculated path; FileMaker 26 options can be supplied as a calculation or structured json_options object.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Save a Copy as XML](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26003) | Yes | beta | v0.73 |

## Description

Performs the equivalent script step.

Parameters

- file_path
- window_name
- include_details
- standalone_binarydata
- json_options // requires FM26

For the full list of json_options and catalog names see the script step help page above.

In FM26 the options can be passed individually, as above, or together as json_options

- catalogs_included
- include_details
- split_catalogs
- standalone_binarydata

Note that the json_options (as all (*planned*) json based parameters in fmIDEAS) can be passed in two different ways:

- as a calculated JSON object string, or
- as a JSON object (when using fmJAML means by setting the elements directly via the json path)

See the test examples.


## Full Syntax

```
# In FM < 26:

[+].Save a Copy as XML
[:]..file_path = == «calculation»
[:]..window_name = == «calculation» // optional
[:]..include_details = == «boolean-expression» // FM26+ - overridden by json_options
[:]..standalone_binarydata = == «boolean-expression» // FM26+ - overridden by json_options
[:]..json_options = == «calculation» // FM26+

# - Alternatively the json_options can be defined directly:

[:]..json_options
[:]...catalogs_included[+] = "FieldCatalog"
[:]...                   ] = "LayoutCatalog"
[:]...                   ] = "ScriptCatalog"
[:]...include_details = «boolean-expression»
[:]...split_catalogs = «boolean-expression»
[:]...standalone_binarydata = «boolean-expression»
```

## Usage

### Save A Copy As XML single file of current window


Save the XML of the current window to the given file_path

```
[+].Save A Copy As XML = == $FilePath
```


> ---
> 
> #### Test Case #1 "Save a Copy as XML current window (short form)"
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
> [+].Save A Copy As XML = == $FilePath
> ```
> 
> 
> ##### Description
> 
> Save a Copy as XML overwrites the file, but for test purposes we are deleting it beforehand.
> 
> 
> 

### Save A Copy As XML single file of named window


Save the XML of the named window to the given file_path

```
[+].Save A Copy As XML
[:]..window_name = == «calculation»
[:]..file_path = == $FilePath
```


> ---
> 
> #### Test Case #1 "Save a Copy as XML named window  (short form)"
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
> [+].Save A Copy As XML
> [:]..window_name = == $WindowName
> [:]..file_path= == $FilePath
> ```
> 
> 
> ##### Description
> 
> The file is overwritten
> 
> 
> 

### Save A Copy As XML with calculated json_options


Save the XML of the named window to the given file_path using the json_options.

Requires at least FileMaker 26

```
[+].Save A Copy As XML
[:]..window_name = == $WindowName
[:]..file_path = == $FilePath
[:]..json_options = == $JsonOptions
```


### Save A Copy As XML with structured json_options


Save the XML of the named window to the given file_path using the json_options that are defined directly in the fmJAML


```
[+].Save a Copy as XML
[:]..file_path = == $folder_path
[:]..window_name = == Get ( WindowName )
[:]..json_options
[:]...catalogs_included[+] = "FieldCatalog"
[:]...                   ] = "LayoutCatalog"
[:]...                   ] = "ScriptCatalog"
[:]...include_details = false
[:]...split_catalogs = true
[:]...standalone_binarydata = false
```


> ---
> 
> #### Test Case #1 "Save a Copy as"
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
> [+].Save A Copy as
> [:]..file_path = == $FilePath
> [:]..create_folders = true
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Save a Copy as XML (static json) all catalogs and split"
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
> [+].Save A Copy As XML
> [:]..file_path = == $FilePath
> [:]..json_options
> [:]...split_catalogs = true
> [:]...catalogs_included[+] = "PersistentStoreCatalog"
> [:]...                   ] = "BaseDirectoryCatalog"
> [:]...                   ] = "FileAccessCatalog"
> [:]...                   ] = "ExternalDataSourceCatalog"
> [:]...                   ] = "BaseTableCatalog"
> [:]...                   ] = "TableOccurrenceCatalog"
> [:]...                   ] = "CustomFunctionsCatalog"
> [:]...                   ] = "ValueListCatalog"
> [:]...                   ] = "FieldCatalog"
> [:]...                   ] = "RelationshipCatalog"
> [:]...                   ] = "CustomMenuCatalog"
> [:]...                   ] = "CustomMenuSetCatalog"
> [:]...                   ] = "ScriptCatalog"
> [:]...                   ] = "ThemeCatalog"
> [:]...                   ] = "LayoutCatalog"
> [:]...                   ] = "LibraryCatalog"
> [:]...                   ] = "PrivilegeSetsCatalog"
> [:]...                   ] = "ExtendedPrivilegesCatalog"
> [:]...                   ] = "AccountsCatalog"
> [:]...                   ] = "Metadata"
> ```
> 
> 
> ##### Description
> 
> This test illustrates how to set the json_options directly and individually from the fmJAML code.
> 
> Note the use of the ellipsis to add further entries to the ``catalogs_included` array in a clean and quiet way.
> 
> 
> 


## See also

- [Save as XML (Alias)](save-as-xml.md)
