# Android Ticket Booking Application - Frontend Development Prompt

## Objective
Create a complete **frontend-only Android Ticket Booking Application** using:

* Python
* Kivy
* KivyMD (for Material Design components)
* Buildozer
* Plyer (for GPS/Location access)

The application should be designed for Android devices and packaged using Buildozer.

---

# Project Directory Structure

The project already exists in the following location:

```text
Don't Do It/
└── AMG-14-06-2026/
```

All source code, assets, screens, widgets, and configuration files should be organized inside the `AMG-14-06-2026/` directory.

---

# Application Overview

The application is a public transport ticket booking system.

Users should be able to:

* View their current location
* Book bus tickets
* Purchase daily passes
* View booked tickets
* View purchased passes

This is currently a frontend-only application.

No backend implementation is required.

Focus on:

* Modern UI
* Android-friendly design
* Navigation flow
* Widget organization
* Responsive layouts
* Kivy architecture

---

# Dashboard Screen

The dashboard is the application's landing page.

Design a modern Android-style dashboard with:

* Application Header
* User Information Section
* Current Location Card
* Quick Actions Area
* Functional Widgets
* Additional Placeholder Widgets

Use:

* Rounded corners
* Elevation/shadow effects
* Modern spacing
* Card-based layouts
* Professional color scheme

---

# Functional Widgets

The following widgets must be fully functional.

---

## 1. Bus Ticket

### Purpose

Allow users to view ticket information.

### Features

* Show Current Location
* Destination Selection
* Route Information
* Ticket Fare Display
* Confirm Ticket Button

### Screen Elements

* Source Location Field
* Destination Field
* Fare Card
* Book Ticket Button

---

## 2. Daily Pass

### Purpose

Allow users to view available daily passes.

### Features

* Daily Pass Types
* Pass Pricing
* Pass Validity
* Pass Information Cards

### Screen Elements

* Pass List
* Price Section
* Validity Section
* Purchase Button

---

## 3. View Ticket

### Purpose

Display booked ticket information.

### Information Displayed

* Ticket ID
* Source Location
* Destination
* Fare
* Booking Date
* Ticket Status

### UI Style

Use modern information cards.

---

## 4. View Pass

### Purpose

Display purchased pass information.

### Information Displayed

* Pass ID
* Pass Type
* Purchase Date
* Expiry Date
* Validity Status

### UI Style

Use Android-style cards.

---

# Additional Widgets

The dashboard may contain additional widgets for future features.

These widgets should:

* Display icons
* Display titles
* Show descriptions
* Be visually consistent

They can remain non-functional placeholders.

---

# Screen Navigation

Implement the following navigation structure:

```text
Dashboard
│
├── Bus Ticket
│
├── Daily Pass
│
├── View Ticket
│
└── View Pass
```

Requirements:

* Smooth navigation
* Back button support
* Return to dashboard from every screen

---

# Current Location Display

The dashboard should include a Current Location section.

Flow:

```text
Application Starts
        │ (Check & Request Permissions)
        ▼
Request Location Permission
        │
        ▼
Get Latitude & Longitude
        │
        ▼
Convert to Location Name
        │
        ▼
Display Current Location
```

Example:

```text
📍 Current Location
Mumbai, Maharashtra
```

---

# UI Design Requirements

## Theme

Create a professional Android design.

Use:

* Rounded cards
* Clean typography
* Consistent spacing
* Material-inspired layouts

## Dashboard Layout

```text
--------------------------------
Header
--------------------------------

Welcome Section

--------------------------------
Current Location Card
--------------------------------

--------------------------------
Quick Actions Grid
--------------------------------

[ Bus Ticket ]
[ Daily Pass ]

[ View Ticket ]
[ View Pass ]

--------------------------------
Additional Widgets
--------------------------------
```

---

# Recommended Folder Structure

```text
Don't Do It/
└── AMG-14-06-2026/
    │
    ├── main.py
    │
    ├── screens/
    │   ├── dashboard.py
    │   ├── bus_ticket.py
    │   ├── daily_pass.py
    │   ├── view_ticket.py
    │   └── view_pass.py
    │
    ├── widgets/
    │   ├── custom_card.py
    │   ├── custom_button.py
    │   └── navigation_bar.py
    │
    ├── assets/
    │   ├── images/
    │   ├── icons/
    │   ├── fonts/
    │   └── theme.json
    │
    ├── kv/
    │   ├── dashboard.kv
    │   ├── bus_ticket.kv
    │   ├── daily_pass.kv
    │   ├── view_ticket.kv
    │   └── view_pass.kv
    │
    └── buildozer.spec
```

---

# Code Quality Requirements

Generate code that is:

* Modular
* Beginner-friendly
* Reusable
* Well-commented
* Easy to maintain

Avoid:

* Monolithic files
* Hardcoded UI logic
* Duplicate components

---

# Android Requirements

The application must:

* Work on Android devices
* Be compatible with Buildozer
* Support different screen sizes
* Support portrait mode
* Follow Android UI guidelines
* Handle Android Runtime Permissions (GPS)
* Include `INTERNET`, `ACCESS_FINE_LOCATION`, and `ACCESS_COARSE_LOCATION` in buildozer.spec


# Expected Deliverables

Generate:

1. Frontend Architecture
2. Screen Flow Diagram
3. Folder Structure
4. Kivy Screen Design Plan
5. Widget Design System
6. Navigation Architecture
7. UI Component Breakdown
8. Android Optimization Suggestions
9. Buildozer Configuration Suggestions
10. Step-by-Step Implementation Roadmap

The final output should resemble a production-ready Android ticket booking application's frontend architecture and implementation plan.
