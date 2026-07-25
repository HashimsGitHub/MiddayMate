# MiddayMate Development Guide

## Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Git
- Docker (optional, for containerized development)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd MiddayMate
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize database**
   ```bash
   python scripts/seed_database.py
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

The app will be available at `http://localhost:5000`

## Project Structure

```
MiddayMate/
├── app/
│   ├── __init__.py          # App factory
│   ├── config.py            # Configuration
│   ├── models.py            # Database models
│   ├── utils.py             # Utility functions
│   └── routes/
│       ├── auth.py          # Authentication endpoints
│       ├── users.py         # User endpoints
│       ├── venues.py        # Venue endpoints
│       ├── promotions.py    # Promotion endpoints
│       ├── invitations.py   # Invitation endpoints
│       ├── messages.py      # Messaging endpoints
│       └── vendors.py       # Vendor endpoints
├── frontend/
│   ├── index.html           # Main HTML
│   ├── css/
│   │   └── style.css        # Styles
│   └── js/
│       └── app.js           # Client-side logic
├── tests/
│   ├── test_models.py       # Model tests
│   └── test_routes.py       # Route tests
├── scripts/
│   └── seed_database.py     # Database seeding
├── run.py                   # Entry point
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker configuration
└── docker-compose.yml       # Docker Compose setup
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - Login with OAuth
- `POST /api/auth/logout` - Logout
- `GET /api/auth/me` - Get current user

### Users
- `GET /api/users/me` - Get current user profile
- `POST /api/users/profile` - Update profile
- `GET /api/users/<id>` - Get user by ID

### Venues
- `GET /api/venues` - Get all venues
- `GET /api/venues/<id>` - Get venue details

### Promotions
- `GET /api/promotions` - Get active promotions
- `GET /api/promotions/venue/<venue_id>` - Get promotions for venue

### Invitations
- `POST /api/invitations` - Create invitation
- `GET /api/invitations` - Get invitations
- `POST /api/invitations/<id>/accept` - Accept invitation
- `POST /api/invitations/<id>/decline` - Decline invitation

### Messages
- `POST /api/messages` - Send message
- `GET /api/messages/invitation/<id>` - Get conversation messages

### Vendors
- `POST /api/vendors` - Register vendor
- `GET /api/vendors/<id>` - Get vendor details
- `GET /api/vendors/<id>/venues` - Get vendor's venues
- `POST /api/vendors/<id>/promotions` - Create promotion
- `PUT /api/vendors/<id>/promotions/<promotion_id>` - Update promotion

## Testing

### Run tests
```bash
pytest                      # Run all tests
pytest -v                   # Verbose
pytest --cov              # With coverage
pytest tests/test_models.py  # Specific file
```

### Test structure
- `tests/test_models.py` - Database model tests
- `tests/test_routes.py` - API endpoint tests

## Database

### Models
- **User** - Professionals and admins
- **Vendor** - Business owners
- **Venue** - Cafés and restaurants
- **Promotion** - Time-limited offers
- **Invitation** - Meetup requests
- **Message** - Conversation messages

### Migrations
Currently using SQLAlchemy with auto-migration. For future migrations, consider using Alembic.

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Write docstrings for functions
- Keep functions focused and small
- Add type hints where beneficial

## Common Tasks

### Add a new API endpoint
1. Create a route in `app/routes/`
2. Define the blueprint and register in `app/__init__.py`
3. Add tests in `tests/`

### Add a new model
1. Define in `app/models.py`
2. Add relationships as needed
3. Create migration if needed

### Database seeding
```bash
python scripts/seed_database.py
```

## Docker Development

### Build image
```bash
docker build -t middaymate:dev .
```

### Run container
```bash
docker-compose up
```

### Access the app
Open `http://localhost:5000`

## Environment Variables

See `.env.example` for all available variables:
- `FLASK_ENV` - Development/production
- `SECRET_KEY` - Session secret
- `DATABASE_URL` - Database connection string
- `AZURE_STORAGE_CONNECTION_STRING` - Azure storage
- OAuth credentials for Microsoft/Google

## Debugging

### Flask debug mode
```bash
FLASK_ENV=development python run.py
```

### Database debugging
```bash
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); print(db.engine.url)"
```

### View database contents
```bash
sqlite3 middaymate.db ".tables"
sqlite3 middaymate.db "SELECT * FROM users;"
```

## Deployment

See main README.md for Azure Container Apps deployment instructions.

## Resources

- Flask: https://flask.palletsprojects.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- pytest: https://pytest.org/
