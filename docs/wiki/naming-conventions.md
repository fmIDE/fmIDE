> Migrated from the existing fmIDE wiki. This page preserves background and historical examples; version-sensitive integration details have not all been re-tested. Use the current [action reference](../actions/README.md), [parameter reference](../parameters/README.md) and [setup guide](../installation.md) for active work.



# Capitalisation Conventions

Every different project has its own naming and capitalising conventions, and to make things worse they have their own naming conventions *for* their capitalising conventions.

So let's get this straight first!

fmIDE uses the following names to reference capitalisation conventions (and cool emojis to iconise them)

- 🔡 lowercase
- 🔠 UPPERCASE
- 📰 Headline Case
- 🏆 Title Case
- 🐪 lowerCamelCase
- 🐫 UpperCamelCase
- 🐍 lower_snake_case
- 🐲 UPPER_SNAKE_CASE
- 🍡 lower-kebab-case
- 🍢 UPPER-KEBAB-CASE

Note: We *don't* use the terms
- PascalCase
- SCREAMING…

## 🔡 lowercase

no explanation needed (or do I mean noexplanationneeded? 🧐)

## 🔠 UPPERCASE

I SAID, NO EXPLANATION NEEDED!

## 📰 Headline Case

- 'Natural' title case as used in headlines
- Main words start with a capital
- Minor words start with a small letter

fmIDE action names - just like FileMaker script steps - use `Headline Case`

`Go to Layout`

## 🏆 Title Case

Every Word Has A Capital Capital

- Capitalised words separated by a single space
- All words are capitalised
- Title Case is 'proper' in the sense of
    - FileMaker Proper() function
    - 'without exception'


## 🐪 lowerCamelCase

Apart from a lower first letter, `🐪 lowerCamelCase` is identical to as `🐫 UpperCamelCase`

## 🐫 UpperCamelCase

- Title Case words with no spaces
- Acronyms as words (Xml not XML, Id not ID)

## 🐍 lower_snake_case

- Lowercase words separated by underscores

## 🐲 UPPER_SNAKE_CASE

- Uppercase words separated by underscores

## 🍡 lower-kebab-case

- Lowercase words skewered by dashes 

GitHub wiki uses lower-kebab-case for its automatic in-page anchors. 

## 🍢 UPPER-KEBAB-CASE

- Uppercase words skewered by dashes 


# fmIDE's capitalisation philosophy

This section is under construction.

## Public API conventions

### fmIDE

fmIDE = fmIDE

### fmIDE API script names 

- UpperCamelCase
  - Exception: fmIDE = fmIDE
- naked (no parameter info)
- «ModuleName».«ScriptName»
- For example: `fmIDE.GetBaseLayoutName`

### JSON Parameters

JSON Parameters use `🐍 lower_snake_case`
fmp url Variables use `$lower_snake_case`


## Coding conventions

###Let-variables

- Let-variables use `¢lower_snake_case`
  - The ¢ prefix is supported by MBS Plugin

### Code Formatting conventions for fmIDE_Actions_JSON

- Use JSONSetElement [;;]-Syntax
- Use the compact JSON syntax for actions
    - Pass an array of actions
    - Each action is a key, whose name is the acton
    - The action name key is the ONLY key which may be expressed
- Place the semicolon at the START of the line, not at the END.
    - This makes it far easier to add & remove lines without having to fiddle with semicolons
- Make the script more readable
    - Add space between the semicolon and the opening '[' as necessary in order to make the indentation visible
    - Add leading zero(es) to the array index as necessary 
    - Recommended
        - In action-scripts with 9 or less actions, leave out the space and leading 0
        - In action-scripts with 10 or more actions, add a space and a leading 0 to the array index


# fmIDE coding philosophy 

Just some thoughts - very in dev.

- Simplicity
- Coherence
- Make the developers life as easy as possible
    - Use standards and conventions where possible
    - Use code snippets where possible
- Write code that speaks to you
    - Wrong code should look wrong
    - Self-documenting code
    - Call a spade a spade
- Code positively
    - Avoid using double (or triple…or more(*)) negatives
    - (*) Don't skip avoiding using negative terms (🧐)
- Agile
- Keep documentation and code in sync
- Use the right tool for the right job

**Why**

- does fmIDE use lower_snake_case 🐍 for Jason parameter names and FMPURL variable parameter names?

**Because**

- It is the simplest case
  - Has the least rules and no exceptions
- It is least unequivocal
  - What is the name of the parameter to hold the ID of base table? `base_table_id` - no more questions!
  - You only have to decide what is a word (filename or file_name?).
- It will lead to fewer bugs in code
  - Promise!
- lower_snake_case is good when there is no length limit on names
  - Where there *is* a limit on name length (e.g. script names max 100), lower_snake_case my lead to name truncation.
