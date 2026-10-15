> Migrated from the existing fmIDE wiki. This page preserves background and historical examples; version-sensitive integration details have not all been re-tested. Use the current [action reference](../actions/README.md), [parameter reference](../parameters/README.md) and [setup guide](../installation.md) for active work.

The `fmIDE-Go to Thing` Script is the gateway from your favourite FileMaker analysis tool directly into your FileMaker development environment. Just run the script - or press the shortcut key - to jump from the current record in the tool to that thing in your database in FileMaker.

See the following projects for current versions of the `fmIDE-Go to Thing` Script.

-  [`fmIDE-Go to Thing` Script from BaseElements](https://github.com/fmIDE/Script-fmIDE-Go-to-Thing-from-BaseElements)
-  [`fmIDE-Go to Thing` Script from CrossCheck](https://github.com/fmIDE/Script-fmIDE-Go-to-Thing-from-CrossCheck)


# How does the script work?

The script simply defines variables, like $script_name, $account_name, of the thing which is currently in focus, and then builds and opens an appropriate fmp(/claris) url to pass the info to fmIDE.

It has five parts (Note: Example code is based on the CrossCheck Script)

1. Parameters

   - `fmide_debug` (boolean)
     - If true fmIDE pauses to let you start the debugger..
   - `get_fmide_url` (boolean)
     - If true does not open the url, just returns the url.
   - `protocol` (string)
     - Which FileMaker url-protocol to use
   - `server_address` (string)
     - The address of the server, where the files are to be found.


2. Where are we?

   - What's in focus?

      ```perl
      Set Variable [ $CurrentLayoutTableName ; Get( LayoutTableName ) ]
      Set Variable [ $ActiveFieldTableName ; Get( ActiveFieldTableName ) ]
      Set Variable [ $ActiveFieldName ; Get( ActiveFieldName ) ]
     ```
   - What's really in focus?

      - It may be necessary to do a little dance and adjust the ActiveTableName in some situations (to make the logic in the next section easier)
      - For example, maybe the user has clicked in a portal showing script steps that reference the current thing. However, if they have clicked in the ScriptName field of that portal, the ActiveFieldTableName may be to the related Script table rather than to the related Script Step table.

3. What thing do we want to see, based on that focus?

    - This section is a (large) switch statement that decides which variables to  define based on the focus.
    
        ```perl
        # Based on focus set variables accordingly
        If [ 0 ]
            # :

        Else If [ $CurrentLayoutTableName = "tTables" ]
            # Tables are in focus

            If [ 0 ]
                # :
            Else If [ $CurrentActiveTableName = "tTables.tScript" ]
                # Focus is on a script using the table
                Set Variable [ $file_name ; tTables.tScript::FileName ]
                Set Variable [ $script_name ; tTables.tScript::ScptName ]

            Else If  [ … ]
                # :

            Else
                # Focus is on the table
                Set Variable [ $file_name ; tTables::FileName ]
                Set Variable [ $table_name ; tTables::TblName ]

            End If
                # :
        Else If [ … ]
            # :
        End If
        ```

4. The fmIDE 'Name that Thing' API bit

    - Construct an fmp url from the variables
    - Open the URL

5. Script return parameter

The script always returns the fmide_url.
