# Database Schema

## Core Tables
- users
  - id
  - name
  - email
  - role
  - availability_status
  - profile_image_url
- venues
  - id
  - name
  - address
  - latitude
  - longitude
  - description
- promotions
  - id
  - venue_id
  - title
  - description
  - start_date
  - end_date
- invitations
  - id
  - sender_id
  - recipient_id
  - venue_id
  - status
  - created_at
- messages
  - id
  - conversation_id
  - sender_id
  - content
  - created_at

## Notes
The schema should remain simple for the MVP and support future extension.
