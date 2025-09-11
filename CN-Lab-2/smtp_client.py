import smtplib
from email.message import EmailMessage
import getpass

def send_email():
    """Connects to an SMTP server and sends an email."""
    
    # --- Configuration ---
    # Update these with your details
    smtp_server = "smtp.gmail.com"  # Example for Gmail
    smtp_port = 587
    sender_email = "your_email@gmail.com" # Your email address
    receiver_email = "recipient_email@example.com" # Recipient's email address
    
    # --- IMPORTANT ---
    # Use an "App Password" if you have 2-Factor Authentication enabled on your account.
    # Do not hardcode your password. getpass prompts you securely.
    try:
        password = getpass.getpass(prompt=f"Enter App Password for {sender_email}: ")
    except Exception as error:
        print('ERROR', error)
        return

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = "Test Email from Python SMTP Client"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content("This is a test email sent from a Python script for the Computer Networks lab assignment.")

    print(f"\n--- Attempting to send email from {sender_email} to {receiver_email} ---")
    
    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Set a debug level of 1 to log the communication process
            server.set_debuglevel(1)
            
            # Start TLS for security
            server.starttls()
            
            # Login to the email account
            server.login(sender_email, password)
            
            # Send the email
            server.send_message(msg)
            
            print("\n✅ Email sent successfully!")
            
    except smtplib.SMTPAuthenticationError:
        print("\n❌ Error: Authentication failed. Please check your email/password and ensure you are using an 'App Password' if 2FA is enabled.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    send_email()
