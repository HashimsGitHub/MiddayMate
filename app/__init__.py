from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app(config_name='development'):
    """Application factory pattern."""
    # Get the root path for static files
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_folder = os.path.join(root_path, 'frontend')
    template_folder = os.path.join(root_path, 'frontend')

    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

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
    from app.routes import auth, users, venues, promotions, invitations, messages, vendors

    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(venues.bp)
    app.register_blueprint(promotions.bp)
    app.register_blueprint(invitations.bp)
    app.register_blueprint(messages.bp)
    app.register_blueprint(vendors.bp)

    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return {'status': 'healthy'}, 200

    # Serve index.html for root path
    @app.route('/', methods=['GET'])
    def index():
        from flask import render_template
        return render_template('index.html')

    # Create tables
    with app.app_context():
        db.create_all()

    return app
