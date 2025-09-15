"""
Statistics service for tracking phishing simulation metrics
"""
import os
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List

class StatisticsService:
    """Service for managing phishing simulation statistics"""
    
    def __init__(self):
        self.stats_file = 'stats.json'
        self.logs_dir = 'logs'
        self.cloned_sites_dir = os.environ.get('UPLOAD_FOLDER', 'cloned_sites')
        self._ensure_stats_file()
    
    def _ensure_stats_file(self):
        """Ensure stats file exists with default values"""
        if not os.path.exists(self.stats_file):
            default_stats = {
                'total_users': 0,
                'tests_completed': 0,
                'emails_sent': 0,
                'websites_cloned': 0,
                'test_results': [],
                'email_logs': [],
                'clone_logs': [],
                'created_at': datetime.now().isoformat()
            }
            self._save_stats(default_stats)
    
    def _load_stats(self) -> Dict:
        """Load statistics from file"""
        try:
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._ensure_stats_file()
            return self._load_stats()
    
    def _save_stats(self, stats: Dict):
        """Save statistics to file"""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(stats, f, indent=2)
        except Exception as e:
            logging.error(f"Failed to save statistics: {e}")
    
    def record_test_completion(self, score: int, total_questions: int, user_id: str = None):
        """Record a completed phishing test"""
        stats = self._load_stats()
        
        test_result = {
            'score': score,
            'total_questions': total_questions,
            'percentage': round((score / total_questions) * 100, 1),
            'user_id': user_id or f"user_{len(stats['test_results']) + 1}",
            'timestamp': datetime.now().isoformat()
        }
        
        stats['test_results'].append(test_result)
        stats['tests_completed'] += 1
        
        # Update total users (simple increment for demo)
        if user_id and user_id not in [r.get('user_id') for r in stats['test_results'][:-1]]:
            stats['total_users'] += 1
        
        self._save_stats(stats)
        logging.info(f"Recorded test completion: {score}/{total_questions}")
    
    def record_email_sent(self, recipient: str, subject: str = None):
        """Record an email being sent"""
        stats = self._load_stats()
        
        email_log = {
            'recipient': recipient,
            'subject': subject or 'Phishing Simulation',
            'timestamp': datetime.now().isoformat()
        }
        
        stats['email_logs'].append(email_log)
        stats['emails_sent'] += 1
        
        self._save_stats(stats)
        logging.info(f"Recorded email sent to {recipient}")
    
    def record_website_cloned(self, url: str, filename: str = None):
        """Record a website being cloned"""
        stats = self._load_stats()
        
        clone_log = {
            'url': url,
            'filename': filename,
            'timestamp': datetime.now().isoformat()
        }
        
        stats['clone_logs'].append(clone_log)
        stats['websites_cloned'] += 1
        
        self._save_stats(stats)
        logging.info(f"Recorded website clone: {url}")
    
    def get_dashboard_stats(self) -> Dict:
        """Get statistics for admin dashboard"""
        stats = self._load_stats()
        
        # Calculate success rate from test results
        if stats['test_results']:
            total_score = sum(r['score'] for r in stats['test_results'])
            total_possible = sum(r['total_questions'] for r in stats['test_results'])
            success_rate = round((total_score / total_possible) * 100, 1) if total_possible > 0 else 0
        else:
            success_rate = 0
        
        # Count active simulations (emails sent in last 24 hours)
        recent_emails = [
            log for log in stats['email_logs']
            if datetime.fromisoformat(log['timestamp']) > datetime.now() - timedelta(hours=24)
        ]
        
        # Count cloned sites that exist
        cloned_sites_count = 0
        if os.path.exists(self.cloned_sites_dir):
            cloned_sites_count = len([f for f in os.listdir(self.cloned_sites_dir) if f.endswith('.html')])
        
        return {
            'total_users': max(stats['total_users'], len(set(r.get('user_id', '') for r in stats['test_results']))),
            'tests_completed': stats['tests_completed'],
            'active_simulations': len(recent_emails),
            'success_rate': success_rate,
            'emails_sent': stats['emails_sent'],
            'websites_cloned': cloned_sites_count,
            'recent_activity': self._get_recent_activity(stats)
        }
    
    def _get_recent_activity(self, stats: Dict) -> List[Dict]:
        """Get recent activity for dashboard"""
        activities = []
        
        # Recent test completions
        recent_tests = sorted(stats['test_results'], key=lambda x: x['timestamp'], reverse=True)[:3]
        for test in recent_tests:
            activities.append({
                'description': f"User completed phishing test ({test['score']}/{test['total_questions']})",
                'timestamp': test['timestamp'],
                'type': 'test'
            })
        
        # Recent emails
        recent_emails = sorted(stats['email_logs'], key=lambda x: x['timestamp'], reverse=True)[:2]
        for email in recent_emails:
            activities.append({
                'description': f"Simulation email sent to {email['recipient']}",
                'timestamp': email['timestamp'],
                'type': 'email'
            })
        
        # Recent clones
        recent_clones = sorted(stats['clone_logs'], key=lambda x: x['timestamp'], reverse=True)[:2]
        for clone in recent_clones:
            activities.append({
                'description': f"Website cloned: {clone['url']}",
                'timestamp': clone['timestamp'],
                'type': 'clone'
            })
        
        # Sort all activities by timestamp and return top 5
        activities.sort(key=lambda x: x['timestamp'], reverse=True)
        return activities[:5]
    
    def get_time_ago(self, timestamp_str: str) -> str:
        """Convert timestamp to human readable time ago"""
        try:
            timestamp = datetime.fromisoformat(timestamp_str)
            now = datetime.now()
            diff = now - timestamp
            
            if diff.days > 0:
                return f"{diff.days} day{'s' if diff.days != 1 else ''} ago"
            elif diff.seconds > 3600:
                hours = diff.seconds // 3600
                return f"{hours} hour{'s' if hours != 1 else ''} ago"
            elif diff.seconds > 60:
                minutes = diff.seconds // 60
                return f"{minutes} min ago"
            else:
                return "Just now"
        except:
            return "Unknown"
