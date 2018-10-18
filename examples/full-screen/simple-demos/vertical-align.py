#!/usr/bin/env python
"""
Vertical align demo with VSplit.
"""
from __future__ import unicode_literals

from prompt_toolkit.application import Application
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, VSplit, Window, VerticalAlign
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.widgets import Frame

TITLE = HTML(""" <u>VSplit VerticalAlign</u> example.
 Press <b>'q'</b> to quit.""")

LIPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Maecenas
quis interdum enim. Nam viverra, mauris et blandit malesuada, ante est bibendum
mauris, ac dignissim dui tellus quis ligula. Aenean condimentum leo at
dignissim placerat."""

# 1. The layout
body = HSplit([
    Frame(
        Window(FormattedTextControl(TITLE), height=2), style='bg:#88ff88 #000000'),
    VSplit([
        Window(FormattedTextControl(HTML('  <u>VerticalAlign.TOP</u>')), height=4, ignore_content_width=True, style='bg:#ff3333 #000000 bold'),
        Window(FormattedTextControl(HTML('  <u>VerticalAlign.CENTER</u>')), height=4, ignore_content_width=True, style='bg:#ff3333 #000000 bold'),
        Window(FormattedTextControl(HTML('  <u>VerticalAlign.BOTTOM</u>')), height=4, ignore_content_width=True, style='bg:#ff3333 #000000 bold'),
        Window(FormattedTextControl(HTML('  <u>VerticalAlign.JUSTIFY</u>')), height=4, ignore_content_width=True, style='bg:#ff3333 #000000 bold'),
    ], height=1, padding=1, padding_style='bg:#ff3333'),
    VSplit([
        # Top alignment.
        HSplit([
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
        ], padding=1, padding_style='bg:#888888', align=VerticalAlign.TOP),
        # Center alignment.
        HSplit([
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
        ], padding=1, padding_style='bg:#888888', align=VerticalAlign.CENTER),
        # Bottom alignment.
        HSplit([
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), height=4, style='bg:#444488'),
        ], padding=1, padding_style='bg:#888888', align=VerticalAlign.BOTTOM),
        # Justify
        HSplit([
            Window(FormattedTextControl(LIPSUM), style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), style='bg:#444488'),
            Window(FormattedTextControl(LIPSUM), style='bg:#444488'),
        ], padding=1, padding_style='bg:#888888', align=VerticalAlign.JUSTIFY),
    ], padding=1, padding_style="bg:#ff3333 #ffffff", padding_char='.')
])


# 2. Key bindings
kb = KeyBindings()


@kb.add('q')
def _(event):
    " Quit application. "
    event.app.exit()


# 3. The `Application`
application = Application(
    layout=Layout(body),
    key_bindings=kb,
    full_screen=True)


def run():
    application.run()


if __name__ == '__main__':
    run()
