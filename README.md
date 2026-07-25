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

# Quick Start

## Local Development

```bash
# 1. Clone and setup
git clone <repo-url>
cd MiddayMate
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup environment
cp .env.example .env

# 4. Seed database
python scripts/seed_database.py

# 5. Run application
python run.py
```

Open `http://localhost:5000` in your browser.

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed instructions.

## Azure Deployment

To deploy to Azure Container Apps:

1. **Prerequisites**: Azure CLI and Docker installed
2. **Automated Setup** (Recommended):
   ```bash
   # Windows PowerShell
   .\scripts\azure_setup.ps1

   # macOS/Linux
   bash scripts/azure_setup.sh
   ```
3. **Manual Setup**: See [AZURE_SETUP.md](AZURE_SETUP.md) for step-by-step instructions

**Quick Reference**: [AZURE_QUICK_REFERENCE.md](AZURE_QUICK_REFERENCE.md)

### Key Azure Resources
- Container Registry: `middaymatecr`
- Storage Account: `middaymatesa`
- SQL Server: `middaymate-sql` (optional)
- Container App: `middaymate`
- Region: `australiaeast`

---

# Documentation

Project documentation is located in the **/docs** directory.

* Project Vision
* Business Model
* Product Requirements
* System Architecture
* Database Design
* API Specification
* UI / UX Guidelines

## Setup Guides
* [Development Guide](DEVELOPMENT.md) - Local setup and development
* [Azure Setup Guide](AZURE_SETUP.md) - Complete Azure deployment instructions
* [Azure Quick Reference](AZURE_QUICK_REFERENCE.md) - Quick lookup for Azure commands
* [AI Guidelines](ai/00_Code_Instructions.md) - Guidelines for AI-assisted development



---

# MVP Goals

The first release focuses on validating three core outcomes:

* Professionals discover nearby hospitality promotions.
* Professionals arrange real-world coffee or lunch meetups.
* Hospitality venues increase weekday customer traffic through targeted campaigns.


---

# Guiding Principles

* Keep the MVP simple.
* Focus on solving real user problems.
* Build for fast deployment and rapid iteration.
* Minimise operational costs.
* Protect user privacy.
* Create measurable value for hospitality businesses.
* Technology should support the product—not define it.

---

# Current Status

**Project Phase:** Planning & MVP Development

The current objective is to build, validate, and launch an MVP within a single Docker container hosted on Azure Container Apps before expanding the platform based on real user feedback.

---

**MiddayMate**

**M2 Find Someone New**
<img width="1518" height="1036" alt="CoffeeFirstDate" src="https://github.com/user-attachments/assets/73e93e99-8c88-45ae-bc0d-33a7a176f899" />
