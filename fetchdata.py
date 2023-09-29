import imapclient
import email
from email.header import decode_header

def fetch_specific_email(subject_keyword):

    with imapclient.IMAPClient('imap.gmail.com') as client: 

        sender_email = "t.r.shyam0007@gmail.com"  # Considered as webpage mail
        sender_password = "fvam btzk exbf ivxz"
        client.login(sender_email, sender_password)

        client.select_folder('INBOX')

        # Search for emails based on subject
        email_ids = client.search(['SUBJECT', subject_keyword])

        if email_ids:
            # Fetch the first matching email
            email_id = email_ids[0]
            email_data = client.fetch([email_id], ['BODY[]'])

            # Get the raw email 
            raw_email = email_data[email_id][b'BODY[]']
            msg = email.message_from_bytes(raw_email)


            # Extract the message body
            message_body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        message_body += part.get_payload(decode=True).decode("utf-8")
            else:
                message_body = msg.get_payload(decode=True).decode("utf-8")

            
            print(message_body.split()[-1])

        # Logout when done
        client.logout()

fetch_specific_email("asdfgh")
