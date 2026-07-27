from flask import Blueprint, request, jsonify, session
from app.models import Promotion, Venue
from datetime import datetime

bp = Blueprint('promotions', __name__, url_prefix='/api/promotions')

@bp.route('', methods=['GET'])
def get_promotions():
    """Get active promotions."""
    now = datetime.utcnow()
    promotions = list(Promotion.objects(start_date__lte=now, end_date__gte=now))

    return jsonify([p.to_dict() for p in promotions]), 200

@bp.route('/venue/<venue_id>', methods=['GET'])
def get_venue_promotions(venue_id):
    """Get promotions for a specific venue."""
    venue = Venue.objects(id=venue_id).first()
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404

    promotions = list(Promotion.objects(venue_id=venue))
    return jsonify([p.to_dict() for p in promotions]), 200

@bp.route('/<promotion_id>', methods=['GET'])
def get_promotion(promotion_id):
    """Get promotion by ID."""
    promotion = Promotion.objects(id=promotion_id).first()
    if not promotion:
        return jsonify({'error': 'Promotion not found'}), 404

    return jsonify(promotion.to_dict()), 200
