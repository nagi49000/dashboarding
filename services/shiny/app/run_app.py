from shiny import App
from .app import get_app_ui, server


app = App(get_app_ui(), server)
