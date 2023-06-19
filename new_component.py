from reactpy import component, html;
from reactpy.backend.fastapi import configure;


@component
def Item2(text):
  myStyle = {"style":  { "color": "violet", "font-size": "32px"}}

  return html.li(myStyle, text)

export = Item2
