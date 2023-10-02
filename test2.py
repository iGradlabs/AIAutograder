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

auth = firebase.auth()


def reset_password()

# Example usage:

user_data = {
        "username": 'asewaeDD',
        "email": 'fuckyouasss@gmail.com',
        "password": 'asdefwferwdesffew4re'
        }
created_user = create_user_with_email_and_password(user_data)