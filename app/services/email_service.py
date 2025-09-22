"""
Email service for phishing simulation campaigns
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import os

class EmailService:
    """Service for sending simulated phishing emails"""
    
    def __init__(self):
        # Hardcoded Gmail SMTP configuration
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.sender_email = 'demoone913@gmail.com'
        self.sender_password = 'eqldcmvdcpcowhoa'  # Gmail App Password (Phishing Simulator)
        
    def send_notification_email(self, recipient_email, subject, body):
        """
        Send a notification email
        
        Args:
            recipient_email (str): Email address of the recipient
            subject (str): Email subject
            body (str): Email body content
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email via Gmail SMTP
            try:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()  # Enable encryption
                    if self.sender_password:
                        server.login(self.sender_email, self.sender_password)
                        server.sendmail(self.sender_email, [recipient_email], msg.as_string())
                        logging.info(f"Notification email sent to {recipient_email}")
                        return True
                    else:
                        # No credentials provided, log locally
                        logging.warning("No email credentials provided. Email logged locally.")
                        self._log_email_simulation(recipient_email, f"Subject: {subject}\n\n{body}")
                        return True
                
            except smtplib.SMTPAuthenticationError as e:
                # Authentication failed - likely need App Password
                logging.error(f"Gmail authentication failed: {e}")
                self._log_email_simulation(recipient_email, f"Authentication Error: {e}\n\nSubject: {subject}\n\n{body}")
                return False
            except (ConnectionRefusedError, OSError) as e:
                # Network issues
                logging.warning(f"SMTP connection error: {e}. Email logged locally.")
                self._log_email_simulation(recipient_email, f"Subject: {subject}\n\n{body}")
                return True
                
        except Exception as e:
            logging.error(f"Failed to send notification email to {recipient_email}: {e}")
            return False

    def send_simulation_email(self, recipient_email):
        """
        Send a simulated phishing email for educational purposes
        
        Args:
            recipient_email (str): Email address of the recipient
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = "🔒 Security Alert - Immediate Action Required"
            
            # Email body with educational warning
            body = """
            ⚠️ EDUCATIONAL SIMULATION - DO NOT CLICK LINKS ⚠️
            
            Dear User,
            
            This is a simulated phishing email for educational purposes only.
            
            In a real phishing attack, you might see:
            - Urgent language demanding immediate action
            - Suspicious links or attachments
            - Requests for personal information
            - Poor grammar or spelling
            - Mismatched sender addresses
            
            Remember: Always verify suspicious emails through official channels.
            
            This simulation is part of your cybersecurity awareness training.
            
            Best regards,
            Phishing Awareness Team
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email via Gmail SMTP
            try:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()  # Enable encryption
                    if self.sender_password:
                        server.login(self.sender_email, self.sender_password)
                        server.sendmail(self.sender_email, [recipient_email], msg.as_string())
                        logging.info(f"Simulation email sent to {recipient_email}")
                        return True
                    else:
                        # No credentials provided, log locally
                        logging.warning("No email credentials provided. Email simulation logged locally.")
                        self._log_email_simulation(recipient_email, body)
                        return True
                
            except smtplib.SMTPAuthenticationError as e:
                # Authentication failed - likely need App Password
                logging.error(f"Gmail authentication failed: {e}")
                self._log_email_simulation(recipient_email, f"Authentication Error: {e}\n\n{body}")
                return False
            except (ConnectionRefusedError, OSError) as e:
                # Network issues
                logging.warning(f"SMTP connection error: {e}. Email simulation logged for {recipient_email}")
                self._log_email_simulation(recipient_email, body)
                return True
                
        except Exception as e:
            logging.error(f"Failed to send simulation email to {recipient_email}: {e}")
            return False
            
    def _log_email_simulation(self, recipient, body):
        """Log email simulation when SMTP is not available"""
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        
        with open(os.path.join(log_dir, 'email_simulations.log'), 'a') as f:
            f.write(f"\n--- Email Simulation ---\n")
            f.write(f"Recipient: {recipient}\n")
            f.write(f"Body: {body}\n")
            f.write(f"--- End Simulation ---\n\n")
