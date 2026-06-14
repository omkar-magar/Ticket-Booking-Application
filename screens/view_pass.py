from kivymd.uix.screen import MDScreen
from kivy.app import App


class ViewPassScreen(MDScreen):
    def go_back(self):
        app = App.get_running_app()
        app.root.transition.direction = "right"
        app.root.current = "dashboard"
