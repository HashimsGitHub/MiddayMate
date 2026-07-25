from flask import Blueprint, request, jsonify, session
from app.models import Promotion, Venue
from app import db
from datetime import datetime

bp = Blueprint('promotions', __name__, url_prefix='/api/promotions')

@bp.route('', methods=['GET'])
def get_promotions():
    """Get active promotions."""
    now = datetime.utcnow()
    promotions = Promotion.query.filter(
        Promotion.start_date <= now,
        Promotion.end_date >= now
    ).all()

    return jsonify([p.to_dict() for p in promotions]), 200

@bp.route('/venue/<int:venue_id>', methods=['GET'])
def get_venue_promotions(venue_id):
    """Get promotions for a specific venue."""
    venue = Venue.query.get(venue_id)

    if not venue:
        return jsonify({'error': 'Venue not found'}), 404

    promotions = Promotion.query.filter_by(venue_id=venue_id).all()
    return jsonify([p.to_dict() for p in promotions]), 200

@bp.route('/<int:promotion_id>', methods=['GET'])
def get_promotion(promotion_id):
    """Get promotion by ID."""
    promotion = Promotion.query.get(promotion_id)

    if not promotion:
        return jsonify({'error': 'Promotion not found'}), 404

    return jsonify(promotion.to_dict()), 200
