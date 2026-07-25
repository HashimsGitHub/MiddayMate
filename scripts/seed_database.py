"""Database seeding script for development."""
import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import User, Vendor, Venue, Promotion, AvailabilityStatus, UserRole

def seed_database():
    """Seed the database with example data."""
    app = create_app('development')

    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create sample users
        users = [
            User(
                oauth_id='user1',
                oauth_provider='google',
                email='alice@example.com',
                name='Alice Johnson',
                role=UserRole.PROFESSIONAL,
                availability_status=AvailabilityStatus.AVAILABLE,
                bio='Marketing manager looking to network'
            ),
            User(
                oauth_id='user2',
                oauth_provider='microsoft',
                email='bob@example.com',
                name='Bob Smith',
                role=UserRole.PROFESSIONAL,
                availability_status=AvailabilityStatus.BUSY,
                bio='Software engineer in CBD'
            ),
            User(
                oauth_id='user3',
                oauth_provider='google',
                email='charlie@example.com',
                name='Charlie Brown',
                role=UserRole.PROFESSIONAL,
                availability_status=AvailabilityStatus.AVAILABLE,
                bio='Financial analyst'
            ),
        ]

        db.session.add_all(users)
        db.session.commit()

        # Create sample vendors
        vendors = [
            Vendor(
                name='John Smith',
                email='john@coffeedreams.com',
                phone='0412345678',
                company_name='Coffee Dreams',
                address='123 Martin Place, Sydney NSW 2000',
                is_approved=True
            ),
            Vendor(
                name='Sarah Lee',
                email='sarah@quickbite.com',
                phone='0412345679',
                company_name='QuickBite Cafe',
                address='456 George Street, Sydney NSW 2000',
                is_approved=True
            ),
            Vendor(
                name='Mike Johnson',
                email='mike@urbanfeast.com',
                phone='0412345680',
                company_name='Urban Feast',
                address='789 Pitt Street, Sydney NSW 2000',
                is_approved=False
            ),
        ]

        db.session.add_all(vendors)
        db.session.commit()

        # Create sample venues
        venues = [
            Venue(
                name='Coffee Dreams',
                address='123 Martin Place, Sydney NSW 2000',
                latitude=-33.8688,
                longitude=151.2093,
                description='Premium coffee and pastries in the heart of CBD',
                phone='0212345678',
                website='www.coffeedreams.com',
                vendor_id=vendors[0].id
            ),
            Venue(
                name='QuickBite Cafe',
                address='456 George Street, Sydney NSW 2000',
                latitude=-33.8648,
                longitude=151.2107,
                description='Fast casual dining with healthy options',
                phone='0212345679',
                website='www.quickbite.com',
                vendor_id=vendors[1].id
            ),
            Venue(
                name='Urban Feast',
                address='789 Pitt Street, Sydney NSW 2000',
                latitude=-33.8705,
                longitude=151.2129,
                description='Modern restaurant with international cuisine',
                phone='0212345680',
                website='www.urbanfeast.com',
                vendor_id=vendors[2].id
            ),
        ]

        db.session.add_all(venues)
        db.session.commit()

        # Create sample promotions
        now = datetime.utcnow()
        promotions = [
            Promotion(
                venue_id=venues[0].id,
                title='Happy Hour Coffee - 20% Off',
                description='All coffee drinks 20% off between 3-5 PM',
                discount_percentage=20,
                start_date=now,
                end_date=now + timedelta(days=30),
                is_featured=True
            ),
            Promotion(
                venue_id=venues[0].id,
                title='Free Pastry with Purchase',
                description='Buy any coffee, get a free pastry',
                discount_amount=5.00,
                start_date=now,
                end_date=now + timedelta(days=14),
                is_featured=False
            ),
            Promotion(
                venue_id=venues[1].id,
                title='Lunch Special - $12 Meal Deal',
                description='Salad, sandwich, and drink combo',
                discount_percentage=15,
                start_date=now,
                end_date=now + timedelta(days=60),
                is_featured=True
            ),
            Promotion(
                venue_id=venues[2].id,
                title='Grand Opening - Buy One Get One 50% Off',
                description='50% off second item on all menu items',
                discount_percentage=50,
                start_date=now,
                end_date=now + timedelta(days=21),
                is_featured=True
            ),
        ]

        db.session.add_all(promotions)
        db.session.commit()

        print("✅ Database seeded successfully!")
        print(f"  - Created {len(users)} users")
        print(f"  - Created {len(vendors)} vendors")
        print(f"  - Created {len(venues)} venues")
        print(f"  - Created {len(promotions)} promotions")

if __name__ == '__main__':
    seed_database()
