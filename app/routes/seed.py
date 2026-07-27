from flask import Blueprint, jsonify
from datetime import datetime, timedelta
from app.models import User, Venue, Promotion, Vendor

bp = Blueprint('seed', __name__, url_prefix='/api/seed')

@bp.route('/populate', methods=['POST'])
def populate_database():
    """Populate database with demo data"""
    try:
        Promotion.drop_collection()
        Venue.drop_collection()
        User.drop_collection()
        Vendor.drop_collection()

        users = [
            User(
                name='Sarah Johnson',
                email='sarah.johnson@dxc.com',
                oauth_id='sarah_johnson_123',
                oauth_provider='microsoft',
                role='professional',
                availability_status='available'
            ),
            User(
                name='Jake Thompson',
                email='jake.thompson@techcorp.com',
                oauth_id='jake_thompson_123',
                oauth_provider='google',
                role='professional',
                availability_status='available'
            ),
            User(
                name='Michael Chen',
                email='michael.chen@dxc.com',
                oauth_id='michael_chen_123',
                oauth_provider='microsoft',
                role='professional',
                availability_status='available'
            ),
            User(
                name='Emily Rodriguez',
                email='emily.rodriguez@dxc.com',
                oauth_id='emily_rodriguez_123',
                oauth_provider='google',
                role='professional',
                availability_status='busy'
            ),
            User(
                name='Lisa Wang',
                email='lisa.wang@financeplus.com',
                oauth_id='lisa_wang_123',
                oauth_provider='microsoft',
                role='professional',
                availability_status='away'
            ),
            User(
                name='David Kumar',
                email='david.kumar@consulting.com',
                oauth_id='david_kumar_123',
                oauth_provider='google',
                role='professional',
                availability_status='available'
            ),
        ]
        for user in users:
            user.save()

        vendor = Vendor(
            name='Hospitality Group',
            email='vendor@hospitality.com',
            company_name='Hospitality Group',
            address='Sydney CBD',
            is_approved=True
        )
        vendor.save()

        venues = [
            Venue(
                name='The Espresso Bar',
                address='Level 5, 123 King Street, Sydney CBD',
                latitude=-33.8688,
                longitude=151.2093,
                description='Premium espresso bar with specialty coffee and fresh pastries',
                vendor_id=vendor
            ),
            Venue(
                name='Urban Lunch Co',
                address='Shop 2, 456 Pitt Street, Sydney CBD',
                latitude=-33.8701,
                longitude=151.2087,
                description='Modern lunch spot with healthy bowls and wraps',
                vendor_id=vendor
            ),
            Venue(
                name='The Boardroom Cafe',
                address='Level 12, 789 George Street, Sydney CBD',
                latitude=-33.8674,
                longitude=151.2099,
                description='Corporate cafe with premium WiFi and meeting spaces',
                vendor_id=vendor
            ),
            Venue(
                name='Market Street Bistro',
                address='101 Market Street, Sydney CBD',
                latitude=-33.8685,
                longitude=151.2072,
                description='French-inspired bistro perfect for business lunches',
                vendor_id=vendor
            ),
            Venue(
                name='Chase Bar & Kitchen',
                address='Level 2, 321 Clarence Street, Sydney CBD',
                latitude=-33.8695,
                longitude=151.2055,
                description='Contemporary bar and kitchen with craft cocktails',
                vendor_id=vendor
            ),
            Venue(
                name='Green Leaf Organic Cafe',
                address='34 Martin Place, Sydney CBD',
                latitude=-33.8650,
                longitude=151.2112,
                description='Farm-to-table cafe with organic ingredients',
                vendor_id=vendor
            ),
            Venue(
                name='The Meeting Room',
                address='Ground Floor, 654 Bourke Street, Sydney CBD',
                latitude=-33.8776,
                longitude=151.2060,
                description='Exclusive lounge for professionals with premium seating',
                vendor_id=vendor
            ),
            Venue(
                name='Chai & Co',
                address='125 Castlereagh Street, Sydney CBD',
                latitude=-33.8705,
                longitude=151.2110,
                description='Trendy chai bar with Asian fusion snacks',
                vendor_id=vendor
            ),
        ]
        for venue in venues:
            venue.save()

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

        return jsonify({
            'success': True,
            'message': 'Database seeded successfully',
            'users': len(users),
            'venues': len(venues),
            'promotions': len(promotions)
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
