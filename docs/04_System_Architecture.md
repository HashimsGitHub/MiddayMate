# System Architecture

Internet

↓

GoDaddy DNS

↓

Azure Container Apps

↓

Flask

↓

SQLite

↓

Azure Blob Storage

## Hosting

Single Docker Container

Contains

- Frontend
- Backend
- Authentication
- REST API

## Storage

Azure Blob Storage

Stores:

- Profile Photos

SQLite stores URLs only.

## Future

SQLite

↓

Azure SQL

↓

Azure Kubernetes Service (AKS)

No Kubernetes required for MVP.