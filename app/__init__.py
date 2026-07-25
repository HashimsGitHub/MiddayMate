from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app(config_name='development'):
    """Application factory pattern."""
    # Get the root path for static files
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_path = os.path.join(root_path, 'frontend', 'dist')

    app = Flask(__name__, static_folder=static_path, static_url_path='')

    # Load configuration
    if config_name == 'production':
        from app.config import ProductionConfig as config
    elif config_name == 'testing':
        from app.config import TestingConfig as config
    else:
        from app.config import DevelopmentConfig as config

    app.config.from_object(config)

    # Initialize extensions
    db.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes import auth, users, venues, promotions, invitations, messages, vendors, seed

    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(venues.bp)
    app.register_blueprint(promotions.bp)
    app.register_blueprint(invitations.bp)
    app.register_blueprint(messages.bp)
    app.register_blueprint(vendors.bp)
    app.register_blueprint(seed.bp)

    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return {'status': 'healthy'}, 200

    # Serve React app
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react(path):
        index_path = os.path.join(static_path, 'index.html')
        if path and os.path.exists(os.path.join(static_path, path)):
            return send_from_directory(static_path, path)
        elif os.path.exists(index_path):
            return send_from_directory(static_path, 'index.html')
        else:
            return {'error': 'React app not built. Run "npm run build"'}, 404

    # Create tables and seed if needed
    with app.app_context():
        db.create_all()

        # Auto-seed if no venues exist
        from app.models import Venue
        if Venue.query.count() == 0:
            seed_initial_data()

    return app


def seed_initial_data():
    """Initialize database with sample data"""
    from datetime import datetime, timedelta
    from app.models import User, Venue, Promotion

    print("Seeding database with initial data...")

    # Create users
    users = [
        User(name='Sarah Johnson', email='sarah.johnson@dxc.com', role='user', availability_status='available'),
        User(name='Jake Thompson', email='jake.thompson@techcorp.com', role='user', availability_status='available'),
        User(name='Michael Chen', email='michael.chen@dxc.com', role='user', availability_status='available'),
        User(name='Emily Rodriguez', email='emily.rodriguez@dxc.com', role='user', availability_status='busy'),
        User(name='Lisa Wang', email='lisa.wang@financeplus.com', role='user', availability_status='away'),
        User(name='David Kumar', email='david.kumar@consulting.com', role='user', availability_status='available'),
    ]
    db.session.add_all(users)
    db.session.flush()

    # Create venues
    venues = [
        Venue(name='The Espresso Bar', address='Level 5, 123 King Street, Sydney CBD',
              latitude=-33.8688, longitude=151.2093, description='Premium espresso bar with specialty coffee and fresh pastries'),
        Venue(name='Urban Lunch Co', address='Shop 2, 456 Pitt Street, Sydney CBD',
              latitude=-33.8701, longitude=151.2087, description='Modern lunch spot with healthy bowls and wraps'),
        Venue(name='The Boardroom Cafe', address='Level 12, 789 George Street, Sydney CBD',
              latitude=-33.8674, longitude=151.2099, description='Corporate cafe with premium WiFi and meeting spaces'),
        Venue(name='Market Street Bistro', address='101 Market Street, Sydney CBD',
              latitude=-33.8685, longitude=151.2072, description='French-inspired bistro perfect for business lunches'),
        Venue(name='Chase Bar & Kitchen', address='Level 2, 321 Clarence Street, Sydney CBD',
              latitude=-33.8695, longitude=151.2055, description='Contemporary bar and kitchen with craft cocktails'),
        Venue(name='Green Leaf Organic Cafe', address='34 Martin Place, Sydney CBD',
              latitude=-33.8650, longitude=151.2112, description='Farm-to-table cafe with organic ingredients'),
        Venue(name='The Meeting Room', address='Ground Floor, 654 Bourke Street, Sydney CBD',
              latitude=-33.8776, longitude=151.2060, description='Exclusive lounge for professionals with premium seating'),
        Venue(name='Chai & Co', address='125 Castlereagh Street, Sydney CBD',
              latitude=-33.8705, longitude=151.2110, description='Trendy chai bar with Asian fusion snacks'),
    ]
    db.session.add_all(venues)
    db.session.flush()

    # Create promotions
    promotions = [
        Promotion(venue_id=venues[0].id, title='Happy Hour Coffee Special',
                 description='20% off all espresso-based drinks from 2-4 PM', discount_percentage=20,
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=30)),
        Promotion(venue_id=venues[0].id, title='Free Pastry with Coffee',
                 description='Buy any coffee, get a free pastry (up to $8 value)',
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=14)),
        Promotion(venue_id=venues[1].id, title='Lunch Combo Deal',
                 description='Get a bowl + drink + dessert for $15', discount_percentage=35,
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=60)),
        Promotion(venue_id=venues[1].id, title='CBD Workers Special',
                 description='10% off with work ID for all lunch items', discount_percentage=10,
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=90)),
        Promotion(venue_id=venues[2].id, title='Corporate Meeting Packages',
                 description='Private meeting room + catering from $200',
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=120)),
        Promotion(venue_id=venues[3].id, title='Afternoon Tea Promo',
                 description='Elegant afternoon tea service, normally $35, now $25', discount_percentage=29,
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=45)),
        Promotion(venue_id=venues[4].id, title='Happy Hour Cocktails',
                 description='Buy 1 cocktail, get 2nd at 50% off (4-6 PM)', discount_percentage=50,
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=30)),
        Promotion(venue_id=venues[5].id, title='Organic Breakfast Bundle',
                 description='Breakfast + fresh juice + smoothie for $18', discount_percentage=22,
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=30)),
        Promotion(venue_id=venues[6].id, title='Executive Lounge Trial',
                 description='Free day pass to the lounge with any purchase over $50',
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=60)),
        Promotion(venue_id=venues[7].id, title='Chai Lovers Festival',
                 description='25% off all chai varieties this month', discount_percentage=25,
                 start_date=datetime.now(), end_date=datetime.now() + timedelta(days=30)),
    ]
    db.session.add_all(promotions)
    db.session.commit()

    print(f"✓ Seeded {len(users)} users, {len(venues)} venues, {len(promotions)} promotions")
