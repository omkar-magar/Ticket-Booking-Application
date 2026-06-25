from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.clock import Clock


class SplashScreen(MDScreen):
    # Minimum seconds to keep the brand visible so the splash never just flashes
    # by, even when the dashboard builds quickly.
    MIN_SPLASH = 1.2
    # Safety cap so a slow/failed build can never leave the user stuck on the
    # splash forever — advance regardless once this much time has elapsed.
    MAX_SPLASH = 5.0

    def on_enter(self, *args):
        # Instead of a fixed pause, advance as soon as the dashboard is built
        # (it's constructed lazily after this screen renders). Wait at least
        # MIN_SPLASH for the brand, then poll each frame until it's ready.
        self._waited = 0.0
        Clock.schedule_once(self._maybe_advance, self.MIN_SPLASH)

    def _maybe_advance(self, dt):
        self._waited += dt
        app = App.get_running_app()
        # Advance once the dashboard exists, or once the safety cap is hit.
        if app.root.has_screen("dashboard") or self._waited >= self.MAX_SPLASH:
            app.root.transition.direction = "left"
            app.root.current = "dashboard"
            return
        # Not ready yet — check again next frame.
        Clock.schedule_once(self._maybe_advance, 0)
