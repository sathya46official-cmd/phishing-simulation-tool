"""
Simulation routes for phishing tests and email campaigns
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.services.email_service import EmailService
from app.services.certificate_generator import CertificateGenerator
from app.services.statistics import StatisticsService

simulation_bp = Blueprint('simulation', __name__)

@simulation_bp.route('/test', methods=['GET', 'POST'])
def phishing_test():
    """Interactive phishing awareness test"""
    import random
    
    # Large pool of questions for randomization
    question_pool = [
        {
            "q": "Which URL is suspicious?", 
            "options": ["google.com", "g00gle.com", "facebook.com", "gmail.com"], 
            "answer": "g00gle.com"
        },
        {
            "q": "Which email is likely a phishing attempt?", 
            "options": ["support@paypal.com", "security-paypal@info.com", "admin@bank.com", "service@amazon.com"], 
            "answer": "security-paypal@info.com"
        },
        {
            "q": "What should you do if you receive a suspicious email?", 
            "options": ["Click the link to verify", "Reply with your password", "Delete and report it", "Forward to friends"], 
            "answer": "Delete and report it"
        },
        {
            "q": "Which greeting is a red flag in phishing emails?", 
            "options": ["Dear John Smith", "Hello Mr. Smith", "Dear Customer", "Hi John"], 
            "answer": "Dear Customer"
        },
        {
            "q": "What is a common sign of a phishing email?", 
            "options": ["Professional formatting", "Correct spelling", "Urgent language", "Company logo"], 
            "answer": "Urgent language"
        },
        {
            "q": "Which domain is suspicious for a bank email?", 
            "options": ["chase.com", "bankofamerica.com", "wel1sfargo.com", "citibank.com"], 
            "answer": "wel1sfargo.com"
        },
        {
            "q": "What should you do before clicking a link in an email?", 
            "options": ["Click immediately", "Hover to see the URL", "Forward to friends", "Reply to sender"], 
            "answer": "Hover to see the URL"
        },
        {
            "q": "Which attachment type is most dangerous?", 
            "options": [".pdf", ".txt", ".exe", ".jpg"], 
            "answer": ".exe"
        },
        {
            "q": "What is spear phishing?", 
            "options": ["Random mass emails", "Targeted personal attacks", "SMS messages", "Phone calls"], 
            "answer": "Targeted personal attacks"
        },
        {
            "q": "Which is the best way to verify a suspicious email?", 
            "options": ["Reply to the email", "Click the verification link", "Contact company directly", "Ignore it"], 
            "answer": "Contact company directly"
        },
        {
            "q": "What does 2FA stand for?", 
            "options": ["Two Factor Authentication", "Two File Access", "Total Fraud Alert", "Two Form Application"], 
            "answer": "Two Factor Authentication"
        },
        {
            "q": "Which email subject is suspicious?", 
            "options": ["Monthly Newsletter", "URGENT: Account Suspended!", "Meeting Tomorrow", "Happy Birthday"], 
            "answer": "URGENT: Account Suspended!"
        }
    ]
    
    # Randomly select 5 questions for each test
    questions = random.sample(question_pool, min(5, len(question_pool)))
    
    if request.method == 'POST':
        answers = [request.form.get(f'q{i}') for i in range(len(questions))]
        correct_answers = [question['answer'] for question in questions]
        
        # Calculate score
        score = sum(1 for i, answer in enumerate(answers) if answer == correct_answers[i])
        percentage = round((score / len(questions)) * 100, 1)
        
        # Record test completion in statistics
        stats_service = StatisticsService()
        stats_service.record_test_completion(score, len(questions))
        
        # Store results in session for results page
        session['test_results'] = {
            'score': score,
            'total': len(questions),
            'percentage': percentage,
            'questions': questions,
            'user_answers': answers,
            'correct_answers': correct_answers
        }
        
        return redirect(url_for('simulation.test_results'))
    
    return render_template('simulation/test.html', questions=questions)

@simulation_bp.route('/results')
def test_results():
    """Display test results and generate certificate"""
    score = session.get('test_score', 0)
    total = session.get('total_questions', 0)
    percentage = (score / total * 100) if total > 0 else 0
    
    return render_template('simulation/results.html', 
                         score=score, total=total, percentage=percentage)

@simulation_bp.route('/email', methods=['GET', 'POST'])
def email_simulation():
    """Send simulated phishing emails for testing"""
    if request.method == 'POST':
        recipient_email = request.form.get('email')
        if not recipient_email:
            flash('Please provide a valid email address', 'error')
            return render_template('simulation/email.html')
        
        email_service = EmailService()
        success = email_service.send_simulation_email(recipient_email)
        
        # Record email sending in statistics
        stats_service = StatisticsService()
        if success:
            stats_service.record_email_sent(recipient_email)
            flash('Simulation email sent successfully!', 'success')
        else:
            flash('Failed to send email. Check your SMTP configuration.', 'error')
    
    return render_template('simulation/email.html')
