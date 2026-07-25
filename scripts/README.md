# MiddayMate Scripts

Utility scripts for development and operations.

## Database Scripts

### `seed_database.py`

Populates the development database with sample data.

**Usage:**
```bash
python scripts/seed_database.py
```

This script will:
- Create sample users (professionals)
- Create sample vendors
- Create sample venues in Sydney CBD
- Create sample promotions with discounts

**Data Created:**
- 3 users with different availability statuses
- 3 vendors (2 approved, 1 pending)
- 3 venues
- 4 promotional offers

## Running Tests

```bash
pytest                    # Run all tests
pytest -v                 # Verbose output
pytest --cov             # With coverage report
pytest tests/test_models.py  # Specific test file
```
