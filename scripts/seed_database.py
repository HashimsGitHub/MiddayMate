#!/usr/bin/env python
"""Seed database with dummy data for prototyping"""

import os
import sys
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import User, Venue, Promotion

def seed_database():
    """Populate database with dummy data"""
    app = create_app('development')

    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        print("✓ Database cleared and recreated")

        # Create dummy users
        users = [
            User(
                name='Sarah Johnson',
                email='sarah.johnson@dxc.com',
                role='user',
                availability_status='available'
            ),
            User(
                name='Michael Chen',
                email='michael.chen@dxc.com',
                role='user',
                availability_status='available'
            ),
            User(
                name='Emily Rodriguez',
                email='emily.rodriguez@dxc.com',
                role='user',
                availability_status='busy'
            ),
            User(
                name='James Thompson',
                email='james.thompson@techcorp.com',
                role='user',
                availability_status='available'
            ),
            User(
                name='Lisa Wang',
                email='lisa.wang@financeplus.com',
                role='user',
                availability_status='away'
            ),
            User(
                name='David Kumar',
                email='david.kumar@consulting.com',
                role='user',
                availability_status='available'
            ),
        ]
        db.session.add_all(users)
        db.session.commit()
        print("✓ Created 6 dummy users")

        # Create dummy venues
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
        db.session.commit()
        print("✓ Created 8 dummy venues")

        # Create dummy promotions
        promotions = [
            Promotion(
                venue_id=1,
                title='Happy Hour Coffee Special',
                description='20% off all espresso-based drinks from 2-4 PM',
                discount_percentage=20,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
            Promotion(
                venue_id=1,
                title='Free Pastry with Coffee',
                description='Buy any coffee, get a free pastry (up to \ value)',
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=14)
            ),
            Promotion(
                venue_id=2,
                title='Lunch Combo Deal',
                description='Get a bowl + drink + dessert for \',
                discount_percentage=35,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=60)
            ),
            Promotion(
                venue_id=2,
                title='CBD Workers Special',
                description='10% off with work ID for all lunch items',
                discount_percentage=10,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=90)
            ),
            Promotion(
                venue_id=3,
                title='Corporate Meeting Packages',
                description='Private meeting room + catering from \',
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=120)
            ),
            Promotion(
                venue_id=4,
                title='Afternoon Tea Promo',
                description='Elegant afternoon tea service, normally \, now \',
                discount_percentage=29,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=45)
            ),
            Promotion(
                venue_id=5,
                title='Happy Hour Cocktails',
                description='Buy 1 cocktail, get 2nd at 50% off (4-6 PM)',
                discount_percentage=50,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
            Promotion(
                venue_id=6,
                title='Organic Breakfast Bundle',
                description='Breakfast + fresh juice + smoothie for \',
                discount_percentage=22,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
            Promotion(
                venue_id=7,
                title='Executive Lounge Trial',
                description='Free day pass to the lounge with any purchase over \',
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=60)
            ),
            Promotion(
                venue_id=8,
                title='Chai Lovers Festival',
                description='25% off all chai varieties this month',
                discount_percentage=25,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
        ]
        db.session.add_all(promotions)
        db.session.commit()
        print("✓ Created 10 dummy promotions")

        print("\n" + "="*50)
        print("✅ Database seeding complete!")
        print("="*50)
        print("\nDemo Users:")
        print("  • Sarah Johnson")
        print("  • Michael Chen") 
        print("  • Emily Rodriguez")
        print("\n8 Venues with active promotions ready for demo!")

if __name__ == '__main__':
    seed_database()
