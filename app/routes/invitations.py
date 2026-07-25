from flask import Blueprint, request, jsonify, session
from app.models import Invitation, InvitationStatus, User, Venue
from app import db

bp = Blueprint('invitations', __name__, url_prefix='/api/invitations')

@bp.route('', methods=['POST'])
def create_invitation():
    """Create a meetup invitation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    data = request.get_json()

    if not data or not data.get('recipient_id') or not data.get('venue_id'):
        return jsonify({'error': 'Missing required fields'}), 400

    recipient_id = data['recipient_id']
    venue_id = data['venue_id']
    message = data.get('message', '')

    # Validate recipient exists
    recipient = User.query.get(recipient_id)
    if not recipient:
        return jsonify({'error': 'Recipient not found'}), 404

    # Validate venue exists
    venue = Venue.query.get(venue_id)
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404

    invitation = Invitation(
        sender_id=user_id,
        recipient_id=recipient_id,
        venue_id=venue_id,
        message=message
    )

    db.session.add(invitation)
    db.session.commit()

    return jsonify({
        'message': 'Invitation sent',
        'invitation': invitation.to_dict()
    }), 201

@bp.route('', methods=['GET'])
def get_invitations():
    """Get invitations for current user."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    # Get received invitations
    received = Invitation.query.filter_by(recipient_id=user_id).all()

    return jsonify([i.to_dict() for i in received]), 200

@bp.route('/<int:invitation_id>/accept', methods=['POST'])
def accept_invitation(invitation_id):
    """Accept an invitation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    invitation = Invitation.query.get(invitation_id)

    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404

    if invitation.recipient_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    invitation.status = InvitationStatus.ACCEPTED
    db.session.commit()

    return jsonify({
        'message': 'Invitation accepted',
        'invitation': invitation.to_dict()
    }), 200

@bp.route('/<int:invitation_id>/decline', methods=['POST'])
def decline_invitation(invitation_id):
    """Decline an invitation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    invitation = Invitation.query.get(invitation_id)

    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404

    if invitation.recipient_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    invitation.status = InvitationStatus.DECLINED
    db.session.commit()

    return jsonify({
        'message': 'Invitation declined',
        'invitation': invitation.to_dict()
    }), 200
