import os
from flask import Flask, render_template, request, redirect, url_for, session,flash
import email_send,ed_email
from flask_session import Session
from dotenv import load_dotenv
import json

load_dotenv()

# Access the variables
secret_key = os.getenv("SECRET_KEY")
session_type = os.getenv("SESSION_TYPE")
admin_emails = [ str(x) for x in str(os.getenv("ADMIN_MAIL_ID")).split(',')]

# flask app namess

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key  
app.config['SESSION_TYPE'] =  session_type 





@app.route('/')
def index():
    if 'email' in session:
        print(session)
        # print(email_send.display_data())

        return render_template('dashboard.html',username=session['user_info']['username'])
    else:
        return redirect(url_for('sign_in'))

    



@app.route('/auth-register-basic.html',methods=['POST','GET'])
def sign_up():

    if request.method == 'POST':
        username=request.form['username']
        email=request.form['email']
        company_name=request.form['company_name']
        requter_name=request.form['requter_name']
        company_id=request.form['company_id']

        user_data = {
        "username": username,
        "email": email,
        "company_name":company_name,
        "requter_name":requter_name,
        "company_id":company_id
        }
        email_send.create_db(user_data)
        email_send.send_mail(user_data)
        return redirect('auth-login-basic.html')

        

    return render_template('auth-register-basic.html')





@app.route("/auth-login-basic.html", methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email-username']
        password = request.form['password']
        print(email, password)

        #encode & decode email
        encoded_email= ed_email.encode_email(email)
        print(encoded_email)
        user_info=email_send.user_info(encoded_email)
        #encode & decode email



        valid_credentials = email_send.sign_in(email, password)

        if valid_credentials:
            session['email'] = email
            session['is_admin'] = False
            session['user_info']=user_info
            print(session)
            # print(email_send.display_data())
            
            print(session)

            if email in admin_emails: # 
                print(email)
                # print("admibn")
                session['is_admin'] = True
                # return redirect(url_for('admin_auth'))
                return redirect(url_for('index'))

            return redirect(url_for('index'))

        error_message = "Invalid login credentials. Please try again."
        return render_template('auth-login-basic.html', error=error_message)

    return render_template('auth-login-basic.html')


@app.route("/sign-out", methods=['GET'])
def sign_out():
    # Clear the user's session to sign them out
    session.pop('email', None)
    return redirect(url_for('sign_in'))

@app.route("/admin-auth", methods=['GET'])
def admin_auth():
    # email_send.approve(action,user_id)
    usersData=email_send.display_data()
    return render_template('admin-auth.html',usersData=usersData)

@app.route('/password',methods=['POST','GET'])
def passwordPage():
    # if request.method == 'GET':
    #     email=request.args.get('email')
    #     print("defhiugewaiufgh",email)
    message = ""  
    if request.method == 'POST':
        print("heyyyyyyyyyyyyyyyy")
        password=request.form['password']
        ConPassword=request.form['ConformPassword']
        if password==ConPassword:
            email=request.args.get('email')
            authPassword=password
            email_send.create_user_id(email,password)
            print(email,authPassword)
            return redirect("/auth-login-basic.html")
        else:
            message="different match on password"
            
    return render_template('password.html',error=message)

@app.route('/process/<action>/<user_id>/<email>')
def process_user(action, user_id,email):
    approvel=email_send.approve(action,user_id)
    if approvel ==  True:
        email_send.sendMail_requi(email)
    else:
        print("hey you Fbi open up the door")
    return redirect('/admin-auth')



@app.route('/auth-forgot-password-basic.html',methods=['POST','GET'])
def forgot_password():

    if request.method == 'POST':
        email=request.form['email']

        validation=email_send.forgot_password(email)

        if validation==True:
            msg="Please check your mail for the reset link"
            return render_template("auth-forgot-password-basic.html",message=msg)


    return render_template("auth-forgot-password-basic.html")


@app.route('/filter_candidates')
def filter_candidates():
    return render_template('Filter_candidates.html')

@app.route('/job_posting')
def job_posting ():
    return render_template('job_posting.html')

@app.route('/create_learning_path')
def create_learning_path():
    return render_template('create_learning_path.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/schedule_interview')
def schedule_interview():
    return render_template('schedule_interview.html')




if __name__ == '__main__':
    app.run(debug=True)

