from app import db
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

class User(db.Model):
    """User model for professionals and admins."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    oauth_id = db.Column(db.String(255), unique=True, nullable=False)
    oauth_provider = db.Column(db.String(50), nullable=False)  # 'microsoft' or 'google'
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default=UserRole.PROFESSIONAL)
    availability_status = db.Column(db.String(50), default=AvailabilityStatus.AWAY)
    profile_image_url = db.Column(db.String(500), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    social_media_links = db.Column(db.JSON, nullable=True)  # {'linkedin': '', 'twitter': ''}
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    sent_invitations = db.relationship('Invitation', foreign_keys='Invitation.sender_id', backref='sender')
    received_invitations = db.relationship('Invitation', foreign_keys='Invitation.recipient_id', backref='recipient')
    messages = db.relationship('Message', backref='user', lazy='dynamic')
    favorite_venues = db.relationship('Venue', secondary='user_favorites', backref='favorited_by')

    def to_dict(self):
        """Convert user to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'availability_status': self.availability_status,
            'profile_image_url': self.profile_image_url,
            'bio': self.bio,
            'created_at': self.created_at.isoformat(),
        }

class Venue(db.Model):
    """Venue model for cafés and restaurants."""
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    website = db.Column(db.String(500), nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    promotions = db.relationship('Promotion', backref='venue', lazy='dynamic', cascade='all, delete-orphan')
    invitations = db.relationship('Invitation', backref='venue', lazy='dynamic')

    def to_dict(self):
        """Convert venue to dictionary."""
        return {
            'id': self.id,
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

class Vendor(db.Model):
    """Vendor model for business owners."""
    __tablename__ = 'vendors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    company_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    venues = db.relationship('Venue', backref='vendor', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self):
        """Convert vendor to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'company_name': self.company_name,
            'is_approved': self.is_approved,
            'created_at': self.created_at.isoformat(),
        }

class Promotion(db.Model):
    """Promotion model for venue offers."""
    __tablename__ = 'promotions'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    discount_percentage = db.Column(db.Integer, nullable=True)
    discount_amount = db.Column(db.Float, nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convert promotion to dictionary."""
        return {
            'id': self.id,
            'venue_id': self.venue_id,
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

class Invitation(db.Model):
    """Invitation model for meetup requests."""
    __tablename__ = 'invitations'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    status = db.Column(db.String(50), default=InvitationStatus.PENDING)
    message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convert invitation to dictionary."""
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'recipient_id': self.recipient_id,
            'venue_id': self.venue_id,
            'status': self.status,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
        }

class Message(db.Model):
    """Message model for conversations."""
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    invitation_id = db.Column(db.Integer, db.ForeignKey('invitations.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    invitation = db.relationship('Invitation', backref='messages')

    def to_dict(self):
        """Convert message to dictionary."""
        return {
            'id': self.id,
            'invitation_id': self.invitation_id,
            'sender_id': self.sender_id,
            'content': self.content,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat(),
        }

# Association table for user favorites
user_favorites = db.Table(
    'user_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('venue_id', db.Integer, db.ForeignKey('venues.id'))
)
