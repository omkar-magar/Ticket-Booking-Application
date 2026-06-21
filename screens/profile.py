from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.properties import StringProperty

APP_VERSION = "App version : 1.0.14 (26)"


class ProfileScreen(MDScreen):
    app_version = StringProperty(APP_VERSION)

    def open_item(self, name):
        app = App.get_running_app()
        if name == "tickets":
            app.root.transition.direction = "left"
            app.root.current = "view_ticket"
        elif name == "passes":
            app.root.transition.direction = "left"
            app.root.current = "view_pass"
        # Complaints / Share app / Rate Us / Validate are placeholders.

    def go_back(self):
        app = App.get_running_app()
        app.root.transition.direction = "right"
        app.root.current = "dashboard"
