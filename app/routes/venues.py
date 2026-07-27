from flask import Blueprint, request, jsonify
from app.models import Venue, Vendor

bp = Blueprint('venues', __name__, url_prefix='/api/venues')

@bp.route('', methods=['GET'])
def get_venues():
    """Get venues and vendors as venue cards."""
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    radius = request.args.get('radius', type=float, default=5.0)

    # Get all venues
    venues = list(Venue.objects())
    venue_items = [v.to_dict() for v in venues]

    # Get approved vendors and convert to venue format
    vendors = list(Vendor.objects(is_approved=True))
    for vendor in vendors:
        vendor_item = {
            'id': str(vendor.id),
            'name': vendor.name,
            'address': vendor.address,
            'description': vendor.description or '',
            'phone': vendor.phone,
            'website': vendor.website,
            'image_url': vendor.image_url,
            'latitude': -33.8688,  # Sydney CBD center
            'longitude': 151.2093,
            'created_at': vendor.created_at.isoformat(),
        }
        venue_items.append(vendor_item)

    if latitude is not None and longitude is not None:
        filtered = []
        for item in venue_items:
            distance = ((item['latitude'] - latitude) ** 2 + (item['longitude'] - longitude) ** 2) ** 0.5
            if distance <= radius * 0.01:
                filtered.append(item)
        return jsonify(filtered), 200

    return jsonify(venue_items), 200

@bp.route('/<venue_id>', methods=['GET'])
def get_venue(venue_id):
    """Get venue by ID."""
    venue = Venue.objects(id=venue_id).first()
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404

    return jsonify(venue.to_dict()), 200
