import os
from dotenv import load_dotenv
from app import create_app, db

# Load environment variables
load_dotenv()

app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Make shell context for Flask CLI."""
    return {'db': db}

if __name__ == '__main__':
    # In production, use gunicorn instead
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=5000, debug=debug)
