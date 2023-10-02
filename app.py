from flask import Flask, render_template, request, redirect, url_for, session
import email_send


# flask app name
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth-register-basic.html',methods=['POST','GET'])
def sign_up():

    if request.method == 'POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']

        user_data = {
        "username": username,
        "email": email,
        "password": password
        }
    
        email_send.send_mail(user_data)

    return render_template('auth-register-basic.html')


@app.route("/auth-login-basic.html",methods=['POST','GET'])
def sign_in():
        
    if request.method == 'POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
    return render_template('auth-login-basic.html')









if __name__ == '__main__':
    app.run(debug=True)

    # user_data={}
    # company_users=None
    # def user_sign_up(data):
    #     company_users=None
    #     try:
    #         db.child("company_users").child(data["username"]).set(data)
          
    #         # company_users=data["email"]
    #         company_users=auth.create_user_with_email_and_password(data["email"],'password')
    #     except:
    #         print('User already exist')
    #     return company_users

    #   user_sign_up(user_data)