from flask import Blueprint, request, jsonify, session
from app.models import Message, Invitation, InvitationStatus, User

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

    invitation = Invitation.objects(id=data['invitation_id']).first()
    sender = User.objects(id=user_id).first()

    if not invitation or not sender:
        return jsonify({'error': 'Invitation or user not found'}), 404

    if user_id not in [str(invitation.sender_id.id), str(invitation.recipient_id.id)]:
        return jsonify({'error': 'Unauthorized'}), 403

    if invitation.status != InvitationStatus.ACCEPTED.value:
        return jsonify({'error': 'Invitation not accepted'}), 400

    message = Message(
        invitation_id=invitation,
        sender_id=sender,
        content=data['content']
    )
    message.save()

    return jsonify({
        'message': 'Message sent',
        'data': message.to_dict()
    }), 201

@bp.route('/invitation/<invitation_id>', methods=['GET'])
def get_messages(invitation_id):
    """Get all messages in an invitation conversation."""
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401

    invitation = Invitation.objects(id=invitation_id).first()
    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404

    if user_id not in [str(invitation.sender_id.id), str(invitation.recipient_id.id)]:
        return jsonify({'error': 'Unauthorized'}), 403

    messages = list(Message.objects(invitation_id=invitation).order_by('created_at'))

    Message.objects(invitation_id=invitation).update(is_read=True)

    return jsonify([m.to_dict() for m in messages]), 200
