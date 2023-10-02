import smtplib
from email.mime.text import MIMEText
import pyrebase
config={
  'apiKey': "AIzaSyCJW1arUPVjgJRxLYfhX9vbztByaUytAOM",
  'authDomain': "agt1-16b90.firebaseapp.com",
  'projectId': "agt1-16b90",
  'storageBucket': "agt1-16b90.appspot.com",
  'messagingSenderId': "356668542049",
  'appId': "1:356668542049:web:a57f7c56467f8bef51ee20",
  'measurementId': "G-EXR7R90QRQ",
  'databaseURL':" https://agt1-16b90-default-rtdb.asia-southeast1.firebasedatabase.app/"
  }

firebase = pyrebase.initialize_app(config)  
db=firebase.database()
auth=firebase.auth()

def create_db(data):
    # db.child("company_users").child(data["username"]).set(data)

    users=db.child("company_users")#LIST OF USERS ADDED IN THE REALTIME DATABASE
    users_data = users.get().val()
    # print(users_data)

    if users_data is not None and data["username"] in users_data:
        print("Username exists.")
    else:
        db.child("company_users").child(data["username"]).set(data)
        print("Username does not exist.")


def create_user_id(user_data):
        try:
            user = auth.create_user_with_email_and_password(user_data["email"],user_data["password"])
            print("User created successfully.")
            return user
        except Exception as e:
            print("Error creating user:", str(e))
            return None


def send_mail(data):

    # Set up the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the email message
    sender_email = "t.r.shyam0007@gmail.com"#consided as webpage mail
    sender_password="fvam btzk exbf ivxz"
    receiver_email = "ktraveendran25@gmail.com"#consided as rep
    subject = "New user sign-up request"
    message =f"Username: {data['username']}\nEmail: {data['email']}"


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


