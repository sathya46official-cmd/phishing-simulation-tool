"""
Education routes for tutorials and learning materials
"""

from flask import Blueprint, render_template, send_file
from app.services.certificate_generator import CertificateGenerator

education_bp = Blueprint('education', __name__)

@education_bp.route('/tutorial')
def tutorial():
    """Interactive tutorial with Matrix-themed design"""
    return render_template('education/tutorial.html', 
                         book_title="Don't Get Trapped, Get Educated", 
                         matrix_style=True, 
                         page_flip=True)

@education_bp.route('/chapter1')
def chapter1():
    """Chapter 1: Recognizing Phishing"""
    return render_template('education/chapter1.html')

@education_bp.route('/chapter2')
def chapter2():
    """Chapter 2: Protection Strategies"""
    return render_template('education/chapter2.html')

@education_bp.route('/chapter3')
def chapter3():
    """Chapter 3: Common Attack Types"""
    return render_template('education/chapter3.html')

@education_bp.route('/chapter4')
def chapter4():
    """Chapter 4: Incident Response"""
    return render_template('education/chapter4.html')

@education_bp.route('/guidelines')
def guidelines():
    """Security guidelines and best practices"""
    return render_template('education/guidelines.html')

@education_bp.route('/certificate/<int:score>/<int:total>')
def generate_certificate(score, total):
    """Generate and download awareness certificate"""
    generator = CertificateGenerator()
    pdf_path = generator.create_certificate(score, total)
    return send_file(pdf_path, as_attachment=True)
