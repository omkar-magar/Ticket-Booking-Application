from kivymd.uix.screen import MDScreen
from kivy.app import App

class DashboardScreen(MDScreen):
    """
    Logic for the main landing screen.
    Handles navigation to functional modules.
    """
    def navigate_to(self, screen_name):
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = screen_name