from flask import Blueprint, request, jsonify
from app.models import Venue
from app import db
from sqlalchemy import and_

bp = Blueprint('venues', __name__, url_prefix='/api/venues')

@bp.route('', methods=['GET'])
def get_venues():
    """Get venues with optional filtering by location."""
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    radius = request.args.get('radius', type=float, default=5.0)  # km

    query = Venue.query

    # Filter by distance if coordinates provided
    if latitude is not None and longitude is not None:
        # Simple distance calculation (rough approximation)
        # In production, use proper geospatial queries
        venues = query.all()
        filtered = []

        for venue in venues:
            # Rough distance calculation
            distance = ((venue.latitude - latitude) ** 2 + (venue.longitude - longitude) ** 2) ** 0.5
            if distance <= radius * 0.01:  # Rough approximation
                filtered.append(venue)

        return jsonify([v.to_dict() for v in filtered]), 200

    venues = query.all()
    return jsonify([v.to_dict() for v in venues]), 200

@bp.route('/<int:venue_id>', methods=['GET'])
def get_venue(venue_id):
    """Get venue by ID."""
    venue = Venue.query.get(venue_id)

    if not venue:
        return jsonify({'error': 'Venue not found'}), 404

    return jsonify(venue.to_dict()), 200
