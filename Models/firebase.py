import pyrebase
from Models.sqlAlcamy import creat_sql_database,get_user_id,delete_user_by_id,update_user

import os
from dotenv import load_dotenv

load_dotenv()

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

def create_db_fb(data):

    user_id=get_user_id(data['email'])
    data['user_id']=user_id   
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
    admin_emails = [ str(x) for x in str(os.getenv("ADMIN_MAIL_ID")).split(',')]

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