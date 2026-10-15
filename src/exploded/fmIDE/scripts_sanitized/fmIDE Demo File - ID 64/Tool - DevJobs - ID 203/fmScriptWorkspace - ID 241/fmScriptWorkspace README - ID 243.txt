# /##
# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
# # fmScriptWorkspace

# @author MrWatson <russell@mrwatson.de>
# @version @see the version / changes script

# fmScriptWorkspace is a FileMaker Module which makes it possible to automate activities in the Script Workspace (Mac ONLY).
# For example: open a named script in the script workspace and select/scroll to a specific line/lines

# This is possible from within FileMaker or - by using an fmpurl - from an external tool, application or website



# Dependencies:
# @requires MBS Plugin Version 7.4 or higher for basic functionality
# @requires MBS Plugin Version 8.6.0.04 or higher for extended functionality
# @requires a paid MBS licence, but can be used under the conditions of the Demo or Trial Version
# @requires script developers (full access users) to have the extended privilege fmurlscript if you want to open scripts via the fmp url.
# @requires at least FileMaker 14 (where the Script Workspace was introduced) to use the basic functionality 
# @requires at least FileMaker 17 if you want to call the module's scripts by name from within FileMaker

# @see https://github.com/fmScriptWorkspace-FileMaker-Module for the latest version of this module
# @see https://modularfilemaker.org for an introduction to the philosophy of filemaker modules 

# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
# # INSTALLATION


# 1. Security: Tweak, if necessary

# fmScriptWorkspace has been designed to be secure. 
# For this reason only users with [Full Access] privileges are allowed to open scripts with fmScriptWorkspace.

# However, if you have...
# - non-full access privilege sets that have been authorized to edit (all or certain) scripts
# - AND you would like them to be able to use fmScriptWorkspace to open scripts automatically
# => please edit the fmScriptWorkspace.HaltScriptIfNoAccess script to remove the security block for them

# 2. Scripts: Copy the fmScriptWorkspace folder into _each_ of your solution files:

#   - Copy the entire @folder "Modules" into each file of your solution
#   - *OR* (if you already have a modules folder in your solution)
#   - Copy the @folder "fmScriptWorkspace" to each solution file

# IFF you wish to open scripts from external tools:

# 3. Security: Grant Full Access users the ability to perform FileMaker scripts via fm URL: In each file

#   - Open the Manage > Security… Dialog
#   - Select the Extended Privileges tab
#   - Double click the "fmurlscript" extended privilege
#   - Grant this privilege to full access users by checking the On box.

# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
# # USE

# To open a script in the **CURRENT** file (from a button or from a script) use @script "fmScriptWorkspace.OpenScript" like this:

# ` Perform Script [ Specified: From List ]
  		[ "fmScriptWorkspace.OpenScript" ]
  		[ Parameter: List( $Script ; $Line ; $LineTo ) ]
  

# Alternatively you can use Perform Script by Name (so that the call does not break if you update/replace the module layout):

# ` Perform Script [ Specified: By name ]
  		[ "fmScriptWorkspace.OpenScript" ]
  		[ Parameter: List( $Script ; $Line ; $LineTo ) ]
  


# To open a script in a **DIFFERENT** (referenced) file use @script "fmScriptWorkspace.OpenScriptInFile":

# ` Perform Script [ Specified: From List ]
  		[ "fmScriptWorkspace.OpenScriptInFile" ]
  		[ Parameter: $FileName & ¶ & List( $Script ; $Line ; $LineTo ) ]
  

# Note:
# - the FileName is the name of the external data source that references the file // best keep the names identical!
# - AND, of course, the other file must also have the fmScriptWorkspace module installed!


# Note: The fmScriptWorkspace.OpenScriptInFile script uses perform by name and the "filename::scriptname" syntax to call the fmScriptWorkspace.OpenScript API script in the remote file:

# ` Perform Script [ Specified: By name ]
  		[ "otherfile::fmScriptWorkspace.OpenScript" ]
  		[ Parameter: "MyScript¶-4" /* fourth line from the end */ ]
  


# Note for FM16 developers: If you have fm16 or less, you can also use MrWatsons PSBN module to fake a Call by Name



# To open a script from an external application, use an fmp-URL, like this:

# ` fmp://$/TargetFile.fmp12?script=fmScriptWorkSpace.OpenScript&param=SYS%20KeyCheck%20fortlaufende%20Nummer%20(ID)%0D-4

# The script name and parameter must be URL-encoded, (spaces as %20 and the return as %0D)

# @see documentation of @script "fmScriptWorkspace.OpenScript"

# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
# # LICENCE
# @license        The MIT License (MIT)
  
  Copyright (c) 2021 Russell Watson
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  
  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.
  
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.

# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
# # WHY USE PERFORM SCRIPT BY NAME?

# IFF you ALWAYS use Perform Script *by Name* to call the public API scripts of this module...

# - you can call the api scripts in ANY file (without knowing the file)
#   - which means you can swap file vesions in + out of your solution without breaking script calls
# - you can update the module by just deleting it + replacing it with the newest version.

# OTHERWISE

# - swapping out single files in multi file systems may break script calls
# - you must update the contents of each script, so as not to break anything

# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
# # ABOUT THIS COMMENTING SYSTEM
# This commenting system…

# - uses FileMakerDoc @tags to tag particularly important information
# - uses some FileMakerMarkdown notation to mark & style lines
# - uses fmSyntaxColorizer to colorize the script steps + comments
# - which, of course, uses the MBS SyntaxColoring Component to achieve this

# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
# # The ULTIMATE GOAL?

# - Create a 'javadoc'-like system for creating external documentation (FileMakerDoc)
# - Create (API) documents, which can dynamically link back to the scripts it documents (1)

# - Increase modularity + sharability of code in FileMaker
# - to help stablise Script Names
# - by helping free up script names of the burden of documenting parameter names
# - to help promote the use of Perform Script by Name
# - to win the battle against tightly coupled code

# - and - one day - to help establish an ultimate - de facto - method of parameter passing!
    (the final stone on the path to salvation)

# ` Substitute( "One Ring to rule them all, One Ring to find them,
               One Ring to bring them all and in the darkness bind them!" ;
              "Ring" ; "de facto standard FileMaker parameter passing technique" ) 

# Something like that

# Oh...and not forgetting:

# - create a script-writing robot "Patch" or "the Last One" or the likes

# Happy FileMaking

# MrWatson

# ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___

# #/

