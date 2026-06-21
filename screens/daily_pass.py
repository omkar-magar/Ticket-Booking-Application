from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from datetime import datetime

# Countdown duration (seconds) the user has to complete the purchase.
PASS_TIMEOUT = 5 * 60  # 05:00


class DailyPassScreen(MDScreen):
    timer_text = StringProperty("05:00")
    date_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._remaining = PASS_TIMEOUT
        self._event = None

    def on_pre_enter(self, *args):
        # Purchase timestamp shown in the green header.
        self.date_text = datetime.now().strftime("%d %b, %Y | %I:%M %p")

        # Reset and (re)start the countdown each time the screen opens.
        self._remaining = PASS_TIMEOUT
        self._update_timer_label()
        if self._event:
            self._event.cancel()
        self._event = Clock.schedule_interval(self._tick, 1)

    def on_leave(self, *args):
        if self._event:
            self._event.cancel()
            self._event = None

    def _tick(self, dt):
        if self._remaining > 0:
            self._remaining -= 1
            self._update_timer_label()
        else:
            if self._event:
                self._event.cancel()
                self._event = None

    def _update_timer_label(self):
        minutes, seconds = divmod(self._remaining, 60)
        self.timer_text = f"{minutes:02d}:{seconds:02d}"

    def limit_pin(self, widget, text):
        # Keep digits only, max 4 characters.
        digits = "".join(c for c in text if c.isdigit())[:4]
        if text != digits:
            widget.text = digits

    def go_back(self):
        app = App.get_running_app()
        app.root.transition.direction = "right"
        app.root.current = "dashboard"
