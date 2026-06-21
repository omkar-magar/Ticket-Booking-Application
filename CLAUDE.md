# CLAUDE.md — AMG Transport Ticket Booking App

## Project Overview
Frontend-only Android ticket booking app for public transport (bus tickets, daily passes).
Built with **Python + Kivy + KivyMD**. Targets Android via Buildozer. No backend exists.

## Tech Stack
- Python 3.10+
- Kivy 2.x
- KivyMD (Material Design components)
- Buildozer (Android packaging)
- Plyer (GPS/location access, planned)

## Project Structure
```
AMG-14-06-2026/
├── main.py              # App entry point (AMGApp class, ScreenManager setup)
├── screens/             # Python screen classes (one file per screen)
│   ├── dashboard.py
│   ├── bus_ticket.py
│   ├── daily_pass.py
│   ├── view_ticket.py
│   └── view_pass.py
├── kv/                  # KV layout files (all UI lives here)
│   ├── dashboard (1).kv
│   ├── bus_ticket.kv
│   ├── daily_pass.kv
│   ├── view_ticket.kv
│   └── view_pass.kv
└── assets/              # PNG icons referenced in KV files
```

## How to Run
```
python main.py
```

## Theme
- Primary palette: Teal 400
- Theme style: Light
- Background: warm off-white `(0.953, 0.949, 0.941, 1)`
- Card color: light blue `(0.878, 0.937, 0.969, 1)`
- Top bar accent: teal `(0.17, 0.75, 0.67, 1)`
- Text: near-black `(0.08, 0.08, 0.08, 1)`

## Navigation
Hub-and-spoke: Dashboard is the home screen. All sub-screens return to Dashboard.
Transitions: SlideTransition — left to enter, right to return.
Android back button (key 27) returns to dashboard from any screen.

---

## STRICT UI RULES — READ BEFORE MAKING ANY CHANGE

### This is a frontend-only app. Every rule below is mandatory.

1. **All UI must be defined in KV files inside `kv/`.** Never build UI in Python code. Python screen classes handle logic only (navigation, event handlers, data formatting). If a screen needs a new layout, edit or create a `.kv` file.

2. **Do not add backend, database, API calls, or network requests.** This app is purely frontend. Use hardcoded/mock data for any content that would normally come from a server (ticket lists, pass details, fares, locations). Store mock data as Python dicts/lists in the screen class, never in external files.

3. **Follow the established design system exactly:**
   - Cards: light blue `(0.878, 0.937, 0.969, 1)`, rounded corners `dp(16)–dp(18)`, elevation 0 for action cards.
   - Backgrounds: warm off-white `(0.953, 0.949, 0.941, 1)` for scrollable areas, white `(1,1,1,1)` for top bars.
   - Font sizes: labels `dp(13)–dp(16)`, input text `dp(17)`, headings `H6`.
   - Top app bars on sub-screens: teal background, white text, left back arrow.
   - Do not introduce new colors, gradients, or dark backgrounds unless explicitly asked.

4. **Every screen must have a back button** that returns to dashboard with `transition.direction = "right"`.

5. **Use KivyMD components** (`MDCard`, `MDLabel`, `MDBoxLayout`, `MDTopAppBar`, `MDIconButton`, etc.). Do not use raw Kivy widgets when a KivyMD equivalent exists.

6. **Keep layouts responsive.** Use `dp()` for all sizes, paddings, and spacings. Use `size_hint` and `adaptive_height: True` — never hardcode pixel values without `dp()`. The app must look correct on varying Android screen sizes.

7. **Do not delete or restructure the dashboard layout.** The dashboard grid (2 large cards + 4 small cards) is finalized. Only modify it if the user explicitly asks. Adding new cards below the existing grid is allowed.

8. **Assets are PNG files in `assets/`.** Reference them by relative path (`assets/filename.png`). Do not embed base64 images or use URLs. If an asset doesn't exist yet, note it in a comment but don't break the layout — use an MDIcon as fallback.

9. **Marathi language support.** The search bar uses Marathi placeholder text. Preserve any Marathi strings. Do not replace them with English unless asked.

10. **No external dependencies beyond Kivy/KivyMD/Plyer.** Do not add pip packages. Everything must work within Buildozer's Android build pipeline.

11. **Screen naming convention:** screen names in ScreenManager are snake_case (`bus_ticket`, `daily_pass`, `view_ticket`, `view_pass`). KV class names are PascalCase (`BusTicketScreen`, `DailyPassScreen`). Never break this mapping.

12. **When building out sub-screens** (bus_ticket, daily_pass, view_ticket, view_pass), follow this pattern:
    - Keep the `MDTopAppBar` with back arrow
    - Use `ScrollView` wrapping an `MDBoxLayout(orientation: "vertical", adaptive_height: True)`
    - Content goes inside Material cards with the established color scheme
    - Use mock/hardcoded data — no empty placeholder labels

13. **Ripple behavior** (`ripple_behavior: True`) must be on all tappable cards. Non-interactive cards should not have ripple.

14. **Do not modify `main.py`** unless adding a new screen to the ScreenManager or adding app-level logic (like GPS permissions). The build method structure and screen registration order should stay as-is.

## Known Issues
- Dashboard KV file is named `dashboard (1).kv` (space + parentheses) — may cause build issues. Do not rename without user approval.
- Sub-screens (bus_ticket, daily_pass, view_ticket, view_pass) are stubs — they only show a centered label. These need to be built out with proper UI per the GEMINI.md spec.
- `buildozer.spec` does not exist yet.
- GPS/current location feature is specced but not implemented.
- Route Timetable and Metro Ticket dashboard cards are placeholders with no linked screens.
