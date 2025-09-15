"""
Main routes for the phishing simulation tool
"""

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page with navigation to different modules"""
    return render_template('index.html')

@main_bp.route('/about')
def about():
    """About page explaining the purpose of the tool"""
    return render_template('about.html')
