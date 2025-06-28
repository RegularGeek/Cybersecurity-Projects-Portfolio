# Basic phishing email analyzer
import re

def analyze_email(email_content):
    links = re.findall(r'https?://\S+', email_content)
    keywords = ['password', 'urgent', 'verify', 'click here', 'account suspended']
    found_keywords = [word for word in keywords if word in email_content.lower()]

    print("Links found:", links)
    print("Suspicious keywords found:", found_keywords)

if __name__ == "__main__":
    email = input("Paste email content here:\n")
    analyze_email(email)
