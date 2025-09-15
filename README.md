# 🛡️ Phishing Simulation Tool

A comprehensive educational cybersecurity platform designed to help users learn about phishing attacks through interactive simulations, tutorials, and awareness testing.

## 🌟 Features

- **Interactive Tutorial**: Matrix-themed educational content with page-flip effects
- **Phishing Awareness Test**: Quiz system with certificate generation
- **Website Cloning**: Safe simulation environment for educational purposes
- **Email Simulation**: Controlled phishing email testing
- **Admin Dashboard**: Management interface for training programs
- **Professional UI**: Modern, responsive design with Bootstrap 5

## 🔒 Security Notice

This tool is designed for educational purposes only. Always ensure you have proper authorization before testing any system. The tool includes built-in safety measures to prevent misuse.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/phishing-simulation-tool.git
   cd phishing-simulation-tool
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Then edit the `.env` file with your configuration:
   - `SENDER_EMAIL`: Your Gmail address
   - `SENDER_PASSWORD`: Your Gmail App Password (not your regular password)
   - `SECRET_KEY`: A strong secret key for Flask sessions
   
   > **Important**: Never commit your `.env` file to version control. It's already added to `.gitignore` for security.

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
phishing_simulation_tool/
├── app/
│   ├── __init__.py              # Application factory
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py              # Main routes
│   │   ├── admin.py             # Admin functionality
│   │   ├── simulation.py        # Phishing simulations
│   │   └── education.py         # Educational content
│   └── services/
│       ├── __init__.py
│       ├── website_cloner.py    # Website cloning service
│       ├── email_service.py     # Email simulation service
│       └── certificate_generator.py  # PDF certificate generation
├── templates/
│   ├── base.html               # Base template
│   ├── index.html              # Home page
│   ├── admin/                  # Admin templates
│   ├── simulation/             # Simulation templates
│   └── education/              # Educational templates
├── static/
│   ├── css/
│   │   └── style.css           # Custom styles
│   └── js/
│       └── main.js             # JavaScript functionality
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── run.py                     # Application entry point
└── README.md                  # This file
```

## 🎯 Usage

### For Learners

1. **Start with the Tutorial**: Navigate to Education → Tutorial to learn about phishing identification
2. **Take the Test**: Complete the phishing awareness quiz in Simulation → Take Test
3. **Download Certificate**: Get your completion certificate after passing the test

### For Administrators

1. **Access Admin Dashboard**: Navigate to Admin → Dashboard
2. **Clone Websites**: Use Admin → Clone Website for creating safe simulation environments
3. **Send Test Emails**: Use Simulation → Email Simulation for controlled phishing tests

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
SMTP_SERVER=localhost
SMTP_PORT=587
SENDER_EMAIL=admin@phishingtest.com
```

### Email Configuration

For email simulations, configure your SMTP settings in the `.env` file. In development mode, emails are logged to `logs/email_simulations.log` if no SMTP server is available.

## 🛠️ Development

### Running in Development Mode

```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python run.py
```

### Adding New Features

1. Create new routes in the appropriate blueprint (`app/routes/`)
2. Add corresponding templates in `templates/`
3. Update static assets as needed
4. Add any new dependencies to `requirements.txt`

## 📊 Features Overview

### Educational Components
- **Interactive Tutorial**: Learn phishing identification techniques
- **Security Guidelines**: Best practices for email security
- **Real-world Examples**: Actual phishing scenarios

### Simulation Components
- **Website Cloning**: Safe environment for testing recognition skills
- **Email Testing**: Controlled phishing email campaigns
- **Progress Tracking**: Monitor learning progress and completion

### Administrative Tools
- **Dashboard**: Overview of user progress and system metrics
- **Report Generation**: Detailed analytics and performance reports
- **User Management**: Track individual and group progress

## 🔒 Security Best Practices

1. **Email Configuration**
   - Use a dedicated Gmail account for testing
   - Generate an App Password instead of using your regular password
   - Never commit real credentials to version control

2. **Environment Variables**
   - Keep all sensitive data in `.env` file
   - The `.env` file is automatically ignored by Git
   - Share only the `.env.example` file with placeholder values

3. **Application Security**
   - All cloned websites include prominent educational warning banners
   - Use HTTPS in production environments
   - Keep dependencies updated

## 🚨 Gmail Setup Instructions

1. Enable 2-Step Verification on your Google Account:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Under "Signing in to Google," select 2-Step Verification
   - Follow the setup steps

2. Generate an App Password:
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and "Other (Custom name)" as the app
   - Enter a name (e.g., "Phishing Simulator")
   - Click "Generate"
   - Use the generated 16-character password in your `.env` file as `SENDER_PASSWORD`
- Email simulations are clearly marked as educational content
- No actual malicious code is executed
- All activities are logged for educational review
- Designed for authorized educational use only

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is designed for educational and authorized testing purposes only. Users must ensure they have proper authorization before cloning any websites or conducting phishing simulations. The developers are not responsible for any misuse of this tool.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/phishing-simulation-tool/issues) page
2. Create a new issue with detailed information
3. Contact the development team

## 🙏 Acknowledgments

- Bootstrap for the responsive UI framework
- Font Awesome for icons
- ReportLab for PDF generation
- Flask community for the excellent web framework
