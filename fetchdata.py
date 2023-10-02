# import imapclient
# import email
# from email.header import decode_header


# def fetch_specific_email(subject_keyword):
#     result = {}
#     with imapclient.IMAPClient('imap.gmail.com') as client: 

#         sender_email = "t.r.shyam0007@gmail.com"  # Considered as webpage mail
#         sender_password = "fvam btzk exbf ivxz"
#         client.login(sender_email, sender_password)

#         client.select_folder('INBOX')

#         # Search for emails based on subject
#         email_ids = client.search(['SUBJECT', subject_keyword])

#         if email_ids:
#             # Fetch the first matching email
#             email_id = email_ids[-1]
#             email_data = client.fetch([email_id], ['BODY[]'])

#             # Get the raw email 
#             raw_email = email_data[email_id][b'BODY[]']
#             msg = email.message_from_bytes(raw_email)


#             # Extract the message body
#             message_body = ""

#             if msg.is_multipart():
#                 for part in msg.walk():
#                     if part.get_content_type() == "text/plain":
#                         message_body += part.get_payload(decode=True).decode("utf-8")
#             else:
#                 message_body = msg.get_payload(decode=True).decode("utf-8")

    
#             result["Subject"] = msg["Subject"]
#             result["From"] = msg["From"]
#             result["To"] = msg["To"]
#             result["Body"] = message_body
 
#         client.logout()
#     return result
        

# # email_info=fetch_specific_email("Re: New user sign-up request")
# # # print(email_info)
# # # print( email_info["Body"].split()[0])

# # if  email_info["Body"].split()[0].lower() =="yes":
# #     print(email_info["Body"])
# #     # email_send.create_db()
# #     print ("User is verified")

# # elif email_info["Body"].split()[0].lower() =="no":
# #     print(email_info["Body"])
# #     print("User not verified by the college")

# # else:
# #     print("Invalid input")








# # if email_info:
# #     print("Subject:", email_info["Subject"])
# #     print("From:", email_info["From"])
# #     print("To:", email_info["To"])
# #     print("Body:", email_info["Body"])
# # else:
# #     print("Email not found.")