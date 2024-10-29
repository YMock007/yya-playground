import imaplib
import email
import os
import re
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Connect to your email server
try:
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
except imaplib.IMAP4.error as e:
    print(f"Login failed: {e}")
    exit()

# Select the mailbox you want to filter (e.g., 'INBOX')
mail.select('INBOX')

# Search for emails from the specified sender
status, messages = mail.search(None, 'FROM "ibanking.alert@dbs.com"')
email_ids = messages[0].split()

# Initialize total amount
total_amount = 0.0
last_total_amount = total_amount  # Store the last total amount for comparison

# Get the list of boss names from the environment variable
BOSS_NAMES = os.getenv('BOSS_NAMES', '').split(',')

# Check if any emails are found
if not email_ids:
    print("No emails found.")
else:
    print("Calculating Total Salary")
    
    for email_id in email_ids:
        try:
            # Fetch the email by ID
            res, msg = mail.fetch(email_id, '(RFC822)')
            msg = email.message_from_bytes(msg[0][1])

            # Filter criteria
            delivered_to = msg['Delivered-To']
            from_header = msg['From']
            subject = msg['Subject']

            if delivered_to == os.getenv('EMAIL_USER') and 'ibanking.alert@dbs.com' in from_header and 'Transaction Alerts' in subject:
                body = ""
                # Extract the email body
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                        elif content_type == "text/html":
                            html_body = part.get_payload(decode=True).decode()
                            soup = BeautifulSoup(html_body, 'html.parser')
                            body = soup.get_text()  # Get text from HTML
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                # Get the date and subtract one day
                email_date = email.utils.parsedate_to_datetime(msg['Date']) - timedelta(days=1)
                formatted_date = email_date.strftime('%Y-%m-%d')

                # Check if any of the boss names are in the email body
                if any(boss_name in body for boss_name in BOSS_NAMES):
                    # Use regex to find the amount in the email body
                    amount_match = re.search(r'You have received SGD ([\d,]+\.\d{2})', body)
                    if amount_match:
                        amount = float(amount_match.group(1).replace(',', ''))
                        total_amount += amount

                        # Print total salary and amount added
                        if total_amount != last_total_amount:
                            print(f'Total Salary = SGD {total_amount:.2f} (Added: SGD {amount:.2f} on {formatted_date})')
                            last_total_amount = total_amount

        except Exception as e:
            print(f"Error processing email ID {email_id}: {e}")

# Logout
mail.logout()
