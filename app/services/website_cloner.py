"""
Website cloning service for phishing simulation
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

class WebsiteCloner:
    """Service for cloning websites for educational phishing simulations"""
    
    def __init__(self, upload_folder='cloned_sites'):
        self.upload_folder = upload_folder
        os.makedirs(self.upload_folder, exist_ok=True)
        
    def clone_website(self, url):
        """
        Clone a website and save it locally
        
        Args:
            url (str): URL of the website to clone
            
        Returns:
            dict: {'success': bool, 'message': str, 'url': str}
        """
        try:
            # Validate URL
            original_url = url
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            # Add headers to mimic a real browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, timeout=15, headers=headers, allow_redirects=True)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Add warning banner to cloned site
            warning_banner = soup.new_tag('div', style="""
                background: #ff4444; color: white; padding: 15px; text-align: center;
                font-weight: bold; position: fixed; top: 0; width: 100%; z-index: 9999;
                box-shadow: 0 2px 10px rgba(0,0,0,0.3); font-size: 16px;
            """)
            warning_banner.string = "⚠️ EDUCATIONAL SIMULATION - THIS IS NOT THE REAL WEBSITE ⚠️"
            
            # Add margin to body to account for banner
            if soup.body:
                soup.body.insert(0, warning_banner)
                soup.body['style'] = soup.body.get('style', '') + '; margin-top: 60px !important;'
            
            # Remove any scripts that might cause issues
            for script in soup.find_all('script'):
                script.decompose()
            
            # Save the cloned website with timestamp
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'cloned_site_{timestamp}.html'
            output_path = os.path.join(self.upload_folder, filename)
            
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(str(soup))
                
            logging.info(f"Successfully cloned website: {url}")
            return {
                'success': True, 
                'message': f'Website successfully cloned from {original_url}',
                'url': url,
                'filename': filename
            }
            
        except requests.RequestException as e:
            error_msg = f"Failed to access website {original_url}: {str(e)}"
            logging.error(error_msg)
            return {'success': False, 'message': error_msg, 'url': original_url}
        except Exception as e:
            error_msg = f"Unexpected error cloning website {original_url}: {str(e)}"
            logging.error(error_msg)
            return {'success': False, 'message': error_msg, 'url': original_url}
            
    def get_cloned_sites(self):
        """Get list of cloned sites"""
        sites = []
        if os.path.exists(self.upload_folder):
            for file in os.listdir(self.upload_folder):
                if file.endswith('.html'):
                    sites.append(file)
        return sites
