from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app(config_name='development'):
    """Application factory pattern."""
    # Get the root path for static files
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_path = os.path.join(root_path, 'frontend', 'dist')

    app = Flask(__name__, static_folder=static_path, static_url_path='')

    # Load configuration
    if config_name == 'production':
        from app.config import ProductionConfig as config
    elif config_name == 'testing':
        from app.config import TestingConfig as config
    else:
        from app.config import DevelopmentConfig as config

    app.config.from_object(config)

    # Initialize extensions
    db.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes import auth, users, venues, promotions, invitations, messages, vendors, seed

    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(venues.bp)
    app.register_blueprint(promotions.bp)
    app.register_blueprint(invitations.bp)
    app.register_blueprint(messages.bp)
    app.register_blueprint(vendors.bp)
    app.register_blueprint(seed.bp)

    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return {'status': 'healthy'}, 200

    # Serve React app
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react(path):
        index_path = os.path.join(static_path, 'index.html')
        if path and os.path.exists(os.path.join(static_path, path)):
            return send_from_directory(static_path, path)
        elif os.path.exists(index_path):
            return send_from_directory(static_path, 'index.html')
        else:
            return {'error': 'React app not built. Run "npm run build"'}, 404

    # Create tables
    with app.app_context():
        db.create_all()

    return app
