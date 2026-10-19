fmIDE Tests overlay tour — prototype

A standalone fmIDEAS that creates a rounded HTML speech bubble and a separate
transparent highlight around the button being explained. No scripts, macros,
custom functions, layouts or records need to be installed or edited.

RUN

Open a disposable copy of the fmIDE demo file in FileMaker 26. Use 100% zoom
and a content area at least 1102 points wide. MBS 16.2 or later is required.

From this folder, replacing fmIDE-Overlay-Tour with the open copy's database name:

  fmide -fmp 26 -file fmIDE-Overlay-Tour --parameter-file tests-tour.fmIDEAS

The tour opens the fmIDE Tests layout. Use < for Back, X to stop, and > for
Next (Finish on the last stop). The tour explains controls; it does not run tests.
It follows the FileMaker window and animates between six header buttons.

Fallback stop command, targeting the same database:

  fmide -fmp 26 -file fmIDE-Overlay-Tour --parameter-file stop-tour.fmIDEAS

CLI exit success confirms dispatch only. Check that the bubble appears.
Both stop methods release this tour's overlays and clear its session variables.

EDIT

The runnable fmIDEAS already contains its HTML; Python is not needed to run it.
To change the tour, edit tour.html and rebuild with:

  python3 build.py

The HTML calls MBS FileMaker.Evaluate directly. Navigation therefore needs no
installed callback script. A named fmJAML here-text delimiter preserves HTML
and JavaScript, including JavaScript's === operator.

VERIFIED

Tested on Russells-iMac.local, macOS, FileMaker Pro 26.0.3, MBS 16.4.0.08.
All six stops, Back, Next, Finish, X and window following passed. Completion
files reported error 0; JavaScript state and native overlay positions were
checked as well as the visible controls. The original repository database's
SHA-256 remained unchanged. See verification.json for the recorded evidence.

The two JPEGs are real screenshots of the speech-bubble window, not composite
screenshots showing its position over FileMaker.

LIMITS

This prototype uses the current Tests layout's button coordinates at 100% zoom.
Window movement and right anchoring are accounted for; changed layout geometry
needs updated coordinates. Named layout objects would be a better later anchor.
Only macOS was tested. The overlays float above other windows until stopped.
Keyboard navigation is included but was not separately tested.

MBS REFERENCE

https://www.mbsplugins.eu/OverlayAddWebViewer.shtml
https://www.mbsplugins.eu/OverlayMove.shtml
https://www.mbsplugins.eu/OverlaySetFrameWithControl.shtml
https://www.mbsplugins.eu/ScheduleEvaluateAfterDelay.shtml
