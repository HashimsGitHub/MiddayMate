#!/usr/bin/env python
"""Seed MongoDB database with venue and promotion data"""

import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.models import User, Venue, Vendor, Promotion

def seed_database():
    """Populate MongoDB with demo data"""
    app = create_app('development')

    with app.app_context():
        # Clear existing data
        User.drop_collection()
        Venue.drop_collection()
        Vendor.drop_collection()
        Promotion.drop_collection()
        print("✓ Database cleared")

        # Create vendor
        vendor = Vendor(
            name='Hospitality Group Sydney',
            email='venues@hospitalitygroup.com.au',
            company_name='Hospitality Group Sydney',
            address='Sydney CBD',
            is_approved=True
        )
        vendor.save()
        print("✓ Created vendor")

        # Create venues
        AZURE_IMAGE_BASE = 'https://middaymatesa.blob.core.windows.net/images'
        venues = [
            Venue(
                name='The Espresso Bar',
                address='Level 5, 123 King Street, Sydney CBD',
                latitude=-33.8688,
                longitude=151.2093,
                description='Premium espresso bar with specialty coffee and fresh pastries',
                vendor_id=vendor,
                phone='02-9999-0001',
                image_url=f'{AZURE_IMAGE_BASE}/The_Expresso_Bar.jpg'
            ),
            Venue(
                name='Urban Lunch Co',
                address='Shop 2, 456 Pitt Street, Sydney CBD',
                latitude=-33.8701,
                longitude=151.2087,
                description='Modern lunch spot with healthy bowls and wraps',
                vendor_id=vendor,
                phone='02-9999-0002',
                image_url=f'{AZURE_IMAGE_BASE}/Urban_Kitchen_and_Co.jpg'
            ),
            Venue(
                name='The Boardroom Cafe',
                address='Level 12, 789 George Street, Sydney CBD',
                latitude=-33.8674,
                longitude=151.2099,
                description='Corporate cafe with premium WiFi and meeting spaces',
                vendor_id=vendor,
                phone='02-9999-0003',
                image_url=f'{AZURE_IMAGE_BASE}/The_Boardroom_Gaming_Cafe.jpg'
            ),
            Venue(
                name='Market Street Bistro',
                address='101 Market Street, Sydney CBD',
                latitude=-33.8685,
                longitude=151.2072,
                description='French-inspired bistro perfect for business lunches',
                vendor_id=vendor,
                phone='02-9999-0004',
                image_url=f'{AZURE_IMAGE_BASE}/Market_Bistro.jpg'
            ),
            Venue(
                name='Chase Bar & Kitchen',
                address='Level 2, 321 Clarence Street, Sydney CBD',
                latitude=-33.8695,
                longitude=151.2055,
                description='Contemporary bar and kitchen with craft cocktails',
                vendor_id=vendor,
                phone='02-9999-0005',
                image_url=f'{AZURE_IMAGE_BASE}/Chase_Restaurant_and_Lounge.webp'
            ),
            Venue(
                name='Green Leaf Organic Cafe',
                address='34 Martin Place, Sydney CBD',
                latitude=-33.8650,
                longitude=151.2112,
                description='Farm-to-table cafe with organic ingredients',
                vendor_id=vendor,
                phone='02-9999-0006',
                image_url=f'{AZURE_IMAGE_BASE}/Green_Leaf_Cafe_and_Bar.jpg'
            ),
            Venue(
                name='The Meeting Room',
                address='Ground Floor, 654 Bourke Street, Sydney CBD',
                latitude=-33.8776,
                longitude=151.2060,
                description='Exclusive lounge for professionals with premium seating',
                vendor_id=vendor,
                phone='02-9999-0007',
                image_url=f'{AZURE_IMAGE_BASE}/The_Meeting_Place_Cafe.jpg'
            ),
            Venue(
                name='Chai & Co',
                address='125 Castlereagh Street, Sydney CBD',
                latitude=-33.8705,
                longitude=151.2110,
                description='Trendy chai bar with Asian fusion snacks',
                vendor_id=vendor,
                phone='02-9999-0008',
                image_url=f'{AZURE_IMAGE_BASE}/Chai_and_Co.jpg'
            ),
        ]
        for venue in venues:
            venue.save()
        print(f"✓ Created {len(venues)} venues")

        # Create promotions
        promotions = [
            Promotion(
                venue_id=venues[0],
                title='Happy Hour Coffee Special',
                description='20% off all espresso-based drinks from 2-4 PM',
                discount_percentage=20,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
            Promotion(
                venue_id=venues[0],
                title='Free Pastry with Coffee',
                description='Buy any coffee, get a free pastry (up to $8 value)',
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=14)
            ),
            Promotion(
                venue_id=venues[1],
                title='Lunch Combo Deal',
                description='Get a bowl + drink + dessert for $15',
                discount_percentage=35,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=60)
            ),
            Promotion(
                venue_id=venues[1],
                title='CBD Workers Special',
                description='10% off with work ID for all lunch items',
                discount_percentage=10,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=90)
            ),
            Promotion(
                venue_id=venues[2],
                title='Corporate Meeting Packages',
                description='Private meeting room + catering from $200',
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=120)
            ),
            Promotion(
                venue_id=venues[3],
                title='Afternoon Tea Promo',
                description='Elegant afternoon tea service, normally $35, now $25',
                discount_percentage=29,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=45)
            ),
            Promotion(
                venue_id=venues[4],
                title='Happy Hour Cocktails',
                description='Buy 1 cocktail, get 2nd at 50% off (4-6 PM)',
                discount_percentage=50,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
            Promotion(
                venue_id=venues[5],
                title='Organic Breakfast Bundle',
                description='Breakfast + fresh juice + smoothie for $18',
                discount_percentage=22,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
            Promotion(
                venue_id=venues[6],
                title='Executive Lounge Trial',
                description='Free day pass to the lounge with any purchase over $50',
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=60)
            ),
            Promotion(
                venue_id=venues[7],
                title='Chai Lovers Festival',
                description='25% off all chai varieties this month',
                discount_percentage=25,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30)
            ),
        ]
        for promotion in promotions:
            promotion.save()
        print(f"✓ Created {len(promotions)} promotions")

        print("\n" + "="*50)
        print("✅ Database seeding complete!")
        print("="*50)
        print(f"  Venues: {Venue.objects.count()}")
        print(f"  Promotions: {Promotion.objects.count()}")
        print(f"  Vendors: {Vendor.objects.count()}")

if __name__ == '__main__':
    try:
        seed_database()
    except Exception as e:
        print(f"❌ Seeding failed: {str(e)}")
        sys.exit(1)
