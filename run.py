#!/usr/bin/env python3
"""
Phishing Simulation Tool - Application Entry Point
Educational cybersecurity awareness platform
"""

import os
from app import create_app
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create Flask application instance
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment variables
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"""
    🛡️  Phishing Simulation Tool Starting...
    
    📍 URL: http://{host}:{port}
    🔧 Debug Mode: {debug}
    📚 Educational Platform Ready!
    
    Navigate to the URL above to begin your cybersecurity training.
    """)
    
    app.run(host=host, port=port, debug=debug)
