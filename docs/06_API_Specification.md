# API Specification

## Authentication

POST /api/auth/login

POST /api/auth/logout

---

## Users

GET /api/users/me

PUT /api/users/me

GET /api/users/nearby

GET /api/users/available

---

## Promotions

GET /api/promotions

GET /api/promotions/nearby

GET /api/promotions/{id}

---

## Vendors

GET /api/vendors

GET /api/vendors/{id}

GET /api/vendors/promotions

---

## Invitations

POST /api/invitations

PUT /api/invitations/accept

PUT /api/invitations/reject

---

## Chat

GET /api/chat/{id}

POST /api/chat/send

---

## Administration

CRUD

Users

Vendors

Campaigns

Promotions

Reports