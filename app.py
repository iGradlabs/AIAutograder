from flask import Flask, render_template, request, redirect, url_for, session,flash
import email_send
from flask_session import Session


# flask app name
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key123123'  # Change this to a secure secret key
app.config['SESSION_TYPE'] = 'filesystem'#types of session are (filesystem,sqlalchemy,mongodb,redis,memcached)





@app.route('/')
def index():
    if 'email' in session:
        print(session)
        return render_template('index.html')
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
        

    return render_template('auth-register-basic.html')





@app.route("/auth-login-basic.html", methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email-username']
        password = request.form['password']
        print(email, password)

        valid_credentials = email_send.sign_in(email, password)

        if valid_credentials:
            session['email'] = email 
            print(session)
            if email == "t.r.shyam0007@gmail.com": 
                session['is_admin'] = True

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



if __name__ == '__main__':
    app.run(debug=True)

