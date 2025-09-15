#!/usr/bin/env python3
"""
Legacy main.py - Redirects to new modular structure
This file is kept for backward compatibility.
Use run.py for the new application structure.
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the new application factory
from app import create_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the application
app = create_app()

if __name__ == '__main__':
    print("""
    ⚠️  NOTICE: This is the legacy main.py file.
    
    For the new professional structure, please use:
    python run.py
    
    The application will still work, but we recommend using run.py
    for the best experience with the new modular architecture.
    """)
    
    app.run(debug=True)
