from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
from datetime import datetime

# Countdown duration (seconds) the user has to complete the booking.
TICKET_TIMEOUT = 5 * 60  # 05:00


class BusTicketScreen(MDScreen):
    timer_text = StringProperty("05:00")
    date_text = StringProperty("")
    full_count = NumericProperty(1)
    half_count = NumericProperty(0)
    mode = StringProperty("fare")  # "fare" or "ending"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._remaining = TICKET_TIMEOUT
        self._event = None

    def on_pre_enter(self, *args):
        # Booking timestamp shown in the green header, e.g. "21 Jun, 2026 | 05:13 PM"
        self.date_text = datetime.now().strftime("%d %b, %Y | %I:%M %p")

        # Reset and (re)start the countdown each time the screen opens.
        self._remaining = TICKET_TIMEOUT
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
            # Time expired: stop the clock (booking session timed out).
            if self._event:
                self._event.cancel()
                self._event = None

    def _update_timer_label(self):
        minutes, seconds = divmod(self._remaining, 60)
        self.timer_text = f"{minutes:02d}:{seconds:02d}"

    # ── Fare / Ending-stop toggle ──────────────────────────────
    def set_mode(self, mode):
        self.mode = mode

    # ── Ticket count steppers ──────────────────────────────────
    def inc_full(self):
        self.full_count += 1

    def dec_full(self):
        if self.full_count > 0:
            self.full_count -= 1

    def inc_half(self):
        self.half_count += 1

    def dec_half(self):
        if self.half_count > 0:
            self.half_count -= 1

    def go_back(self):
        app = App.get_running_app()
        app.root.transition.direction = "right"
        app.root.current = "dashboard"
