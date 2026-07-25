# Codex Instructions for MiddayMate

## Purpose
This file provides implementation guidance for AI-assisted development on the MiddayMate project.

## Project Summary
MiddayMate is a location-based hospitality engagement platform for CBD professionals. The MVP focuses on venue discovery, promotions, social invitations, and lightweight chat.

## Development Priorities
- Keep the MVP simple and usable.
- Prefer clear, maintainable Flask and vanilla JavaScript code.
- Use SQLite for the MVP and keep the schema straightforward.
- Ensure the experience feels useful to both professionals and venue owners.

## Constraints
- Do not introduce unnecessary complexity.
- Avoid over-engineering authentication or real-time features in the MVP.
- Preserve a privacy-first approach.
- Keep documentation and code aligned with the project goals.

## Implementation Guidance
- Start with core user and vendor flows.
- Prioritize nearby venue discovery and promotion browsing.
- Keep API endpoints RESTful and predictable.
- Write clear comments where business logic is non-obvious.

## Guidelines
You are building MiddayMate.

Always prefer simplicity over cleverness.

Do not introduce frameworks unless requested.

Frontend must remain HTML/CSS/Vanilla JavaScript.

Backend must remain Flask.

Never introduce React.

Never introduce Angular.

Never introduce Vue.

Keep everything Azure Container Apps compatible.

The project must run in one Docker container.

Use SQLAlchemy ORM.

Use Flask Blueprints.

Follow MVC.

Write production-quality code.

Write unit tests.

Write docstrings.

Avoid duplicate code.

Do not over-engineer.

Build features incrementally.