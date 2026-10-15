<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Clipboard Objects`

Place supported FileMaker object data on the clipboard.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.26 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Set Clipboard Objects
```

## Usage

### Set Clipboard Objects




> ---
> 
> #### Test Case #1 "Set Clipboard Objects"
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
> [+].Set Clipboard Objects = =====
> <fmxmlsnippet type="FMObjectList"><Step enable="True" id="89" name="# (comment)"><DisableStepCollapsed state="False"></DisableStepCollapsed><Restore state="False"></Restore><Text>Success</Text></Step></fmxmlsnippet>
> =====
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Clipboard Objects"
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
> [+].Set Clipboard Objects = =====
> <?xml version="1.0" encoding="UTF-8"?>
> <fmxmlsnippet type="LayoutObjectList">
> <Layout enclosingRectTop ="19.0000000" enclosingRectLeft ="250.0000000" enclosingRectBottom ="105.0000000" enclosingRectRight ="482.0000000">
> <Object type="Text" key="749" LabelKey="0" flags="0" rotation="0">
> <Bounds top="19.0000000" left="250.0000000" bottom="105.0000000" right="482.0000000"/>
> <TextObj flags="2">
> <ExtendedAttributes fontHeight="10" graphicFormat="0">
> <NumFormat flags="0" charStyle="0" negativeStyle="0" currencySymbol="" thousandsSep="0" decimalPoint="0" negativeColor="#0" decimalDigits="0" trueString="" falseString=""/>
> <DateFormat format="0" charStyle="0" monthStyle="0" dayStyle="0" separator="0">
> <DateElement>0</DateElement>
> <DateElement>0</DateElement>
> <DateElement>0</DateElement>
> <DateElement>0</DateElement>
> <DateElementSep index="0"></DateElementSep>
> <DateElementSep index="1"></DateElementSep>
> <DateElementSep index="2"></DateElementSep>
> <DateElementSep index="3"></DateElementSep>
> <DateElementSep index="4"></DateElementSep>
> </DateFormat>
> <TimeFormat flags="0" charStyle="0" hourStyle="0" minsecStyle="0" separator="0" amString="" pmString="" ampmString=""/>
> <CharacterStyle mask="32695">
> <Font-family codeSet="Other" fontId="8" postScript="ArialRoundedMTBold">Arial Rounded MT Bold</Font-family>
> <Font-size>72</Font-size>
> <Face>0</Face>
> <Color>#008800</Color>
> </CharacterStyle>
> </ExtendedAttributes>
> <Styles>
> <LocalCSS>
> self:normal .self&#10;{&#10;&#09;font-family: -fm-font-family(Arial Rounded MT Bold,ArialRoundedMTBold);&#10;&#09;font-size: 72pt;&#10;&#09;color: rgba(0%,53.3333%,0%,1);&#10;}&#10;</LocalCSS>
> <FullCSS>
> self:normal .self&#10;{&#10;&#09;background-image: none;&#10;&#09;background-position: 0% 0%;&#10;&#09;background-size: auto;&#10;&#09;background-repeat: repeat repeat;&#10;&#09;background-origin: padding-box;&#10;&#09;background-clip: border-box;&#10;&#09;background-color: rgba(0%,0%,0%,0);&#10;&#09;border-top-color: rgba(0%,0%,0%,0);&#10;&#09;border-right-color: rgba(0%,0%,0%,0);&#10;&#09;border-bottom-color: rgba(0%,0%,0%,0);&#10;&#09;border-left-color: rgba(0%,0%,0%,0);&#10;&#09;border-top-style: none;&#10;&#09;border-right-style: none;&#10;&#09;border-bottom-style: none;&#10;&#09;border-left-style: none;&#10;&#09;border-top-width: 0pt;&#10;&#09;border-right-width: 0pt;&#10;&#09;border-bottom-width: 0pt;&#10;&#09;border-left-width: 0pt;&#10;&#09;border-top-right-radius: 0pt 0pt;&#10;&#09;border-bottom-right-radius: 0pt 0pt;&#10;&#09;border-bottom-left-radius: 0pt 0pt;&#10;&#09;border-top-left-radius: 0pt 0pt;&#10;&#09;border-image-source: none;&#10;&#09;border-image-slice: 100% 100% 100% 100% fill;&#10;&#09;border-image-width: 1 1 1 1;&#10;&#09;border-image-outset: 0 0 0 0;&#10;&#09;border-image-repeat: stretch stretch;&#10;&#09;outline-width: 0pt;&#10;&#09;outline-style: none;&#10;&#09;outline-color: invert;&#10;&#09;outline-offset: 0pt;&#10;&#09;font-family: -fm-font-family(Arial Rounded MT Bold,ArialRoundedMTBold);&#10;&#09;font-weight: normal;&#10;&#09;font-stretch: normal;&#10;&#09;font-style: normal;&#10;&#09;font-variant: normal;&#10;&#09;font-size: 72pt;&#10;&#09;color: rgba(0%,53.3333%,0%,1);&#10;&#09;direction: ltr;&#10;&#09;line-height: 1line;&#10;&#09;block-progression: tb;&#10;&#09;text-align: left;&#10;&#09;text-transform: none;&#10;&#09;text-indent: 0pt;&#10;&#09;box-shadow: none;&#10;&#09;box-sizing: content-box;&#10;&#09;vertical-align: baseline;&#10;&#09;-fm-digit-set: roman;&#10;&#09;-fm-space-before: 0line;&#10;&#09;-fm-space-after: 0line;&#10;&#09;-fm-tab-stops: ;&#10;&#09;-fm-strikethrough: false;&#10;&#09;-fm-underline: none;&#10;&#09;-fm-glyph-variant: ;&#10;&#09;-fm-paragraph-margin-left: 0pt;&#10;&#09;-fm-paragraph-margin-right: 0pt;&#10;&#09;-fm-character-direction: ;&#10;&#09;-fm-use-default-appearance: false;&#10;&#09;-fm-override-with-classic: false;&#10;&#09;-fm-baseline-shift: 0pt;&#10;&#09;-fm-fill-effect: 0;&#10;&#09;-fm-highlight-color: rgba(0%,0%,0%,0);&#10;&#09;-fm-text-vertical-align: top;&#10;&#09;-fm-tategaki: false;&#10;&#09;-fm-rotation: 0;&#10;&#09;-fm-borders-between-reps: false;&#10;&#09;-fm-borders-baseline: false;&#10;&#09;-fm-texty-field: false;&#10;&#09;-fm-box-shadow-persist: none;&#10;}&#10;self:normal .inner_border&#10;{&#10;&#09;border-top-color: rgba(0%,0%,0%,0);&#10;&#09;border-right-color: rgba(0%,0%,0%,0);&#10;&#09;border-bottom-color: rgba(0%,0%,0%,0);&#10;&#09;border-left-color: rgba(0%,0%,0%,0);&#10;&#09;border-top-style: none;&#10;&#09;border-right-style: none;&#10;&#09;border-bottom-style: none;&#10;&#09;border-left-style: none;&#10;&#09;border-top-width: 0pt;&#10;&#09;border-right-width: 0pt;&#10;&#09;border-bottom-width: 0pt;&#10;&#09;border-left-width: 0pt;&#10;&#09;border-top-right-radius: 0pt 0pt;&#10;&#09;border-bottom-right-radius: 0pt 0pt;&#10;&#09;border-bottom-left-radius: 0pt 0pt;&#10;&#09;border-top-left-radius: 0pt 0pt;&#10;&#09;padding-top: 0pt;&#10;&#09;padding-right: 0pt;&#10;&#09;padding-bottom: 0pt;&#10;&#09;padding-left: 0pt;&#10;&#09;margin-top: 0pt;&#10;&#09;margin-right: 0pt;&#10;&#09;margin-bottom: 0pt;&#10;&#09;margin-left: 0pt;&#10;&#09;width: auto;&#10;&#09;height: auto;&#10;&#09;top: auto;&#10;&#09;right: auto;&#10;&#09;bottom: auto;&#10;&#09;left: auto;&#10;&#09;position: static;&#10;&#09;box-shadow: none;&#10;&#09;box-sizing: content-box;&#10;}&#10;self:normal .text&#10;{&#10;&#09;padding-top: 0pt;&#10;&#09;padding-right: 0pt;&#10;&#09;padding-bottom: 0pt;&#10;&#09;padding-left: 0pt;&#10;&#09;margin-top: 0pt;&#10;&#09;margin-right: 0pt;&#10;&#09;margin-bottom: 0pt;&#10;&#09;margin-left: 0pt;&#10;&#09;height: 100%;&#10;&#09;box-sizing: border-box;&#10;}&#10;self:normal .baseline&#10;{&#10;&#09;border-top-color: rgba(0%,0%,0%,0);&#10;&#09;border-right-color: rgba(0%,0%,0%,0);&#10;&#09;border-bottom-color: rgba(0%,0%,0%,0);&#10;&#09;border-left-color: rgba(0%,0%,0%,0);&#10;&#09;border-top-style: none;&#10;&#09;border-right-style: none;&#10;&#09;border-bottom-style: none;&#10;&#09;border-left-style: none;&#10;&#09;border-top-width: 0pt;&#10;&#09;border-right-width: 0pt;&#10;&#09;border-bottom-width: 0pt;&#10;&#09;border-left-width: 0pt;&#10;}&#10;</FullCSS>
> <ThemeName>com.filemaker.theme.custom.BBDA8CF7_7A20_4144_BF4A_2F88F2F0F686</ThemeName></Styles>
> <CharacterStyleVector>
> <Style>
> <Data>Hello</Data>
> <CharacterStyle mask="32695">
> <Font-family codeSet="Other" fontId="8" postScript="ArialRoundedMTBold">Arial Rounded MT Bold</Font-family>
> <Font-size>72</Font-size>
> <Face>0</Face>
> <Color>#008800</Color>
> </CharacterStyle>
> </Style>
> </CharacterStyleVector>
> <ParagraphStyleVector>
> <Style>
> <Data>Hello</Data>
> <ParagraphStyle mask="0">
> </ParagraphStyle>
> </Style>
> </ParagraphStyleVector>
> </TextObj>
> </Object>
> </Layout></fmxmlsnippet>
> ===
> ```
> 
> 
> ##### Description
> 
> Puts layout objects on ther clipboard
> 
> 
> 


## See also

- [Set Clipboard Text](set-clipboard-text.md)
- [Paste Into Current Layout](paste-into-current-layout.md)
