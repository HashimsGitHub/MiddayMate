from flask import Blueprint, request, jsonify, session
from app.models import Message, Invitation, InvitationStatus
from app import db

bp = Blueprint('messages', __name__, url_prefix='/api/messages')

@bp.route('', methods=['POST'])
def send_message():
    """Send a message in an invitation conversation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    data = request.get_json()

    if not data or not data.get('invitation_id') or not data.get('content'):
        return jsonify({'error': 'Missing required fields'}), 400

    invitation_id = data['invitation_id']
    content = data['content']

    invitation = Invitation.query.get(invitation_id)

    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404

    # Only participants can message
    if user_id not in [invitation.sender_id, invitation.recipient_id]:
        return jsonify({'error': 'Unauthorized'}), 403

    # Invitation must be accepted
    if invitation.status != InvitationStatus.ACCEPTED:
        return jsonify({'error': 'Invitation not accepted'}), 400

    message = Message(
        invitation_id=invitation_id,
        sender_id=user_id,
        content=content
    )

    db.session.add(message)
    db.session.commit()

    return jsonify({
        'message': 'Message sent',
        'data': message.to_dict()
    }), 201

@bp.route('/invitation/<int:invitation_id>', methods=['GET'])
def get_messages(invitation_id):
    """Get all messages in an invitation conversation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    invitation = Invitation.query.get(invitation_id)

    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404

    # Only participants can view messages
    if user_id not in [invitation.sender_id, invitation.recipient_id]:
        return jsonify({'error': 'Unauthorized'}), 403

    messages = Message.query.filter_by(invitation_id=invitation_id).order_by(Message.created_at).all()

    # Mark messages as read
    Message.query.filter_by(invitation_id=invitation_id).update({'is_read': True})
    db.session.commit()

    return jsonify([m.to_dict() for m in messages]), 200
