from reactpy import component, html;
from reactpy.backend.fastapi import configure;
from fastapi import FastAPI;

@component
def Item2(text):
  return html.li(text)

export = Item2
