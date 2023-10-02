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

# <<<----- creating database in firebase to the company users----->>>
firebase = pyrebase.initialize_app(config)  
db=firebase.database()
auth=firebase.auth()

def cr(data):
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




user_data = {
        "username": 'asDeeeD',
        "email": 'assatthesky@gmail.com',
        "password": 'asdefeedfe'
        }

create_user_id(user_data)
# cr(user_data)
