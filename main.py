from reactpy import component, html, hooks;
from reactpy.backend.fastapi import configure;
from fastapi import FastAPI;

# pip install "reactpy[fastapi]" // con backend
# pip install "unicorn[standard]"
# *> uvicorn main:app --reload

@component
def Item(text, initial_done = False):
  done, set_done = hooks.use_state(initial_done)
  

  def handle_click(event):
    set_done(not done)

  attrs = {"style": { "color": "green"} } if done else {}

  if done:
    return html.li(attrs, text)
  else:
    return html.li(
      html.span(attrs, text),
      html.button({"on_click": handle_click}, "Done!")
    )
  

@component
def HelloWorld():
  return html._(
    html.h1("Lista de Tareas!"),
    html.ul(
      Item("Tarea 1 con componente"),
      Item("Using React with Python"),
      Item("Tarea 3", initial_done=True),
    )
  )  

app = FastAPI()
configure(app, HelloWorld)
