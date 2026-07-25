"""Tests for database models."""
import pytest
from app import create_app, db
from app.models import User, Venue, Vendor, Promotion, Invitation, Message

@pytest.fixture
def app():
    """Create and configure a test app."""
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

class TestUserModel:
    """Test User model."""

    def test_user_creation(self, app):
        """Test creating a user."""
        with app.app_context():
            user = User(
                oauth_id='test123',
                oauth_provider='google',
                email='test@example.com',
                name='Test User'
            )
            db.session.add(user)
            db.session.commit()

            fetched = User.query.filter_by(email='test@example.com').first()
            assert fetched is not None
            assert fetched.name == 'Test User'

    def test_user_to_dict(self, app):
        """Test user serialization."""
        with app.app_context():
            user = User(
                oauth_id='test123',
                oauth_provider='google',
                email='test@example.com',
                name='Test User'
            )
            db.session.add(user)
            db.session.commit()

            user_dict = user.to_dict()
            assert user_dict['name'] == 'Test User'
            assert user_dict['email'] == 'test@example.com'

class TestVenueModel:
    """Test Venue model."""

    def test_venue_creation(self, app):
        """Test creating a venue."""
        with app.app_context():
            vendor = Vendor(
                name='John',
                email='john@example.com',
                company_name='Coffee Co',
                address='123 Main St'
            )
            db.session.add(vendor)
            db.session.commit()

            venue = Venue(
                name='Test Cafe',
                address='123 Main St',
                latitude=-33.8688,
                longitude=151.2093,
                vendor_id=vendor.id
            )
            db.session.add(venue)
            db.session.commit()

            fetched = Venue.query.filter_by(name='Test Cafe').first()
            assert fetched is not None
            assert fetched.vendor_id == vendor.id

class TestInvitationModel:
    """Test Invitation model."""

    def test_invitation_creation(self, app):
        """Test creating an invitation."""
        with app.app_context():
            user1 = User(
                oauth_id='user1',
                oauth_provider='google',
                email='user1@example.com',
                name='User 1'
            )
            user2 = User(
                oauth_id='user2',
                oauth_provider='google',
                email='user2@example.com',
                name='User 2'
            )
            db.session.add_all([user1, user2])
            db.session.commit()

            vendor = Vendor(
                name='John',
                email='john@example.com',
                company_name='Coffee Co',
                address='123 Main St'
            )
            db.session.add(vendor)
            db.session.commit()

            venue = Venue(
                name='Test Cafe',
                address='123 Main St',
                latitude=-33.8688,
                longitude=151.2093,
                vendor_id=vendor.id
            )
            db.session.add(venue)
            db.session.commit()

            invitation = Invitation(
                sender_id=user1.id,
                recipient_id=user2.id,
                venue_id=venue.id,
                message='Want to grab coffee?'
            )
            db.session.add(invitation)
            db.session.commit()

            fetched = Invitation.query.filter_by(venue_id=venue.id).first()
            assert fetched is not None
            assert fetched.sender_id == user1.id
            assert fetched.recipient_id == user2.id
