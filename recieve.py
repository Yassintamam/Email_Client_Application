import imaplib
import email
from email.header import decode_header

try:
    username = 'yassine.tamam3@gmail.com'
    password = 'zpff ugdz odhy lcdv'

    imap_host = 'imap.gmail.com'
    imap = imaplib.IMAP4_SSL(imap_host)

    imap.login('yassine.tamam3@gmail.com', 'zpff ugdz odhy lcdv')
    status, messages = imap.select("INBOX")

    status, message_data = imap.fetch(messages[0], "(RFC822)")
    raw_email = message_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    body = " "

    # If the email is multipart, iterate over email parts
    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            try:
                body += part.get_payload(decode=True).decode()
            except:
                pass
    else:
        body = email_message.get_payload(decode=True).decode()

    # Print the email body
    print("Email Body:")
    print(body)

    imap.logout()

except Exception as e:
        print(f"An error occurred while receiving the email: {str(e)}")
