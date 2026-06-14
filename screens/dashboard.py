from kivymd.uix.screen import MDScreen
from kivy.app import App


class DashboardScreen(MDScreen):
    """Main landing screen. Handles navigation to all modules."""

    def navigate_to(self, screen_name):
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = screen_name
