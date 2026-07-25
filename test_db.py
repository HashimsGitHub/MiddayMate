#!/usr/bin/env python
"""Test database CRUD operations"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User, Venue, Promotion

def test_database():
    app = create_app('development')

    with app.app_context():
        print("=" * 70)
        print("DATABASE DIAGNOSTIC & CRUD TEST")
        print("=" * 70)

        # Check database file
        db_path = os.path.join(os.getcwd(), 'instance', 'middaymate.db')
        print(f"\n📁 Database Path: {db_path}")
        if os.path.exists(db_path):
            size = os.path.getsize(db_path)
            print(f"   ✓ Database file exists ({size} bytes)")
        else:
            print(f"   ✗ Database file NOT found")

        print("\n" + "=" * 70)
        print("CURRENT DATA IN TABLES")
        print("=" * 70)

        # Count records
        user_count = User.query.count()
        venue_count = Venue.query.count()
        promo_count = Promotion.query.count()

        print(f"\n👥 Users: {user_count} records")
        users = User.query.all()
        for user in users[:5]:
            print(f"   • {user.name} ({user.email})")

        print(f"\n🏢 Venues: {venue_count} records")
        venues = Venue.query.all()
        for venue in venues[:8]:
            print(f"   • {venue.name}")

        print(f"\n🎁 Promotions: {promo_count} records")
        promos = Promotion.query.all()
        for promo in promos[:5]:
            print(f"   • {promo.title}")

        # If no venues, try seeding
        if venue_count == 0:
            print("\n" + "=" * 70)
            print("NO VENUES FOUND - SEEDING DATABASE")
            print("=" * 70)

            seed_data()

            # Check again
            new_venue_count = Venue.query.count()
            print(f"\n✓ After seeding: {new_venue_count} venues")

        # Test CRUD
        print("\n" + "=" * 70)
        print("TESTING CRUD OPERATIONS")
        print("=" * 70)

        # CREATE
        print("\n[CREATE] Adding test venue...")
        test_venue = Venue(
            name='Test Cafe',
            address='123 Test Street',
            latitude=0.0,
            longitude=0.0,
            description='Test venue for CRUD'
        )
        db.session.add(test_venue)
        db.session.commit()
        print(f"✓ Created: {test_venue.name} (ID: {test_venue.id})")

        # READ
        print("\n[READ] Reading test venue...")
        found = Venue.query.filter_by(name='Test Cafe').first()
        if found:
            print(f"✓ Found: {found.name} - {found.description}")
        else:
            print("✗ Not found!")

        # UPDATE
        print("\n[UPDATE] Updating test venue...")
        found.description = 'Updated via CRUD test'
        db.session.commit()
        print(f"✓ Updated: {found.description}")

        # DELETE
        print("\n[DELETE] Deleting test venue...")
        db.session.delete(found)
        db.session.commit()
        print("✓ Deleted test venue")

        # Test API
        print("\n" + "=" * 70)
        print("TESTING API ENDPOINT")
        print("=" * 70)

        with app.test_client() as client:
            print("\nGET /api/venues")
            response = client.get('/api/venues')
            print(f"Status Code: {response.status_code}")

            data = response.get_json()
            if isinstance(data, list):
                print(f"Response: List with {len(data)} venues")
                if len(data) > 0:
                    print(f"Sample: {data[0].get('name', 'N/A')}")
            else:
                print(f"Response Type: {type(data)}")
                print(f"Content: {str(data)[:200]}")

        print("\n" + "=" * 70)
        print("✓ DIAGNOSTIC COMPLETE")
        print("=" * 70)

def seed_data():
    """Seed database with sample data"""
    from datetime import datetime, timedelta
    from app import db

    app = create_app('development')
    with app.app_context():
        # Create venues
        venues = [
            Venue(
                name='The Espresso Bar',
                address='Level 5, 123 King Street, Sydney CBD',
                latitude=-33.8688,
                longitude=151.2093,
                description='Premium espresso bar with specialty coffee and fresh pastries'
            ),
            Venue(
                name='Urban Lunch Co',
                address='Shop 2, 456 Pitt Street, Sydney CBD',
                latitude=-33.8701,
                longitude=151.2087,
                description='Modern lunch spot with healthy bowls and wraps'
            ),
            Venue(
                name='The Boardroom Cafe',
                address='Level 12, 789 George Street, Sydney CBD',
                latitude=-33.8674,
                longitude=151.2099,
                description='Corporate cafe with premium WiFi and meeting spaces'
            ),
            Venue(
                name='Market Street Bistro',
                address='101 Market Street, Sydney CBD',
                latitude=-33.8685,
                longitude=151.2072,
                description='French-inspired bistro perfect for business lunches'
            ),
            Venue(
                name='Chase Bar & Kitchen',
                address='Level 2, 321 Clarence Street, Sydney CBD',
                latitude=-33.8695,
                longitude=151.2055,
                description='Contemporary bar and kitchen with craft cocktails'
            ),
            Venue(
                name='Green Leaf Organic Cafe',
                address='34 Martin Place, Sydney CBD',
                latitude=-33.8650,
                longitude=151.2112,
                description='Farm-to-table cafe with organic ingredients'
            ),
            Venue(
                name='The Meeting Room',
                address='Ground Floor, 654 Bourke Street, Sydney CBD',
                latitude=-33.8776,
                longitude=151.2060,
                description='Exclusive lounge for professionals with premium seating'
            ),
            Venue(
                name='Chai & Co',
                address='125 Castlereagh Street, Sydney CBD',
                latitude=-33.8705,
                longitude=151.2110,
                description='Trendy chai bar with Asian fusion snacks'
            ),
        ]
        db.session.add_all(venues)
        db.session.flush()

        # Create promotions
        promotions = [
            Promotion(
                venue_id=venues[0].id,
                title='Happy Hour Coffee Special',
                description='20% off all espresso-based drinks from 2-4 PM',
                discount_percentage=20,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
            Promotion(
                venue_id=venues[1].id,
                title='Lunch Combo Deal',
                description='Get a bowl + drink + dessert for $15',
                discount_percentage=35,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=60)
            ),
            Promotion(
                venue_id=venues[4].id,
                title='Happy Hour Cocktails',
                description='Buy 1 cocktail, get 2nd at 50% off (4-6 PM)',
                discount_percentage=50,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
        ]
        db.session.add_all(promotions)
        db.session.commit()

        print(f"✓ Seeded {len(venues)} venues and {len(promotions)} promotions")

if __name__ == '__main__':
    test_database()
