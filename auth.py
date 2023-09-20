import pyrebase

config={
  'apiKey': "AIzaSyCJW1arUPVjgJRxLYfhX9vbztByaUytAOM",
  'authDomain': "agt1-16b90.firebaseapp.com",
  'projectId': "agt1-16b90",
  'storageBucket': "agt1-16b90.appspot.com",
  'messagingSenderId': "356668542049",
  'appId': "1:356668542049:web:a57f7c56467f8bef51ee20",
  'measurementId': "G-EXR7R90QRQ",
  'databaseURL':" "
  }


firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

email=''
password=''

# user=auth.create_user_with_email_and_password(email,password)

user=auth.sign_in_with_email_and_password(email,password)
# print(auth.get_account_info(user['idToken']))

# auth.send_email_verification(user['idToken'])
# print(user)
auth.send_password_reset_email(email)