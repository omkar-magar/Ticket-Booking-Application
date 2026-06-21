from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.factory import Factory
from kivy.properties import StringProperty

# Mock diversion route data (frontend-only).
ROUTES = [
    {"badge": "आँगी 2", "route": "लोकशाहीर मा. अण्णाभाऊ ...", "tag": "Water Logging"},
    {"badge": "279", "route": "मार्केटयार्ड → कातर खडक खावली", "tag": "Water Logging"},
    {"badge": "233ब", "route": "मार्केटयार्ड → भादस", "tag": "Water Logging"},
    {"badge": "233अ", "route": "मार्केटयार्ड → कोळवण", "tag": "Water Logging"},
    {"badge": "233", "route": "मार्केटयार्ड → पोंडगाव", "tag": "Water Logging"},
    {"badge": "280", "route": "मार्केटयार्ड → हडपसर", "tag": "Water Logging"},
    {"badge": "158", "route": "स्वारगेट → कात्रज", "tag": "Water Logging"},
    {"badge": "102", "route": "पुणे स्टेशन → वाघोली", "tag": "Water Logging"},
    {"badge": "104", "route": "स्वारगेट → निगडी", "tag": "Water Logging"},
    {"badge": "107", "route": "पुणे स्टेशन → हडपसर", "tag": "Water Logging"},
    {"badge": "112", "route": "कोथरूड → स्वारगेट", "tag": "Water Logging"},
    {"badge": "129", "route": "शिवाजीनगर → वाघोली", "tag": "Water Logging"},
    {"badge": "131", "route": "स्वारगेट → मंजरी", "tag": "Water Logging"},
    {"badge": "143", "route": "पुणे स्टेशन → खराडी", "tag": "Water Logging"},
    {"badge": "160", "route": "कात्रज → हडपसर", "tag": "Water Logging"},
    {"badge": "162", "route": "स्वारगेट → धायरी", "tag": "Water Logging"},
    {"badge": "165", "route": "शनिवारवाडा → कोंढवा", "tag": "Water Logging"},
    {"badge": "178", "route": "पुणे स्टेशन → आळंदी", "tag": "Water Logging"},
    {"badge": "191", "route": "स्वारगेट → सासवड", "tag": "Water Logging"},
    {"badge": "201", "route": "मार्केटयार्ड → वारजे", "tag": "Water Logging"},
    {"badge": "210", "route": "कोथरूड → पाषाण", "tag": "Water Logging"},
    {"badge": "224", "route": "शिवाजीनगर → बाणेर", "tag": "Water Logging"},
    {"badge": "241", "route": "स्वारगेट → पिरंगुट", "tag": "Water Logging"},
    {"badge": "256", "route": "पुणे स्टेशन → लोणी काळभोर", "tag": "Water Logging"},
    {"badge": "262", "route": "हडपसर → फुरसुंगी", "tag": "Water Logging"},
    {"badge": "270", "route": "मार्केटयार्ड → उरुळी कांचन", "tag": "Water Logging"},
    {"badge": "288", "route": "स्वारगेट → भोर", "tag": "Water Logging"},
    {"badge": "301", "route": "निगडी → देहू रोड", "tag": "Water Logging"},
]


class DiversionScreen(MDScreen):
    count_text = StringProperty("")

    def on_pre_enter(self, *args):
        self._render(ROUTES)

    def _render(self, routes):
        self.count_text = f"{len(routes)} routes total"
        container = self.ids.routes_box
        container.clear_widgets()
        for r in routes:
            parts = r["route"].split("→")
            source = parts[0].strip()
            dest = parts[1].strip() if len(parts) > 1 else ""
            card = Factory.RouteCard()
            card.badge_text = r["badge"]
            card.source_text = source
            card.dest_text = dest
            card.show_arrow = bool(dest)
            card.tag_text = r["tag"]
            container.add_widget(card)

    def search(self):
        query = self.ids.route_input.text.strip()
        if not query:
            self._render(ROUTES)
            return
        filtered = [
            r for r in ROUTES
            if query in r["badge"] or query in r["route"]
        ]
        self._render(filtered)

    def go_back(self):
        app = App.get_running_app()
        app.root.transition.direction = "right"
        app.root.current = "dashboard"
