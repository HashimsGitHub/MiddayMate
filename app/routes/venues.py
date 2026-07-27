from flask import Blueprint, request, jsonify
from app.models import Venue

bp = Blueprint('venues', __name__, url_prefix='/api/venues')

@bp.route('', methods=['GET'])
def get_venues():
    """Get venues with optional filtering by location."""
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    radius = request.args.get('radius', type=float, default=5.0)

    venues = list(Venue.objects())

    if latitude is not None and longitude is not None:
        filtered = []
        for venue in venues:
            distance = ((venue.latitude - latitude) ** 2 + (venue.longitude - longitude) ** 2) ** 0.5
            if distance <= radius * 0.01:
                filtered.append(venue)
        return jsonify([v.to_dict() for v in filtered]), 200

    return jsonify([v.to_dict() for v in venues]), 200

@bp.route('/<venue_id>', methods=['GET'])
def get_venue(venue_id):
    """Get venue by ID."""
    venue = Venue.objects(id=venue_id).first()
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404

    return jsonify(venue.to_dict()), 200
