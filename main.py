import os
import sys
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window

# Ensure the current directory is in sys.path for clean module imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from screens.dashboard import DashboardScreen
from screens.bus_ticket import BusTicketScreen
from screens.daily_pass import DailyPassScreen
from screens.view_ticket import ViewTicketScreen
from screens.view_pass import ViewPassScreen

class AMGApp(MDApp):
    def build(self):
        # Application Theme Configuration (Material Design)
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Light"

        # Load KV Layout files
        # We load the dashboard layout here; other screens can be loaded dynamically
        kv_path = os.path.join(BASE_DIR, 'kv', 'dashboard.kv')
        Builder.load_file(kv_path)
        # Placeholder loading for other KVs - normally you'd automate this
        # Builder.load_file('kv/bus_ticket.kv') ...

        # Initialize Screen Manager with native-like transitions
        self.screen_manager = ScreenManager(transition=SlideTransition())

        # Register all screens
        self.screen_manager.add_widget(DashboardScreen(name='dashboard'))
        self.screen_manager.add_widget(BusTicketScreen(name='bus_ticket'))
        self.screen_manager.add_widget(DailyPassScreen(name='daily_pass'))
        self.screen_manager.add_widget(ViewTicketScreen(name='view_ticket'))
        self.screen_manager.add_widget(ViewPassScreen(name='view_pass'))
        
        self.screen_manager.current = 'dashboard'

        # Bind hardware back button (essential for Android UX)
        Window.bind(on_keyboard=self.on_back_button)

        return self.screen_manager

    def on_back_button(self, window, key, *args):
        """
        Handles the Android back button. 
        If not on the dashboard, it returns to the dashboard instead of exiting.
        """
        if key == 27:  # 27 is the keycode for Back/Esc
            if self.screen_manager.current != 'dashboard':
                self.screen_manager.transition.direction = "right"
                self.screen_manager.current = 'dashboard'
                return True  # Event handled
        return False  # Let the system handle it (standard app exit)

if __name__ == '__main__':
    AMGApp().run()