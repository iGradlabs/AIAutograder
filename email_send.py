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


config={
  "apiKey": "AIzaSyAUlsLdMJS7q_mdU9RZl4iFZd4yPBUlcXI",
  "authDomain": "aiauto-7cc64.firebaseapp.com",
  "databaseURL": "https://aiauto-7cc64-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "aiauto-7cc64",
  "storageBucket": "aiauto-7cc64.appspot.com",
  "messagingSenderId": "447608317094",
  "appId": "1:447608317094:web:83634606c2d1800563c067",
  "measurementId": "G-PCE3YXT91M"
}



firebase = pyrebase.initialize_app(config)  
db=firebase.database()
auth=firebase.auth()


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



def create_db(data):   
    db.child("company_users").child(data['user_id']).set(data)
    

def approve(action,user_id):

    if action == 'approve':
        db.child("company_users").child(user_id).update({"status": "approved"})
        return True

    elif action == 'reject':
        db.child("company_users").child(user_id).update({"status": "rejected"})

        # db.child("users").child(user_id).remove()
        return False
    else:
        return "invalid option"
    
def user_info(user_id,new_data=None):
    # Get the data from the Realtime Database
    user = db.child("company_users").child(user_id)
    if new_data is None:
        user_data = user.get().val()
        return user_data
    else:
        user_data=user.update(new_data)
        return user_data
    
    
def display_data():
    # Get the data from the Realtime Database
    user = db.child('company_users')
    user_data = user.get().val()
    return user_data



def create_user_id(email,password):  
        try:
            user = auth.create_user_with_email_and_password(email,password)
            print("User created successfully.")
            return user
        except Exception as e:
            print("Error creating user:", str(e))
            return None

def deleteUser(user_id):
    try:
        db.child("company_users").child(user_id).remove()
        return True
    except Exception as e:
        print('error deleting user',str(e))



def sign_in(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        # print(type(user))
        admin=user["email"]
        if admin in admin_emails:
            return admin
        return True
    except Exception as e:
        print("Error creating user:", str(e))
        return False
        
def forgot_password(email):
    try:
        user=auth.send_password_reset_email(email)
        print("Request send to mail")
        return True
    except Exception as e:
        print('error',str(e))
# psql 'postgresql://TRshyam:CbzGc1T3mtnp@ep-sparkling-wave-85770255.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'
# psql 'postgresql://TRshyam:CbzGc1T3mtnp@ep-sparkling-wave-85770255.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'