"""
Admin routes for website cloning and management
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.services.website_cloner import WebsiteCloner
from app.services.statistics import StatisticsService
from app.routes.auth import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
@admin_required
def dashboard():
    """Admin dashboard for managing phishing simulations"""
    stats_service = StatisticsService()
    dashboard_stats = stats_service.get_dashboard_stats()
    return render_template('admin/dashboard.html', stats=dashboard_stats)

@admin_bp.route('/clone', methods=['GET', 'POST'])
@admin_required
def clone_website():
    """Clone a website for phishing simulation"""
    if request.method == 'POST':
        url = request.form.get('url')
        email = request.form.get('notification_email')
        
        if not url:
            flash('Please provide a valid URL', 'error')
            return render_template('admin/clone.html')
        
        cloner = WebsiteCloner()
        result = cloner.clone_website(url)
        
        if result['success']:
            flash(result['message'], 'success')
            
            # Record the website cloning in statistics
            stats_service = StatisticsService()
            stats_service.record_website_cloned(result['url'], result.get('filename'))
            
            # Send notification email if provided
            if email:
                from app.services.email_service import EmailService
                email_service = EmailService()
                
                notification_body = f"""
                🛡️ PHISHING SIMULATION ALERT 🛡️
                
                A website has been cloned for educational phishing simulation:
                
                Original URL: {result['url']}
                Cloned File: {result['filename']}
                Purpose: Educational cybersecurity training
                
                This is part of your phishing awareness training program.
                The cloned site includes clear warning banners and is for educational use only.
                
                Please review the cloned site and use it to test your phishing detection skills.
                
                Best regards,
                Cybersecurity Training Team
                """
                
                email_sent = email_service.send_notification_email(email, "Website Cloned for Training", notification_body)
                if email_sent:
                    flash(f'Notification email sent to {email}', 'info')
                    stats_service.record_email_sent(email, "Website Cloned for Training")
                else:
                    flash(f'Website cloned but failed to send notification to {email}', 'warning')
            
            return redirect(url_for('admin.view_cloned'))
        else:
            flash(result['message'], 'error')
    
    return render_template('admin/clone.html')

@admin_bp.route('/cloned')
@admin_required
def view_cloned():
    """View cloned websites"""
    return render_template('admin/cloned.html')
