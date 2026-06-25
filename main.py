import os
import sys
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.utils import platform as kivy_platform

# Only force a phone-sized window on desktop (for previewing). On Android/iOS
# the app must fill the real screen — never set Window.size there, or it renders
# into a fixed box in the corner. Note: Python's platform.system() is unreliable
# on Android, so use Kivy's platform detection instead.
if kivy_platform not in ("android", "ios"):
    Window.size = (393, 852)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Register a Devanagari-capable font so Marathi/Hindi text renders correctly
# (Kivy's default Roboto cannot display Devanagari script).
_FONT_PATH = os.path.join(BASE_DIR, "assets", "fonts", "NotoSansDevanagari-Regular.ttf")
if os.path.exists(_FONT_PATH):
    LabelBase.register(name="Devanagari", fn_regular=_FONT_PATH)

from screens.splash import SplashScreen
from screens.dashboard import DashboardScreen
from screens.bus_ticket import BusTicketScreen
from screens.daily_pass import DailyPassScreen
from screens.view_ticket import ViewTicketScreen
from screens.view_pass import ViewPassScreen
from screens.profile import ProfileScreen
from screens.diversion import DiversionScreen


class AMGApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Light"

        kv_dir = os.path.join(BASE_DIR, 'kv')
        if os.path.exists(kv_dir):
            for kv_file in sorted(os.listdir(kv_dir)):
                if kv_file.endswith('.kv'):
                    Builder.load_file(os.path.join(kv_dir, kv_file))

        # Only build the splash up front so the first frame paints instantly.
        # The remaining screens (especially the image-heavy dashboard) are
        # constructed one frame later in on_start, while the splash is visible —
        # otherwise the app appears frozen on a blank window until every screen
        # and asset has loaded.
        self.screen_manager = ScreenManager(transition=SlideTransition())
        self.screen_manager.add_widget(SplashScreen(name='splash'))
        self.screen_manager.current = 'splash'

        Window.bind(on_keyboard=self.on_back_button)
        return self.screen_manager

    def on_start(self):
        # Defer the heavy screens until after the splash has rendered.
        # Build the dashboard first (the splash waits on it before advancing),
        # then construct the remaining screens one per frame so no single frame
        # janks while the splash is on screen.
        Clock.schedule_once(self._build_dashboard, 0)

    def _build_dashboard(self, *args):
        self.screen_manager.add_widget(DashboardScreen(name='dashboard'))

        # Secondary screens are not needed for the first interaction, so build
        # them lazily — one at a time, each on its own frame — to spread the
        # construction cost instead of hanging on a single heavy frame.
        self._pending_screens = [
            lambda: BusTicketScreen(name='bus_ticket'),
            lambda: DailyPassScreen(name='daily_pass'),
            lambda: ViewTicketScreen(name='view_ticket'),
            lambda: ViewPassScreen(name='view_pass'),
            lambda: ProfileScreen(name='profile'),
            lambda: DiversionScreen(name='diversion'),
        ]
        Clock.schedule_once(self._build_next_screen, 0)

    def _build_next_screen(self, *args):
        if not self._pending_screens:
            return
        make_screen = self._pending_screens.pop(0)
        self.screen_manager.add_widget(make_screen())
        # Yield a frame between each screen so the UI stays responsive.
        Clock.schedule_once(self._build_next_screen, 0)

    def on_back_button(self, window, key, *args):
        if key == 27:
            if self.screen_manager.current != 'dashboard':
                self.screen_manager.transition.direction = "right"
                self.screen_manager.current = 'dashboard'
                return True
        return False


if __name__ == '__main__':
    AMGApp().run()
