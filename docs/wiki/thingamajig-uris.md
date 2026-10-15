> Migrated from the existing fmIDE wiki. This page preserves background and historical examples; version-sensitive integration details have not all been re-tested. Use the current [action reference](../actions/README.md), [parameter reference](../parameters/README.md) and [setup guide](../installation.md) for active work.

First up some definitions:

## Thingamajig

[Wiktionary](https://en.wiktionary.org/wiki/thingamajig):

> *Noun* 
> **thingamajig** (plural [thingamajigs](https://en.wiktionary.org/wiki/thingamajigs#English))
>
> 1. ([informal](https://en.wiktionary.org/wiki/Appendix:Glossary#informal)) Something that one does not know the name of.
>
>    - *He used this, this... this **thingamajig** you saw him with the other day to fix the problem.*


In other words it's a [whatchamacallit](https://en.wiktionary.org/wiki/whatchamacallit), [Dingsbums](https://de.wiktionary.org/wiki/Dingsbums), [aggeggio](https://de.wiktionary.org/wiki/aggeggio), [bidule](https://fr.wiktionary.org/wiki/bidule), [chisme](https://es.wiktionary.org/wiki/chisme) or the like.

## URI = Uniform Resource Identifier

[Wiktionary](https://en.wiktionary.org/wiki/uniform_resource_identifier):

> *Noun*
> [uniform](https://en.wiktionary.org/wiki/uniform#English) [resource](https://en.wiktionary.org/wiki/resource#English) [identifier](https://en.wiktionary.org/wiki/identifier#English) (plural [uniform resource identifiers](https://en.wiktionary.org/wiki/uniform_resource_identifiers#English))
>
> 1. ([Internet](https://en.wiktionary.org/wiki/Internet)) A [string](https://en.wiktionary.org/wiki/string) of [characters](https://en.wiktionary.org/wiki/character) that identifies a [resource](https://en.wiktionary.org/wiki/resource) that can be [accessed](https://en.wiktionary.org/wiki/access) over the [Internet](https://en.wiktionary.org/wiki/Internet).

In other words it's a pointer to a thing.

## fmIDE Thingamajig URIs

fmIDE Thingamajig URIs are ✨ magical ✨ pointers to things in FileMaker databases.

Really!

Let's look at some:

This **thingamajig URI** references the `Hello` script in the `fmGuruDemo.fmp12` database:

    fmGuruDemo&$script_name=Hello

and this thingamajig points to the 5th script step of the same script

    fmGuruDemo&$script_name=Hello&$script_step_number=5

This one also specifies exactly where the file is to be found:

    192.172.1.1/fmGuruDemo&$script_name=Hello&$script_step_number=5

And with an fmp url  to use Filemaker 19 (which can also have its uses!)

    fmp19/192.172.1.1/fmGuruDemo&$script_name=Hello&$script_step_number=5



**fmIDE Thingamajig URIs**  are a short form of [fmIDE 'Name that thing' API fmp url][], and are easily transformed into a magical fmp url link - with a little help from [the magical *fmIDE URIcorn* 🦄](#the-magical-fmide-thingamajig-uricorn-)

## So what are fmIDE Thingamajig URIs exactly?

**fmIDE Thingamajig URIs** are a short form of [fmIDE 'Name that thing' API fmp urls][fmIDE 'Name that thing' API fmp urls].




    [[fmp/][server]/]file(&$var=value)*

At their shortest they are just a file name(*):

    fmGuruDemo

(*) Note: No fmp12 extension required!

This can be followed by any ([fmIDE 'Name that thing' API][fmIDE 'Name that thing' API fmp url]) variables to name the thing you want:


    fmGuruDemo&$custom_function_name=_Recalculate

You can even identify (*some*) things by number or id (or, one day, by uuid)


    fmGuruDemo&$base_table_name=Examples&field_id=12

Optionally you can specify the server address:

    192.172.1.1/fmGuruDemo&$script_name=Hello

…and the target FileMaker fmp protocol to use

    fmp19/192.172.1.1/fmGuruDemo&$script_name=Hello

Or just the fmp protocol:

    fmp19//fmGuruDemo&$script_name=Hello

Note:
- If no server address is specified, then the file must already be open! 
  - *unless*, of course, the magical URIcorn 🦄 knows where your server is…
- Note that values must be correctly url-encoded (space as %20, percent as %25, [etc.](https://de.m.wikipedia.org/wiki/URL-Encoding#Relevante_ASCII-Zeichen_in_Prozentdarstellung)), thus to reference a `Hello World` script you would need:
```
    fmGuruDemo&$script_name=Hello%20World
```

## The magical fmIDE thingamajig URIcorn 🦄

![The magical URIcorn](images/fmide-magical-uricorn-avatar-256.png)

The fmIDE URIcorn 🦄 is the magical beast that, when presented with an [fmIDE thingamajig URI](#fmide-thingamajig-uris), takes you there in the blink of an eye! 🪄

| The fmiDE URIcorn turns thingamajig URIs into fmIDE fmp urls |
|:-:|
| `fmGuruDemo&$script_name=Hello`|
|↓
|[🦄]
|↓
| **fmp19://192.172.1.1/** fmGuruDemo **?script=fmIDE** &$script_name=Hello |↓
|↓
| `fmp19://192.172.1.1/fmGuruDemo?script=fmIDE&$script_name=Hello` |






As a button she looks like this [🦄] or maybe like this [🦄 → ![fmIDE Logo](images/fmide-integrate-emoji.png)] and her magic works like this:

She first consumes a **thingamajig URI** like this one:

    fmGuruDemo&$script_name=Hello

and applies to it what default knowledge she has of your environment:

    fmp19/192.172.1.1/fmGuruDemo&$script_name=Hello

[If she knows nothing about you, she'll assume `fmp/$/`]

This she pads out to a full blown [fmIDE 'Name that thing' API fmp url][]:

    fmp19/192.172.1.1/fmGuruDemo&$script_name=Hello

fmp19 **://** 192.172.1.1/fmGuruDemo **?script=fmIDE** &$script_name=Hello

    fmp19://192.172.1.1/fmGuruDemo?script=fmIDE&$script_name=Hello

…and, with a swish of her magic URIhorn 🦄, she calls fmIDE and 'names that thing', and lets the magic of fmIDE unfold…

✨

…voilà, you are transported exactly to that place! (She really is magic!)

## fmIDE thingamajig action URIs

Of course, since the [fmIDE 'Name that thing' API][] also supports [fmIDE actions][fmIDE Actions], the magic URIhorn can do more that just take you there!

✨ [watch this space] ✨



---
[fmIDE 'Name that thing' API fmp urls]: ../name-that-thing.md#fmp-urls
[fmIDE 'Name that thing' API fmp url]: ../name-that-thing.md#fmp-urls
[fmIDE 'Name that thing' API]: ../name-that-thing.md
[fmIDE Actions]: ../actions/README.md
