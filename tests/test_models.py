"""Tests for database models."""
import pytest
from app import create_app, db
from app.models import User, Venue, Vendor, Promotion, Invitation, Message

@pytest.fixture
def app():
    """Create and configure a test app."""
    app = create_app('testing')

    with app.app_context():
        yield app

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
            user.save()

            fetched = User.objects(email='test@example.com').first()
            assert fetched is not None
            assert fetched.name == 'Test User'

            user.delete()

    def test_user_to_dict(self, app):
        """Test user serialization."""
        with app.app_context():
            user = User(
                oauth_id='test123',
                oauth_provider='google',
                email='test@example.com',
                name='Test User'
            )
            user.save()

            user_dict = user.to_dict()
            assert user_dict['name'] == 'Test User'
            assert user_dict['email'] == 'test@example.com'

            user.delete()

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
            vendor.save()

            venue = Venue(
                name='Test Cafe',
                address='123 Main St',
                latitude=-33.8688,
                longitude=151.2093,
                vendor_id=vendor
            )
            venue.save()

            fetched = Venue.objects(name='Test Cafe').first()
            assert fetched is not None
            assert fetched.vendor_id.id == vendor.id

            venue.delete()
            vendor.delete()

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
            user1.save()

            user2 = User(
                oauth_id='user2',
                oauth_provider='google',
                email='user2@example.com',
                name='User 2'
            )
            user2.save()

            vendor = Vendor(
                name='John',
                email='john@example.com',
                company_name='Coffee Co',
                address='123 Main St'
            )
            vendor.save()

            venue = Venue(
                name='Test Cafe',
                address='123 Main St',
                latitude=-33.8688,
                longitude=151.2093,
                vendor_id=vendor
            )
            venue.save()

            invitation = Invitation(
                sender_id=user1,
                recipient_id=user2,
                venue_id=venue,
                message='Want to grab coffee?'
            )
            invitation.save()

            fetched = Invitation.objects(venue_id=venue).first()
            assert fetched is not None
            assert fetched.sender_id.id == user1.id
            assert fetched.recipient_id.id == user2.id

            invitation.delete()
            venue.delete()
            vendor.delete()
            user1.delete()
            user2.delete()
