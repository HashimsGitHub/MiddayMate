"""Tests for API routes."""
import pytest
from app import create_app, db
from app.models import User, Venue, Vendor

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

class TestAuthRoutes:
    """Test authentication routes."""

    def test_login(self, client):
        """Test user login."""
        response = client.post('/api/auth/login', json={
            'oauth_provider': 'google',
            'oauth_id': 'test123',
            'email': 'test@example.com',
            'name': 'Test User'
        })

        assert response.status_code == 200
        assert 'user' in response.get_json()

    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get('/health')

        assert response.status_code == 200
        assert response.get_json()['status'] == 'healthy'

class TestVenueRoutes:
    """Test venue routes."""

    def test_get_venues(self, client, app):
        """Test getting venues."""
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

        response = client.get('/api/venues')

        assert response.status_code == 200
        venues = response.get_json()
        assert len(venues) > 0
        assert venues[0]['name'] == 'Test Cafe'
