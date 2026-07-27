from flask import Blueprint, request, jsonify, session
from app.models import Vendor, Venue, Promotion, UserRole, User
from app.utils.azure_storage import upload_image_to_azure
from datetime import datetime

bp = Blueprint('vendors', __name__, url_prefix='/api/vendors')

@bp.route('', methods=['POST'])
def register_vendor():
    """Register a new vendor."""
    data = request.get_json()

    required_fields = ['name', 'email', 'company_name', 'address']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    if Vendor.objects(email=data['email']).first():
        return jsonify({'error': 'Vendor with this email already exists'}), 409

    vendor = Vendor(
        name=data['name'],
        email=data['email'],
        company_name=data['company_name'],
        address=data['address'],
        phone=data.get('phone')
    )
    vendor.save()

    return jsonify({
        'message': 'Vendor registration successful, awaiting approval',
        'vendor': vendor.to_dict()
    }), 201

@bp.route('/<vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    """Get vendor details."""
    vendor = Vendor.objects(id=vendor_id).first()
    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    return jsonify(vendor.to_dict()), 200

@bp.route('/<vendor_id>/venues', methods=['GET'])
def get_vendor_venues(vendor_id):
    """Get venues for a vendor."""
    vendor = Vendor.objects(id=vendor_id).first()
    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    venues = list(Venue.objects(vendor_id=vendor))
    return jsonify([v.to_dict() for v in venues]), 200

@bp.route('/<vendor_id>/promotions', methods=['POST'])
def create_promotion(vendor_id):
    """Create a promotion for vendor's venue."""
    data = request.get_json()

    required_fields = ['venue_id', 'title', 'description', 'start_date', 'end_date']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    vendor = Vendor.objects(id=vendor_id).first()
    venue = Venue.objects(id=data['venue_id']).first()

    if not vendor or not venue:
        return jsonify({'error': 'Vendor or venue not found'}), 404

    if str(venue.vendor_id.id) != vendor_id:
        return jsonify({'error': 'Venue not found or unauthorized'}), 404

    try:
        promotion = Promotion(
            venue_id=venue,
            title=data['title'],
            description=data['description'],
            discount_percentage=data.get('discount_percentage'),
            discount_amount=data.get('discount_amount'),
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date']),
            image_url=data.get('image_url'),
            is_featured=data.get('is_featured', False)
        )
        promotion.save()

        return jsonify({
            'message': 'Promotion created',
            'promotion': promotion.to_dict()
        }), 201

    except ValueError as e:
        return jsonify({'error': f'Invalid date format: {str(e)}'}), 400

@bp.route('/<vendor_id>/promotions/<promotion_id>', methods=['PUT'])
def update_promotion(vendor_id, promotion_id):
    """Update a promotion."""
    promotion = Promotion.objects(id=promotion_id).first()
    vendor = Vendor.objects(id=vendor_id).first()

    if not promotion or not vendor:
        return jsonify({'error': 'Promotion or vendor not found'}), 404

    if str(promotion.venue_id.vendor_id.id) != vendor_id:
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

    promotion.save()

    return jsonify({
        'message': 'Promotion updated',
        'promotion': promotion.to_dict()
    }), 200

@bp.route('/<vendor_id>/upload-image', methods=['POST'])
def upload_vendor_image(vendor_id):
    """Upload vendor profile image."""
    vendor = Vendor.objects(id=vendor_id).first()
    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']

    try:
        image_url = upload_image_to_azure(file, folder='vendors')
        vendor.image_url = image_url
        vendor.save()

        return jsonify({
            'message': 'Image uploaded successfully',
            'image_url': image_url,
            'vendor': vendor.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<vendor_id>', methods=['PUT'])
def update_vendor(vendor_id):
    """Update vendor profile."""
    vendor = Vendor.objects(id=vendor_id).first()
    if not vendor:
        return jsonify({'error': 'Vendor not found'}), 404

    data = request.get_json()

    if 'name' in data:
        vendor.name = data['name']
    if 'address' in data:
        vendor.address = data['address']
    if 'description' in data:
        vendor.description = data['description']
    if 'phone' in data:
        vendor.phone = data['phone']
    if 'website' in data:
        vendor.website = data['website']

    vendor.save()

    return jsonify({
        'message': 'Vendor profile updated',
        'vendor': vendor.to_dict()
    }), 200
