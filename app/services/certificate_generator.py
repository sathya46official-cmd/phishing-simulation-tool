"""
Certificate generation service for phishing awareness training
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.colors import HexColor
from datetime import datetime

class CertificateGenerator:
    """Service for generating phishing awareness certificates"""
    
    def __init__(self, output_dir='static/certificates'):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def create_certificate(self, score, total_questions):
        """
        Generate a certificate PDF based on test performance
        
        Args:
            score (int): Number of correct answers
            total_questions (int): Total number of questions
            
        Returns:
            str: Path to the generated certificate
        """
        percentage = (score / total_questions * 100) if total_questions > 0 else 0
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'phishing_awareness_certificate_{timestamp}.pdf'
        pdf_path = os.path.join(self.output_dir, filename)
        
        # Create PDF
        c = canvas.Canvas(pdf_path, pagesize=A4)
        width, height = A4
        
        # Colors
        primary_color = HexColor('#2C3E50')
        accent_color = HexColor('#3498DB')
        success_color = HexColor('#27AE60')
        warning_color = HexColor('#F39C12')
        
        # Header
        c.setFillColor(primary_color)
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredText(width/2, height-100, "PHISHING AWARENESS CERTIFICATE")
        
        # Subtitle
        c.setFillColor(accent_color)
        c.setFont("Helvetica", 16)
        c.drawCentredText(width/2, height-140, "Cybersecurity Education Program")
        
        # Main content
        c.setFillColor(primary_color)
        c.setFont("Helvetica", 14)
        c.drawCentredText(width/2, height-200, "This certifies that the participant has completed")
        c.drawCentredText(width/2, height-220, "the Phishing Awareness Training Program")
        
        # Score section
        c.setFont("Helvetica-Bold", 18)
        if percentage >= 80:
            c.setFillColor(success_color)
            performance_text = "EXCELLENT PERFORMANCE"
        elif percentage >= 60:
            c.setFillColor(warning_color)
            performance_text = "GOOD PERFORMANCE"
        else:
            c.setFillColor(HexColor('#E74C3C'))
            performance_text = "NEEDS IMPROVEMENT"
            
        c.drawCentredText(width/2, height-280, performance_text)
        
        # Score details
        c.setFillColor(primary_color)
        c.setFont("Helvetica", 14)
        c.drawCentredText(width/2, height-320, f"Score: {score}/{total_questions} ({percentage:.1f}%)")
        
        # Date
        c.setFont("Helvetica", 12)
        date_str = datetime.now().strftime("%B %d, %Y")
        c.drawCentredText(width/2, height-380, f"Completed on: {date_str}")
        
        # Footer
        c.setFont("Helvetica-Oblique", 10)
        c.drawCentredText(width/2, 50, "This certificate is issued for educational purposes only")
        
        # Border
        c.setStrokeColor(accent_color)
        c.setLineWidth(3)
        c.rect(30, 30, width-60, height-60)
        
        c.save()
        return pdf_path
