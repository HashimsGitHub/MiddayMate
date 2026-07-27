from mongoengine import Document, StringField, IntField, FloatField, BooleanField, DateTimeField, ListField, ReferenceField, EmailField, URLField, EmbeddedDocument, EmbeddedDocumentField
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    """User role enumeration."""
    PROFESSIONAL = 'professional'
    VENDOR = 'vendor'
    ADMIN = 'admin'

class AvailabilityStatus(str, Enum):
    """User availability status."""
    AVAILABLE = 'available'
    BUSY = 'busy'
    AWAY = 'away'

class InvitationStatus(str, Enum):
    """Invitation status."""
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    DECLINED = 'declined'
    CANCELLED = 'cancelled'

class SocialMediaLinks(EmbeddedDocument):
    """Embedded document for social media links."""
    linkedin = URLField(null=True)
    twitter = URLField(null=True)

class User(Document):
    """User document for professionals and admins."""
    oauth_id = StringField(unique=True, required=True)
    oauth_provider = StringField(required=True)
    email = EmailField(unique=True, required=True)
    name = StringField(required=True, max_length=255)
    role = StringField(default=UserRole.PROFESSIONAL, choices=[r.value for r in UserRole])
    availability_status = StringField(default=AvailabilityStatus.AWAY, choices=[s.value for s in AvailabilityStatus])
    profile_image_url = URLField(null=True)
    bio = StringField(null=True)
    social_media_links = EmbeddedDocumentField(SocialMediaLinks, null=True)
    favorite_venue_ids = ListField(ReferenceField('Venue'), default=list)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'users',
        'indexes': ['email', 'oauth_id', 'created_at']
    }

    def to_dict(self):
        """Convert user to dictionary."""
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'availability_status': self.availability_status,
            'profile_image_url': self.profile_image_url,
            'bio': self.bio,
            'created_at': self.created_at.isoformat(),
        }

class Venue(Document):
    """Venue document for cafés and restaurants."""
    name = StringField(required=True, max_length=255)
    address = StringField(required=True, max_length=500)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    description = StringField(null=True)
    phone = StringField(max_length=20, null=True)
    website = URLField(null=True)
    image_url = URLField(null=True)
    vendor_id = ReferenceField('Vendor', required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'venues',
        'indexes': ['vendor_id', 'created_at', ('latitude', 'longitude')]
    }

    def to_dict(self):
        """Convert venue to dictionary."""
        return {
            'id': str(self.id),
            'name': self.name,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'description': self.description,
            'phone': self.phone,
            'website': self.website,
            'image_url': self.image_url,
            'created_at': self.created_at.isoformat(),
        }

class Vendor(Document):
    """Vendor document for business owners."""
    name = StringField(required=True, max_length=255)
    email = EmailField(unique=True, required=True)
    phone = StringField(max_length=20, null=True)
    company_name = StringField(required=True, max_length=255)
    address = StringField(required=True, max_length=500)
    is_approved = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'vendors',
        'indexes': ['email', 'created_at']
    }

    def to_dict(self):
        """Convert vendor to dictionary."""
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'company_name': self.company_name,
            'is_approved': self.is_approved,
            'created_at': self.created_at.isoformat(),
        }

class Promotion(Document):
    """Promotion document for venue offers."""
    venue_id = ReferenceField('Venue', required=True)
    title = StringField(required=True, max_length=255)
    description = StringField(required=True)
    discount_percentage = IntField(null=True, min_value=0, max_value=100)
    discount_amount = FloatField(null=True)
    start_date = DateTimeField(required=True)
    end_date = DateTimeField(required=True)
    image_url = URLField(null=True)
    is_featured = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'promotions',
        'indexes': ['venue_id', 'start_date', 'end_date', 'created_at']
    }

    def to_dict(self):
        """Convert promotion to dictionary."""
        return {
            'id': str(self.id),
            'venue_id': str(self.venue_id.id) if self.venue_id else None,
            'title': self.title,
            'description': self.description,
            'discount_percentage': self.discount_percentage,
            'discount_amount': self.discount_amount,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'image_url': self.image_url,
            'is_featured': self.is_featured,
            'created_at': self.created_at.isoformat(),
        }

class Invitation(Document):
    """Invitation document for meetup requests."""
    sender_id = ReferenceField('User', required=True)
    recipient_id = ReferenceField('User', required=True)
    venue_id = ReferenceField('Venue', required=True)
    status = StringField(default=InvitationStatus.PENDING, choices=[s.value for s in InvitationStatus])
    message = StringField(null=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'invitations',
        'indexes': ['sender_id', 'recipient_id', 'venue_id', 'status', 'created_at']
    }

    def to_dict(self):
        """Convert invitation to dictionary."""
        return {
            'id': str(self.id),
            'sender_id': str(self.sender_id.id),
            'recipient_id': str(self.recipient_id.id),
            'venue_id': str(self.venue_id.id),
            'status': self.status,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
        }

class Message(Document):
    """Message document for conversations."""
    invitation_id = ReferenceField('Invitation', required=True)
    sender_id = ReferenceField('User', required=True)
    content = StringField(required=True)
    is_read = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'messages',
        'indexes': ['invitation_id', 'sender_id', 'created_at']
    }

    def to_dict(self):
        """Convert message to dictionary."""
        return {
            'id': str(self.id),
            'invitation_id': str(self.invitation_id.id),
            'sender_id': str(self.sender_id.id),
            'content': self.content,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat(),
        }
