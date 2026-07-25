from flask import Blueprint, request, jsonify, session
from app.models import User, AvailabilityStatus
from app import db

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/me', methods=['GET'])
def get_current_user():
    """Get current user profile."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict()), 200

@bp.route('/profile', methods=['POST'])
def update_profile():
    """Update user profile."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()

    if 'name' in data:
        user.name = data['name']
    if 'bio' in data:
        user.bio = data['bio']
    if 'profile_image_url' in data:
        user.profile_image_url = data['profile_image_url']
    if 'social_media_links' in data:
        user.social_media_links = data['social_media_links']
    if 'availability_status' in data:
        if data['availability_status'] in [s.value for s in AvailabilityStatus]:
            user.availability_status = data['availability_status']

    db.session.commit()

    return jsonify({
        'message': 'Profile updated',
        'user': user.to_dict()
    }), 200

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user profile by ID."""
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict()), 200
