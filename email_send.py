import smtplib
from email.mime.text import MIMEText
import pyrebase
import ed_email
from urllib.parse import quote


config={
  "apiKey": "AIzaSyAUlsLdMJS7q_mdU9RZl4iFZd4yPBUlcXI",
  "authDomain": "aiauto-7cc64.firebaseapp.com",
  "databaseURL": "https://aiauto-7cc64-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "aiauto-7cc64",
  "storageBucket": "aiauto-7cc64.appspot.com",
  "messagingSenderId": "447608317094",
  "appId": "1:447608317094:web:83634606c2d1800563c067",
  "measurementId": "G-PCE3YXT91M",
}


# configraw="firebase.json"
# with open(configraw, "r") as file:
#     # Load the JSON data into a Python variable
#     config= json.load(file)
# print(config)

firebase = pyrebase.initialize_app(config)  
db=firebase.database()
auth=firebase.auth()



def send_mail(data):

    # Set up the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the email message
    sender_email = "t.r.shyam0007@gmail.com"#consided as webpage mail
    sender_password="fvam btzk exbf ivxz"
    receiver_email = "ktraveendran25@gmail.com"#consided as college
    subject = "New user sign-up request"
    message =f"Username: {data['username']}\nEmail: {data['email']}\nCompany Name:{data['company_name']}\n Requter Name:{data['requter_name']}\nCompanyId:{data['company_id']} http://127.0.0.1:5000/admin-auth"


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


    sender_email = "t.r.shyam0007@gmail.com"#consided as webpage mail
    sender_password="fvam btzk exbf ivxz"
    receiver_email = reciverMail #consided as college
    # print(receiver_email)
    subject = "New user sign-up request"
    message=f"'yOU CAN ABLE TO SET PASSWORD THROUGH THIS'  http://127.0.0.1:5000/password?email={receiver_email}"
    print(message)
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

    users = db.child("company_users")
    users_data = users.get().val()

    encode_email=ed_email.encode_email(data["email"])
    print(encode_email)
    print(encode_email)
    print(encode_email)
    print(encode_email)
    print(encode_email)
    print(encode_email)
    print(encode_email)
    print(encode_email)

    if users_data is not None and data["username"] in users_data:
        print("User with email already exists.")
    else:
        # Set the user data with the encoded email as the key
        data["status"] = "None"
        db.child("company_users").child(encode_email).set(data)
        print("User added successfully.")
 

# def create_db(data):
#     # db.child("company_users").child(data["username"]).set(data)

#     users=db.child("company_users")#LIST OF USERS ADDED IN THE REALTIME DATABASE
#     users_data = users.get().val()
#     encoded_email = quote(data["email"], safe="")
#     print(encoded_email)
#     print(users_data)

#     if users_data is not None and encoded_email in users_data:
#         print("Username exists.")
#     else:
#         data["status"]="None"
#         db.child("company_users").child(encoded_email).set(data)
#         print("Username does not exist.")

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
    
def user_info(email):
    # Get the data from the Realtime Database
    user = db.child("company_users").child(email)
    user_data = user.get().val()
    return user_data

def display_data():
    # Get the data from the Realtime Database
    user = db.child("company_users").child()
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

def sign_in(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        # print(type(user))
        admin=user["email"]
        if admin=='t.r.shyam0007@gmail.com':
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




# s=sign_in("t.r.shyam0007@gmail.com","shyam1134")
# print(s)
# user_data = {
#         "username": "shymeaah",
#         "email": "shyam113232",
#         "password": "sddfgteow3784ry89723yr78w34ry w47890rty780w3gryq3"
#         }
# create_db(user_data)
# # display_data()





# username="sweiufhjs"
# email= "shaa@gmail.com"
# password="123456789987654321"


# s=sign_in(email,password)
# if sign_in(email,password)==True:
#     print("user signed is")

