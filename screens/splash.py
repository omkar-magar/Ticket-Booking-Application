from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.clock import Clock


class SplashScreen(MDScreen):
    # Seconds the branded splash stays before sliding into the dashboard.
    SPLASH_DURATION = 2.5

    def on_enter(self, *args):
        # Auto-advance to the dashboard after a short, branded pause.
        Clock.schedule_once(self._go_to_dashboard, self.SPLASH_DURATION)

    def _go_to_dashboard(self, *args):
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = "dashboard"
