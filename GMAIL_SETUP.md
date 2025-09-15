# Gmail SMTP Setup Guide

This guide will help you configure Gmail SMTP for sending real emails in the phishing simulation tool.

## Prerequisites

1. A Gmail account
2. Two-Factor Authentication (2FA) enabled on your Gmail account

## Step 1: Enable Two-Factor Authentication

1. Go to your [Google Account settings](https://myaccount.google.com/)
2. Click on "Security" in the left sidebar
3. Under "Signing in to Google", click on "2-Step Verification"
4. Follow the prompts to enable 2FA using your phone number

## Step 2: Generate an App Password

1. After enabling 2FA, go back to the Security section
2. Under "Signing in to Google", click on "App passwords"
3. You may need to sign in again
4. In the "Select app" dropdown, choose "Mail"
5. In the "Select device" dropdown, choose "Other (Custom name)"
6. Enter a name like "Phishing Simulation Tool"
7. Click "Generate"
8. **Important**: Copy the 16-character app password that appears (it will look like: `abcd efgh ijkl mnop`)

## Step 3: Configure Environment Variables

**CRITICAL**: The password you provided (`Sanju1433s`) appears to be your regular Gmail password. For Gmail SMTP to work, you MUST use an App Password instead.

1. Open the `.env` file in your project root
2. Update the following variables with your Gmail credentials:

```env
SENDER_EMAIL=demoone913@gmail.com
SENDER_PASSWORD=your-16-character-app-password-here
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**Important Notes:**
- Use your regular Gmail address for `SENDER_EMAIL` (demoone913@gmail.com)
- **Replace `Sanju1433s` with the 16-character app password from Step 2**
- The app password will look like: `abcd efgh ijkl mnop` (remove spaces when entering)
- Do NOT use your regular Gmail password

## Step 4: Test the Configuration

1. Start your Flask application: `python run.py`
2. Go to the "Email Simulation" page at http://127.0.0.1:5000/simulation/email
3. Enter a test email address
4. Send a test email to verify the configuration works

## Current Status

 Environment file created with your Gmail address
 **Action Required**: Replace regular password with App Password
 **Action Required**: Enable 2FA and generate App Password

## Troubleshooting

### "Authentication failed" error (Current Issue)
- **Most likely cause**: Using regular Gmail password instead of App Password
- **Solution**: Follow Step 2 to generate an App Password and update `.env`
- Double-check that 2FA is enabled on your Gmail account

### "Connection refused" error
- Check your internet connection
- Verify the SMTP server and port settings
- Some networks may block SMTP traffic on port 587

### Still having issues?
- Try using port 465 with SSL instead of 587 with TLS
- Check if your antivirus or firewall is blocking the connection
- Ensure your Gmail account is not suspended or limited

## Security Best Practices

1. Never commit your `.env` file to version control (already in .gitignore)
2. Use different app passwords for different applications
3. Regularly review and revoke unused app passwords
4. Keep your app passwords secure and don't share them

## Alternative: Using a Local SMTP Server

If you prefer not to use Gmail, you can set up a local SMTP server for testing:

1. Install a local SMTP server like [MailHog](https://github.com/mailhog/MailHog)
2. Update your `.env` file:
   ```env
   SMTP_SERVER=localhost
   SMTP_PORT=1025
   SENDER_EMAIL=test@localhost
   SENDER_PASSWORD=
   ```

## Quick Fix for Testing

If you want to test the application immediately without setting up Gmail:
- The application will automatically fall back to logging emails locally
- Check the `logs/` directory for email simulation logs
- All functionality will work except actual email deliveryperfectly for testing and development

## No Additional Software Required!
The application uses Python's built-in `smtplib` - no additional software installation needed.
