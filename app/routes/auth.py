from flask import Blueprint, request, jsonify, session
from app.models import User, UserRole

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login', methods=['POST'])
def login():
    """Handle OAuth login."""
    data = request.get_json()

    if not data or not data.get('oauth_provider') or not data.get('oauth_id'):
        return jsonify({'error': 'Missing required fields'}), 400

    oauth_provider = data['oauth_provider']
    oauth_id = data['oauth_id']
    email = data.get('email')
    name = data.get('name')

    user = User.objects(oauth_id=oauth_id, oauth_provider=oauth_provider).first()
    if not user:
        user = User(
            oauth_id=oauth_id,
            oauth_provider=oauth_provider,
            email=email,
            name=name,
            role=UserRole.PROFESSIONAL.value
        )
        user.save()

    session['user_id'] = str(user.id)
    return jsonify({
        'message': 'Login successful',
        'user': user.to_dict()
    }), 200

@bp.route('/logout', methods=['POST'])
def logout():
    """Handle logout."""
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200

@bp.route('/me', methods=['GET'])
def get_current_user():
    """Get current logged-in user."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user.to_dict()), 200
