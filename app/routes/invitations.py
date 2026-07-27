from flask import Blueprint, request, jsonify, session
from app.models import Invitation, InvitationStatus, User, Venue

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

    recipient = User.objects(id=data['recipient_id']).first()
    venue = Venue.objects(id=data['venue_id']).first()
    sender = User.objects(id=user_id).first()

    if not recipient or not venue or not sender:
        return jsonify({'error': 'Recipient, venue, or sender not found'}), 404

    invitation = Invitation(
        sender_id=sender,
        recipient_id=recipient,
        venue_id=venue,
        message=data.get('message', '')
    )
    invitation.save()

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

    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    received = list(Invitation.objects(recipient_id=user))

    return jsonify([i.to_dict() for i in received]), 200

@bp.route('/<invitation_id>/accept', methods=['POST'])
def accept_invitation(invitation_id):
    """Accept an invitation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    invitation = Invitation.objects(id=invitation_id).first()
    user = User.objects(id=user_id).first()

    if not invitation or not user:
        return jsonify({'error': 'Invitation or user not found'}), 404

    if str(invitation.recipient_id.id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    invitation.status = InvitationStatus.ACCEPTED.value
    invitation.save()

    return jsonify({
        'message': 'Invitation accepted',
        'invitation': invitation.to_dict()
    }), 200

@bp.route('/<invitation_id>/decline', methods=['POST'])
def decline_invitation(invitation_id):
    """Decline an invitation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    invitation = Invitation.objects(id=invitation_id).first()
    user = User.objects(id=user_id).first()

    if not invitation or not user:
        return jsonify({'error': 'Invitation or user not found'}), 404

    if str(invitation.recipient_id.id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    invitation.status = InvitationStatus.DECLINED.value
    invitation.save()

    return jsonify({
        'message': 'Invitation declined',
        'invitation': invitation.to_dict()
    }), 200
