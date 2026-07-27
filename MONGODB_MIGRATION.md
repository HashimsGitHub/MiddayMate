# MongoDB Migration Summary

**Date**: 2026-07-27  
**Status**: ✅ Complete

## Overview
Successfully migrated MiddayMate from SQLAlchemy (SQL) + SQLite to **MongoEngine** (MongoDB ODM).

## What Changed

### 1. Dependencies (requirements.txt)
- ❌ Removed: `Flask-SQLAlchemy==3.1.1`, `SQLAlchemy==2.0.23`
- ✅ Added: `Flask-MongoEngine==1.0.0`, `MongoEngine==0.27.0`

### 2. Database Configuration (app/config.py)
- Changed all configs to use `MONGO_URI` instead of `SQLALCHEMY_DATABASE_URI`
- Removed `SQLALCHEMY_TRACK_MODIFICATIONS` setting
- All configs now require `MONGO_URI` environment variable (required in production)

### 3. Database Models (app/models.py)
Complete rewrite converting SQLAlchemy ORM to MongoEngine Documents:
- User, Venue, Vendor, Promotion, Invitation, Message models migrated
- Relationships converted: `db.relationship()` → `ReferenceField()`
- Foreign keys converted: `db.Column(db.Integer, db.ForeignKey(...))` → `ReferenceField()`
- Association table removed: `user_favorites` → `ListField(ReferenceField())` in User
- Added MongoDB-specific: `meta` class with `collection` name and `indexes`
- Embedded document: `SocialMediaLinks` for storing social media links

### 4. App Initialization (app/__init__.py)
- Changed: `SQLAlchemy()` → `FlaskMongoEngine()`
- Removed: `db.create_all()` (MongoDB creates collections automatically)
- Updated: `seed_initial_data()` to use `.save()` instead of `db.session.commit()`
- Updated: Seeding logic to work with MongoEngine document operations

### 5. All Route Files Updated

#### app/routes/users.py
- `User.query.get()` → `User.objects.get()`
- `db.session.commit()` → `.save()`
- Added: `ObjectDoesNotExist` exception handling

#### app/routes/venues.py
- `Venue.query.all()` → `list(Venue.objects())`
- `Venue.query.get()` → `Venue.objects.get()`
- Removed: SQLAlchemy import

#### app/routes/promotions.py
- `Promotion.query.filter()` → `Promotion.objects(start_date__lte=..., end_date__gte=...)`
- `filter_by()` → Direct object references with ReferenceField

#### app/routes/invitations.py
- Converted all SQLAlchemy queries to MongoEngine
- Handle ReferenceField relationships properly
- Updated status enum handling

#### app/routes/messages.py
- Converted query operations to MongoEngine syntax
- `order_by()` → `order_by('created_at')`
- `update()` → `update(is_read=True)` on queryset

#### app/routes/vendors.py
- All vendor/venue lookups use ReferenceField relationships
- Status code handling updated for new ORM

#### app/routes/auth.py
- `User.query.filter_by()` → `User.objects()`
- Session IDs converted to strings: `session['user_id'] = str(user.id)`

#### app/routes/seed.py
- Complete rewrite for MongoEngine
- Dropped collections instead of clearing sessions
- Creates Vendor document first (required for FK relationships)
- Uses `.save()` for persistence

### 6. Docker Configuration
- ✅ Removed: `RUN mkdir -p /app/instance` (SQLite directory)
- ✅ Updated: `docker-compose.yml` to use `MONGO_URI` environment variable

### 7. Environment Files
- Updated `.env.example` with proper MongoDB connection string format
- Replaced hardcoded SQLite path with SaaS provider connection string

### 8. Tests (tests/test_models.py)
- Converted from SQLAlchemy pytest fixtures to MongoEngine
- Changed: `db.session.add()` → `.save()`
- Changed: `db.query.filter_by()` → `.objects()`
- Added: `.delete()` for cleanup after tests

## Key MongoDB Differences

| SQLAlchemy | MongoEngine |
|-----------|-----------|
| `db.Model` | `Document` |
| `db.Column()` | `StringField()`, `IntField()`, etc. |
| `db.ForeignKey()` | `ReferenceField()` |
| `db.relationship()` | `ReferenceField()` |
| `.query.get()` | `.objects.get()` |
| `.query.filter_by()` | `.objects()` |
| `.query.filter()` | `.objects(field__op=value)` (lookup operators) |
| `db.session.commit()` | `.save()` |
| `db.drop_all()` | `.drop_collection()` |

## MongoDB Connection String Format

Your connection string:
```
mongodb+srv://hashim_db_user:Password123!@clusterh.1k0zic7.mongodb.net/middaymate?appName=ClusterH
```

- **Username**: `hashim_db_user`
- **Password**: `Password123!` (handle special chars with URL encoding if needed)
- **Cluster**: `clusterh.1k0zic7.mongodb.net`
- **Database**: `middaymate`
- **SRV**: Requires MongoDB Atlas cluster (fully managed)

## Next Steps

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables** (already in .env.example):
   ```bash
   export MONGO_URI="mongodb+srv://hashim_db_user:Password123!@clusterh.1k0zic7.mongodb.net/middaymate?appName=ClusterH"
   export SECRET_KEY="your-secret-key"
   ```

3. **Test locally**:
   ```bash
   python run.py
   # or
   docker-compose up
   ```

4. **Update GitHub Actions Secrets** with:
   - `MONGO_URI` = Your MongoDB connection string

5. **Update Azure Container App** environment variables with:
   - `MONGO_URI` = Your MongoDB connection string

## Removed Features

- SQLite support (no fallback to SQLite)
- In-memory SQLite for testing (use real MongoDB for tests)
- Flask-SQLAlchemy session management

## Notes

- All document IDs are automatically generated by MongoDB (ObjectId)
- MongoEngine handles type validation and conversion
- Indexes are defined in model `meta` class for performance
- ReferenceFields maintain referential integrity
- Collections are created automatically on first write
