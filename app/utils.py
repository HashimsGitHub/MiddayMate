"""Utility functions for MiddayMate."""
from functools import wraps
from flask import session, jsonify

def login_required(f):
    """Decorator to require authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

def vendor_required(f):
    """Decorator to require vendor role."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from app.models import User, UserRole

        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401

        user = User.query.get(session['user_id'])
        if not user or user.role != UserRole.VENDOR:
            return jsonify({'error': 'Vendor access required'}), 403

        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to require admin role."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from app.models import User, UserRole

        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401

        user = User.query.get(session['user_id'])
        if not user or user.role != UserRole.ADMIN:
            return jsonify({'error': 'Admin access required'}), 403

        return f(*args, **kwargs)
    return decorated_function
