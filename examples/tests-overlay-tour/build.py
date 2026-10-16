#!/usr/bin/env python3
"""Embed the editable HTML in a standalone fmJAML action script."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
html = (HERE / 'tour.html').read_text()
assert '===FMIDE_TOUR_HTML' not in html

source = '''# fmIDE Tests: an external MBS overlay tour.
# No installed scripts, custom functions, macros, fields or records are changed.
# Requires MBS 16.2+, desktop FileMaker, Tests layout at 100% zoom.
[+].Set Error Capture = 1
[+].If = == not IsEmpty ( $expected_file_path ) and Right ( Get ( FilePath ) ; Length ( $expected_file_path ) ) ≠ $expected_file_path
[+].  Exit Script = == JSONSetElement ( "{}" ; [ "ok" ; False ; JSONBoolean ] ; [ "error" ; "Unexpected database path" ; JSONString ] )
[+].End If
[+].If = == not IsEmpty ( $$fmidetour_overlay ) or not IsEmpty ( $$fmidetour_highlight )
[+].  Exit Script = == JSONSetElement ( "{}" ; [ "ok" ; False ; JSONBoolean ] ; [ "error" ; "A tour already exists. Use X or stop-tour first." ; JSONString ] )
[+].End If
[+].Set.$tour_mbs_version = == MBS ( "Version" )
[+].If = == GetAsNumber ( GetValue ( Substitute ( $tour_mbs_version ; "." ; "¶" ) ; 1 ) ) < 16 or ( GetAsNumber ( GetValue ( Substitute ( $tour_mbs_version ; "." ; "¶" ) ; 1 ) ) = 16 and GetAsNumber ( GetValue ( Substitute ( $tour_mbs_version ; "." ; "¶" ) ; 2 ) ) < 2 )
[+].  Exit Script = == JSONSetElement ( "{}" ; [ "ok" ; False ; JSONBoolean ] ; [ "error" ; "MBS 16.2 or later is required." ; JSONString ] )
[+].End If
[+].Go to Layout = "fmIDE Tests"
[+].If = == $$fmide_get_last_error or Get ( LayoutName ) ≠ "fmIDE Tests" or Get ( WindowZoomLevel ) ≠ 100 or Get ( WindowContentWidth ) < 1102
[+].  Exit Script = == JSONSetElement ( "{}" ; [ "ok" ; False ; JSONBoolean ] ; [ "error" ; "Open fmIDE Tests at 100% zoom in a window at least 1102 points wide." ; JSONString ] )
[+].End If

# HTML is literal here-text: do not hand-escape its quotes.
[+].Set.$tour_html = =====FMIDE_TOUR_HTML
''' + html + '''
===FMIDE_TOUR_HTML

# Create only session objects. Each MBS result is retained for inspection.
[+].Set.$$fmidetour_overlay = == MBS ( "Overlay.Create" )
[+].Set.$$fmidetour_highlight = == MBS ( "Overlay.Create" )
[+].Set.$tour_setup = ===
Let(
[

vFrame = MBS ( "Overlay.SetFrame" ; $$fmidetour_overlay ; 100 ; 100 ; 400 ; 246 ) ;
vTitle = MBS ( "Overlay.SetTitle" ; $$fmidetour_overlay ; "fmIDE Tests tour" ) ;
vFront = MBS ( "Overlay.SetTopMost" ; $$fmidetour_overlay ; 1 ) ;
vHighlightFrame = MBS ( "Overlay.SetFrame" ; $$fmidetour_highlight ; 100 ; 100 ; 200 ; 36 ) ;
vHighlightTitle = MBS ( "Overlay.SetTitle" ; $$fmidetour_highlight ; "fmIDE tour highlight" ) ;
vHighlightFront = MBS ( "Overlay.SetTopMost" ; $$fmidetour_highlight ; 1 ) ;
vPassClicks = MBS ( "Overlay.SetIgnoresMouseEvents" ; $$fmidetour_highlight ; 1 ) ;
vShadow = MBS ( "Overlay.SetHasShadow" ; $$fmidetour_highlight ; 0 ) ;
vHighlightWeb = MBS ( "Overlay.AddWebViewer" ; $$fmidetour_highlight ; 0 ) ;
vHighlightHTML = MBS ( "WebView.LoadHTML" ; vHighlightWeb ; "<html><style>html,body{margin:0;background:transparent;width:100%;height:100%;overflow:hidden}div{box-sizing:border-box;width:100%;height:100%;border:3px solid #008800;border-radius:7px;background:transparent}</style><body><div></div></body></html>" ) ;
$$fmidetour_web = MBS ( "Overlay.AddWebViewer" ; $$fmidetour_overlay ; 2 )

];

List ( vFrame ; vTitle ; vFront ; vHighlightFrame ; vHighlightTitle ; vHighlightFront ; vPassClicks ; vShadow ; vHighlightHTML )

)
===
[+].Set.$tour_config = ===
JSONSetElement ( "{}"
; [ "file_path" ; Get ( FilePath ) ; JSONString ]
; [ "window_name" ; Get ( WindowName ) ; JSONString ]
; [ "window_ref" ; MBS ( "Window.FindByTitle" ; Get ( WindowName ) ) ; JSONNumber ]
; [ "overlay" ; $$fmidetour_overlay ; JSONNumber ]
; [ "highlight" ; $$fmidetour_highlight ; JSONNumber ]
)
===
[+].Set.$tour_load = == MBS ( "WebView.LoadHTML" ; $$fmidetour_web ; Substitute ( $tour_html ; "__TOUR_CONFIG__" ; $tour_config ) )
[+].If = == $tour_load ≠ "OK" or Substitute ( $tour_setup ; [ "OK" ; "" ] ; [ "¶" ; "" ] ) ≠ ""
[+].  Set.$tour_cleanup = ===
Let(
[
vHighlight = MBS ( "Overlay.Release" ; $$fmidetour_highlight ) ;
vBubble = MBS ( "Overlay.Release" ; $$fmidetour_overlay ) ;
$$fmidetour_overlay = "" ;
$$fmidetour_highlight = "" ;
$$fmidetour_web = ""
];
List ( vHighlight ; vBubble )
)
===
[+].  Exit Script = == JSONSetElement ( "{}" ; [ "ok" ; False ; JSONBoolean ] ; [ "setup" ; $tour_setup ; JSONString ] ; [ "load" ; $tour_load ; JSONString ] ; [ "cleanup" ; $tour_cleanup ; JSONString ] )
[+].End If
[+].Exit Script = ===
JSONSetElement ( "{}"
; [ "ok" ; $tour_load = "OK" and Substitute ( $tour_setup ; [ "OK" ; "" ] ; [ "¶" ; "" ] ) = "" ; JSONBoolean ]
; [ "stage" ; "HTML loaded; verify the visible tour separately" ; JSONString ]
; [ "setup" ; $tour_setup ; JSONString ]
; [ "load" ; $tour_load ; JSONString ]
; [ "config" ; $tour_config ; JSONObject ]
; [ "web" ; $$fmidetour_web ; JSONString ]
; [ "mbs_version" ; $tour_mbs_version ; JSONString ]
)
===
'''
(HERE / 'tests-tour.fmIDEAS.fmJAML').write_text(source)
print('Built tests-tour.fmIDEAS.fmJAML:', len(source.encode()), 'bytes')
