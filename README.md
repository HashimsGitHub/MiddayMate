# MiddayMate (M2)

> **M2 Find Someone New.**

MiddayMate is a location-based hospitality engagement platform that connects busy CBD professionals with nearby cafés and restaurants while making it easy to discover people who are available to meet during coffee and lunch breaks.

Unlike traditional social or dating applications, MiddayMate is built around **venues and promotions first**, with people and conversations naturally following.

<img width="1023" height="700" alt="a-business-executive-couple-by-a-large-window-in-the-office-at-sunset-taking-a-break-from-work-ai-generated-photo" src="https://github.com/user-attachments/assets/0e0be072-c999-4e1d-ac5d-efa2fd3a089a" />

---

# Vision

Our vision is to become the preferred lunchtime and coffee-break platform for professionals working in Central Business Districts (CBDs).

By helping hospitality venues attract customers during office hours and making spontaneous social meetups easier, MiddayMate creates value for both businesses and professionals.

---

# The Problem

Busy professionals often have:

* Limited opportunities to socialise during the workday.
* Short coffee and lunch breaks.
* Difficulty discovering nearby venue promotions.
* No simple way to know who else is available for a spontaneous meetup.

At the same time, cafés and restaurants often have unused capacity during weekday business hours and need effective ways to attract nearby office workers.

MiddayMate connects these two groups through one simple platform.

---

# How It Works

### For Users

* Sign in securely using OAuth.
* Create a simple professional profile.
* Discover nearby cafés and restaurants.
* Browse current promotions and exclusive offers.
* See who is available nearby.
* Invite someone to join you for coffee or lunch.
* Chat after an invitation is accepted.
* Enjoy the venue promotion together.

### For Vendors

* Register a business profile.
* Promote cafés, restaurants and events.
* Publish limited-time campaigns and discounts.
* Target nearby CBD professionals.
* Measure campaign performance through analytics.
* Increase weekday foot traffic.

---

# Core Features

## User Features

* OAuth authentication
* Professional profile
* Availability status
* Nearby venue discovery
* Promotion browsing
* Social invitations
* Match and chat
* Favourite venues
* Optional social media links

## Vendor Features

* Business profile management
* Campaign management
* Venue image gallery
* Promotions and discounts
* Featured listings
* Campaign analytics
* Customer engagement dashboard

## Administration

* User moderation
* Vendor approval
* Campaign approval
* Content management
* Reports and analytics

---

# Technology Stack

## Frontend

* HTML5
* CSS3
* Vanilla JavaScript

## Backend

* Python Flask
* REST API
* SQLAlchemy ORM

## Database

* SQLite (MVP)

Future migration:

* Azure SQL Database

## Storage

* Azure Blob Storage

Used for:

* User profile photos
* Vendor images
* Promotional media

## Hosting

* Azure Container Apps
* Docker

---

# Authentication

MiddayMate uses OAuth authentication to simplify onboarding and reduce fake accounts.

Supported providers:

* Microsoft
* Google

Future support:

* Apple

Passwords are not stored by the application.

---

# Privacy First

MiddayMate is designed around minimal data collection.

We only collect information necessary to operate the platform.

We intentionally do **not** store:

* Passwords
* Payment card information
* Government-issued identity documents
* Unnecessary personal information

Profile images are stored in Azure Blob Storage, while the database stores only secure references to those images.

---

# Repository Structure

```text
MiddayMate/

├── frontend/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── assets/
│
├── backend/
│   ├── api/
│   ├── auth/
│   ├── database/
│   ├── models/
│   ├── services/
│   └── templates/
│
├── docs/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Current Status

**🎨 Project Phase:** Mockup/Prototype Phase

This is a **functional mockup** with fully hardcoded frontend data. All core features are working with mock data for demonstration and testing of the UI/UX.

**See [MOCKUP_README.md](MOCKUP_README.md) for current mockup details.**

The next phase will add:
- Real OAuth authentication
- Production database
- Actual user profiles and messaging
- Vendor/business features

---



## Live Site (MockUp)

Visit the live site: https://middaymate.netlify.app/

# Documentation

Project documentation is located in the **/docs** directory.

* Project Vision
* Business Model
* Product Requirements
* System Architecture
* Database Design
* API Specification
* UI / UX Guidelines


---

**MiddayMate** — M2 Find Someone New

<img width="1518" height="1036" alt="CoffeeFirstDate" src="https://github.com/user-attachments/assets/73e93e99-8c88-45ae-bc0d-33a7a176f899" />
