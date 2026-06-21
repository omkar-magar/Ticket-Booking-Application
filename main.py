import os
import sys
import platform
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase

if platform.system() != "Linux":
    Window.size = (393, 852)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Register a Devanagari-capable font so Marathi/Hindi text renders correctly
# (Kivy's default Roboto cannot display Devanagari script).
_FONT_PATH = os.path.join(BASE_DIR, "assets", "fonts", "NotoSansDevanagari-Regular.ttf")
if os.path.exists(_FONT_PATH):
    LabelBase.register(name="Devanagari", fn_regular=_FONT_PATH)

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

        self.screen_manager = ScreenManager(transition=SlideTransition())
        self.screen_manager.add_widget(DashboardScreen(name='dashboard'))
        self.screen_manager.add_widget(BusTicketScreen(name='bus_ticket'))
        self.screen_manager.add_widget(DailyPassScreen(name='daily_pass'))
        self.screen_manager.add_widget(ViewTicketScreen(name='view_ticket'))
        self.screen_manager.add_widget(ViewPassScreen(name='view_pass'))
        self.screen_manager.add_widget(ProfileScreen(name='profile'))
        self.screen_manager.add_widget(DiversionScreen(name='diversion'))

        self.screen_manager.current = 'dashboard'
        Window.bind(on_keyboard=self.on_back_button)
        return self.screen_manager

    def on_back_button(self, window, key, *args):
        if key == 27:
            if self.screen_manager.current != 'dashboard':
                self.screen_manager.transition.direction = "right"
                self.screen_manager.current = 'dashboard'
                return True
        return False


if __name__ == '__main__':
    AMGApp().run()
