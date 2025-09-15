"""
Phishing Simulation Tool - Flask Application Factory
Educational cybersecurity awareness platform
"""

from flask import Flask
import os

def create_app():
    """Application factory pattern for Flask app creation"""
    # Get the parent directory (project root) for template and static folders
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(project_root, 'templates')
    static_dir = os.path.join(project_root, 'static')
    
    app = Flask(__name__, 
                template_folder=template_dir,
                static_folder=static_dir)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['UPLOAD_FOLDER'] = 'cloned_sites'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    
    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.admin import admin_bp
    from app.routes.simulation import simulation_bp
    from app.routes.education import education_bp
    from app.routes.auth import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(simulation_bp, url_prefix='/simulation')
    app.register_blueprint(education_bp, url_prefix='/education')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Register custom Jinja2 filters
    from app.services.statistics import StatisticsService
    stats_service = StatisticsService()
    
    @app.template_filter('timeago')
    def timeago_filter(timestamp_str):
        return stats_service.get_time_ago(timestamp_str)
    
    return app
