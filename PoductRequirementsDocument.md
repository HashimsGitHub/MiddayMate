# MiddayMate (M²)

## Product Requirements Document (PRD)

Version: 1.0 MVP

---

# Project Overview

MiddayMate is a location-based dating platform designed specifically for professionals working in Central Business Districts (CBDs).

The application enables busy professionals to meet over coffee or lunch during office hours.

Unlike traditional dating applications, MiddayMate focuses on real-world meetings that occur during existing coffee and lunch breaks.

The platform also serves cafés and restaurants by promoting their venues and campaigns to users looking for meeting locations.

---

# Product Vision

"Dating for Professionals, Over Coffee."

MiddayMate creates meaningful real-world introductions while helping hospitality venues increase weekday business.

---

# Problem Statement

Professionals often struggle to meet compatible people because of:

- Long work hours
- Career-focused lifestyles
- Limited evening availability
- Traditional dating apps encourage endless chatting rather than meeting

At the same time, cafés and restaurants have spare seating capacity during weekdays.

MiddayMate connects these two markets.

---

# Target Audience

Professionals aged 21+

Examples:

- Lawyers
- Doctors
- Engineers
- Executives
- Consultants
- Accountants
- Corporate Employees
- Entrepreneurs

---

# Business Model

Users join free.

Revenue comes from Vendors.

Vendors include:

- Cafés
- Restaurants
- Wine Bars
- Dessert Cafés

Revenue sources:

- Featured Listings
- Sponsored Campaigns
- Dating Discounts
- Premium Venue Placement

Users are never required to purchase subscriptions for the MVP.

---

# User Types

## 1. User

Can:

- Register
- Login
- Edit profile
- Upload selfies
- Browse nearby matches
- Like
- Pass
- Match
- Chat
- Select meeting venue
- Redeem vendor promotions

---

## 2. Vendor

Can:

- Register business
- Login
- Create campaigns
- Upload venue images
- Publish dating discounts
- View campaign analytics
- Manage venue information
- Sponsor listings

---

## 3. Administrator

Can:

- Manage users
- Moderate reports
- Approve vendors
- Manage campaigns
- Manage featured listings
- Manage categories
- View analytics

---

# Authentication

No usernames.

No passwords.

Supported providers:

- Microsoft
- Google
- Apple (future)

OAuth is used primarily to reduce fake accounts and simplify onboarding.

Store only:

OAuth Provider

OAuth User ID

Email

First Name

Nothing more than necessary.

---

# User Profile

Fields

First Name

Profile Photo

Job Title

Company (optional)

Office Location

Short Bio

Coffee Preference

Lunch Preference

Instagram URL (optional)

LinkedIn URL (optional)

---

# Matching

Swipe Right

Swipe Left

Mutual Like

↓

Match

↓

Chat

↓

Arrange Coffee or Lunch

---

# Chat

Simple messaging.

No voice.

No AI.

No video.

---

# Vendor Features

Business Profile

Venue Photos

Trading Hours

Campaigns

Discounts

Coupons

Featured Listings

Dashboard

Campaign Statistics

---

# Meeting Locations

Users can select venues from nearby participating vendors.

Example

Coffee

- Cafe A

- Cafe B

- Cafe C

Lunch

- Restaurant A

- Restaurant B

Venue promotions displayed alongside listings.

---

# Privacy

Store minimal PII.

Never store passwords.

Never store payment cards.

Never store government identity documents.

Profile photos stored in Azure Blob Storage.

Database stores only image URLs.

---

# MVP Technology Stack

Frontend

HTML5

CSS3

JavaScript

Folder

/frontend

---

Backend

Python Flask

REST API

---

Database

SQLite

Future

Azure SQL Database

---

Storage

Azure Blob Storage

---

Hosting

Azure Container Apps

Single Docker Container

Contains

Frontend

Backend

Authentication

REST API

---

Domain

middaymate.com

DNS hosted by GoDaddy

DNS points directly to Azure Container Apps

Azure Managed HTTPS Certificate

No URL masking

---

Repository Structure

MiddayMate/

    frontend/

        css/

        js/

        images/

    backend/

        api/

        auth/

        database/

        models/

        services/

    uploads/

    Dockerfile

    requirements.txt

    app.py

---

Database Tables

Users

Vendors

VendorCampaigns

Matches

Likes

Chats

Messages

VenueCategories

MeetingLocations

Reports

AdminUsers

---

API Endpoints

Authentication

POST /api/auth/login

POST /api/auth/logout

User

GET /api/users/me

PUT /api/users/me

GET /api/users/nearby

Matching

POST /api/like

POST /api/pass

GET /api/matches

Chat

GET /api/chat/{matchId}

POST /api/chat/send

Vendor

GET /api/vendors

GET /api/vendors/{id}

GET /api/campaigns

Admin

CRUD endpoints

---

Future Roadmap

Push Notifications

Photo Verification

Identity Verification

Premium Membership

Native Mobile Apps

Azure SQL

AKS

AI Matching (optional)

---

Non Functional Requirements

Responsive Design

Docker Deployment

Single Container

Simple Architecture

Fast Load Time

Minimal Dependencies

RESTful API

Secure Authentication

---

Out of Scope

Subscriptions

Voice Calls

Video Calls

AI Chat

AI Speech

Complex Recommendation Engine

Microservices

Kubernetes

---

Definition of MVP Success

Users successfully:

Register

Create profile

Upload photo

Match

Chat

Meet over coffee or lunch

Vendor successfully:

Creates campaign

Promotion appears inside application

Users choose promoted venue

---

Instructions for OpenAI Codex

Build this project using:

Python Flask

SQLite

HTML

CSS

Vanilla JavaScript

Docker

Azure Container Apps compatible deployment

Implement REST APIs.

Keep frontend and backend separated.

Use clean modular architecture.

Follow MVC principles.

Generate Dockerfile and docker-compose.yml.

Use SQLAlchemy ORM.

Use Flask Blueprint architecture.

Include database migrations.

Create sample data for testing.

Produce production-ready code with comments.

Do not introduce React, Angular, Vue or other frontend frameworks.

Keep the MVP lightweight and easily deployable.
