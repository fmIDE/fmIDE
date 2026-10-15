<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Perform Find`

Perform the current find requests or construct requests from a structured query.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Perform Find](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26028) | Yes | beta | v0.35.1 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Perform Find
[:]..query
[:]...request[+]
[:]...       [:].omit = false
[:]...         ].criteria[+]
[:]..          ]         [:].field_name = "Suite"
[:]..          ]           ].value      = "3 fmIDEAS"
[:]..          ]           ].operator   = "=="
[:]...         ].criteria[+]
[:]..          ]         [:].field_name = "TargetAction"
[:]..          ]           ].value      = "Perform Find"
[:]..          ]           ].operator   = "=="
[:]..          ].found_set = "Find"

```

## Usage

### Perform Find specify


Something like this…

#@test
[+].Perform Find
[:]..query
[:]...request[+]
[:]...       [:].omit = false
[:]...         ].criteria[+]
[:]..          ]         [:].field_name = "Suite"
[:]..          ]           ].value      = "3 fmIDEAS"
[:]..          ]           ].operator   = "=="
[:]...         ].criteria[+]
[:]..          ]         [:].field_name = "TargetAction"
[:]..          ]           ].value      = "Perform Find"
#[:]..          ]           ].operator   = "=="
[:]..          ].found_set = "Find"
#@endtest
[+].Pause



