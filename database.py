import pyrebase

config = {
  "apiKey": "AIzaSyAZOxor8qSBpGNLh4cvSbKgnYiebdaWspQ",
  "authDomain": "realtime-data-159cb.firebaseapp.com",
  "databaseURL": "https://realtime-data-159cb-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "realtime-data-159cb",
  "storageBucket": "realtime-data-159cb.appspot.com",
  "messagingSenderId": "381406793969",
  "appId": "1:381406793969:web:3f93dc6d2d99b3b8b19950",
  "measurementId": "G-C0WZ0WL3SX"
}
firebase = pyrebase.initialize_app(config)  
db=firebase.database()
auth=firebase.auth()

def createDb(id,data1):
    data=db.child(id).child("querys").set(data1)
    
# data={
#     "q1":"hello",
#     "q2":"hellodsicvpjsd",
#     "q3":"helloslkfdv",
#     "q4":"hellosflhfssdvihnisk",
#     "q5":"helloewewew"
#     }

# createDb(data)

# createDb(data)