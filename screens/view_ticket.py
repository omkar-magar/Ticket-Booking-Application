import os
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.metrics import dp
from datetime import datetime, timedelta

# Logo pulse (zoom in/out) sizes for the ticket page.
LOGO_BASE = 150
LOGO_ZOOM = 174

# Mock PIN a conductor would enter to verify the ticket (frontend-only demo).
CONDUCTOR_PIN = "1234"
MAX_ATTEMPTS = 3


class ViewTicketScreen(MDScreen):
    # Mock ticket data (frontend-only; would come from a booking in a real app).
    route = StringProperty("43A")
    source = StringProperty("Girme Park")
    destination = StringProperty("Hinjawadi Jakat Naka")
    fare = StringProperty("₹20")
    tickets_count = StringProperty("1")
    ticket_no = StringProperty("2606191913ZSYRA9")
    booking_time = StringProperty("")
    validity_time = StringProperty("")
    status = StringProperty("Valid")
    attempts_left = NumericProperty(MAX_ATTEMPTS)

    def on_pre_enter(self, *args):
        # Booking now, valid for the next hour.
        now = datetime.now()
        valid = now + timedelta(hours=1)
        self.booking_time = now.strftime("%d %b, %y | %I:%M %p")
        self.validity_time = valid.strftime("%d %b, %y | %I:%M %p")

    def on_enter(self, *args):
        # Start the looping zoom in/out pulse on the logo.
        logo = self.ids.get("ticket_logo")
        if not logo:
            return
        base, zoom = dp(LOGO_BASE), dp(LOGO_ZOOM)
        logo.size = (base, base)
        anim = (
            Animation(size=(zoom, zoom), duration=0.9, t="in_out_sine")
            + Animation(size=(base, base), duration=0.9, t="in_out_sine")
        )
        anim.repeat = True
        anim.start(logo)

    def on_leave(self, *args):
        # Stop the animation and reset the logo to its base size.
        logo = self.ids.get("ticket_logo")
        if logo:
            Animation.cancel_all(logo)
            logo.size = (dp(LOGO_BASE), dp(LOGO_BASE))

    def show_qr(self):
        # Generate a QR encoding the ticket number and show it in a popup.
        import qrcode

        app = App.get_running_app()
        path = os.path.join(app.user_data_dir, "ticket_qr.png")
        qr = qrcode.QRCode(box_size=10, border=2)
        qr.add_data(self.ticket_no)
        qr.make(fit=True)
        qr.make_image(fill_color="black", back_color="white").save(path)

        modal = Factory.QRCodeModal()
        modal.qr_source = path
        modal.open()

    def verify(self):
        # Open the conductor verification popup with a fresh attempt count.
        self.attempts_left = MAX_ATTEMPTS
        modal = Factory.ConductorVerifyModal()
        modal.screen = self
        modal.open()

    def verify_pin(self, modal):
        pin = modal.ids.pin_input.text.strip()
        if pin == CONDUCTOR_PIN:
            self.status = "Valid"
            modal.dismiss()
        else:
            if self.attempts_left > 0:
                self.attempts_left -= 1
            if self.attempts_left <= 0:
                self.status = "Expired"
                modal.dismiss()

    def go_back(self):
        app = App.get_running_app()
        app.root.transition.direction = "right"
        app.root.current = "dashboard"
