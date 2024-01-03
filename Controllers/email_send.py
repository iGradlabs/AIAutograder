import smtplib
from email.mime.text import MIMEText
import pyrebase
from urllib.parse import quote
import os
from dotenv import load_dotenv

load_dotenv()
reciver_mail_id =  os.getenv("RECIVER_MAIL_ID")
sender_mail_id = os.getenv("SENDER_MAIL_ID")
sender_mail_password = os.getenv("SENDER_MAIL_PASSWORD")
admin_emails = [ str(x) for x in str(os.getenv("ADMIN_MAIL_ID")).split(',')]



def send_mail(data):

    # Set up the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the email message
    sender_email = sender_mail_id #consided as webpage mail
    sender_password=sender_mail_password
    receiver_email = "eniyans644@gmail.com"#consided as college
    subject = "New user sign-up request"
    message =f'''
    Username: {data['first_name']}\n 
    last_name:{data['last_name']}\n 
    Email: {data['email']}\n
    phone_number:{data['phone_number']}\n
    organization:{data['organization']}\n   
    zip_code:{data['zip_code']} \n 
    state:{data['state']} \n 
    country:{data['country']} 
    
    https://aiautodemo.onrender.com/admin-auth'''


    #<<<----- Set up the MIME message ---->>>
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    #<<<----- Set up the MIME message ---->>>


    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    # Send the email


def sendMail_requi(email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    reciverMail=email

    sender_email = sender_mail_id#consided as webpage mail
    
    sender_password= sender_mail_password
    receiver_email = reciverMail #consided as college
    # print(receiver_email)
    
    subject = "New user sign-up request"
    message=f"'yOU CAN ABLE TO SET PASSWORD THROUGH THIS'  https://aiautodemo.onrender.com/password?email={receiver_email}"
    # print(message)

    #     #<<<----- Set up the MIME message ---->>>
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    #<<<----- Set up the MIME message ---->>>
    
       # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    # Send the email

    # pass
def sendMail_reject(email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    reciverMail=email

    sender_email = sender_mail_id#consided as webpage mail
    
    sender_password= sender_mail_password
    receiver_email = reciverMail #consided as college
    # print(receiver_email)
    
    subject = "You have been rejected"
    message=f"'Sorry for that'  https://aiautodemo.onrender.com/password?email={receiver_email}"
    # print(message)

    #     #<<<----- Set up the MIME message ---->>>
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    #<<<----- Set up the MIME message ---->>>
    
       # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    # Send the email

    # pass




# psql 'postgresql://TRshyam:CbzGc1T3mtnp@ep-sparkling-wave-85770255.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'
# psql 'postgresql://TRshyam:CbzGc1T3mtnp@ep-sparkling-wave-85770255.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'