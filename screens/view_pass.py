import os
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.factory import Factory
from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.metrics import dp

# Logo pulse sizes for the pass page. The logo starts at its base size and
# shrinks down to LOGO_ZOOM, then back — a gentle "breathe in" pulse.
LOGO_BASE = 152
LOGO_ZOOM = 132

# Mock PIN a conductor would enter to verify the pass (frontend-only demo).
CONDUCTOR_PIN = "1234"
MAX_ATTEMPTS = 3


class ViewPassScreen(MDScreen):
    # Mock pass data (frontend-only; would come from a purchase in a real app).
    pass_type = StringProperty("PMC & PCMC")
    pass_id = StringProperty("5040")
    fare = StringProperty("₹70.83")
    pass_no = StringProperty("2606221050WEMV8T")
    pass_label = StringProperty("One Day Pass")
    booking_time = StringProperty("22 Jun, 26 | 10:50 AM")
    validity_time = StringProperty("22 Jun, 26 | 11:59 PM")
    # "Valid" shows a green status; anything else shows a grey status.
    status = StringProperty("Valid")
    attempts_left = NumericProperty(MAX_ATTEMPTS)

    def on_enter(self, *args):
        # Start the looping zoom in/out pulse on the logo.
        logo = self.ids.get("pass_logo")
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
        logo = self.ids.get("pass_logo")
        if logo:
            Animation.cancel_all(logo)
            logo.size = (dp(LOGO_BASE), dp(LOGO_BASE))

    def edit_id(self):
        # Tap-to-edit the pass ID. Opens a small dialog so the on-screen value
        # keeps its exact font; the new value is written back in apply_id().
        modal = Factory.EditIDModal()
        modal.screen = self
        modal.start_text = self.pass_id
        modal.open()

    def apply_id(self, modal):
        value = modal.ids.id_input.text.strip()
        if value:
            self.pass_id = value
        modal.dismiss()

    def show_qr(self):
        # Generate a QR encoding the pass number and show it in a popup.
        import qrcode

        app = App.get_running_app()
        path = os.path.join(app.user_data_dir, "pass_qr.png")
        qr = qrcode.QRCode(box_size=10, border=2)
        qr.add_data(self.pass_no)
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
