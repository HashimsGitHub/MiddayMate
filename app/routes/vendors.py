from flask import Blueprint, request, jsonify, session
from app.models import Vendor, Venue, Promotion, UserRole, User
from app import db
from datetime import datetime

bp = Blueprint('vendors', __name__, url_prefix='/api/vendors')

@bp.route('', methods=['POST'])
def register_vendor():
    """Register a new vendor."""
    data = request.get_json()

    required_fields = ['name', 'email', 'company_name', 'address']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if vendor already exists
    if Vendor.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Vendor with this email already exists'}), 409

    vendor = Vendor(
        name=data['name'],
        email=data['email'],
        company_name=data['company_name'],
        address=data['address'],
        phone=data.get('phone')
    )

    db.session.add(vendor)
    db.session.commit()

    return jsonify({
        'message': 'Vendor registration successful, awaiting approval',
        'vendor': vendor.to_dict()
    }), 201

@bp.route('/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    """Get vendor details."""
    vendor = Vendor.query.get(vendor_id)

    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    return jsonify(vendor.to_dict()), 200

@bp.route('/<int:vendor_id>/venues', methods=['GET'])
def get_vendor_venues(vendor_id):
    """Get venues for a vendor."""
    vendor = Vendor.query.get(vendor_id)

    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    venues = Venue.query.filter_by(vendor_id=vendor_id).all()
    return jsonify([v.to_dict() for v in venues]), 200

@bp.route('/<int:vendor_id>/promotions', methods=['POST'])
def create_promotion(vendor_id):
    """Create a promotion for vendor's venue."""
    # In a real app, verify vendor ownership
    data = request.get_json()

    required_fields = ['venue_id', 'title', 'description', 'start_date', 'end_date']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    venue = Venue.query.get(data['venue_id'])
    if not venue or venue.vendor_id != vendor_id:
        return jsonify({'error': 'Venue not found or unauthorized'}), 404

    try:
        promotion = Promotion(
            venue_id=data['venue_id'],
            title=data['title'],
            description=data['description'],
            discount_percentage=data.get('discount_percentage'),
            discount_amount=data.get('discount_amount'),
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date']),
            image_url=data.get('image_url'),
            is_featured=data.get('is_featured', False)
        )

        db.session.add(promotion)
        db.session.commit()

        return jsonify({
            'message': 'Promotion created',
            'promotion': promotion.to_dict()
        }), 201

    except ValueError as e:
        return jsonify({'error': f'Invalid date format: {str(e)}'}), 400

@bp.route('/<int:vendor_id>/promotions/<int:promotion_id>', methods=['PUT'])
def update_promotion(vendor_id, promotion_id):
    """Update a promotion."""
    promotion = Promotion.query.get(promotion_id)

    if not promotion:
        return jsonify({'error': 'Promotion not found'}), 404

    if promotion.venue.vendor_id != vendor_id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()

    if 'title' in data:
        promotion.title = data['title']
    if 'description' in data:
        promotion.description = data['description']
    if 'discount_percentage' in data:
        promotion.discount_percentage = data['discount_percentage']
    if 'discount_amount' in data:
        promotion.discount_amount = data['discount_amount']
    if 'is_featured' in data:
        promotion.is_featured = data['is_featured']

    db.session.commit()

    return jsonify({
        'message': 'Promotion updated',
        'promotion': promotion.to_dict()
    }), 200
