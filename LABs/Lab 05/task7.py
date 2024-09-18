import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    
    return emails

text = """
Hello, you can reach me at example@example.com.
Also, feel free to contact support@mywebsite.org or feedback123@site.co.uk.
"""
extracted_emails = extract_emails(text)

print("Extracted Email Addresses:")
for email in extracted_emails:
    print(email)
