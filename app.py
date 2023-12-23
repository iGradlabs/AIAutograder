import os
from flask import Flask, render_template, request, redirect, url_for, session,flash
import email_send 
from flask_session import Session
from dotenv import load_dotenv
from sqlAlcamy import db, User,creat_sql_database,get_user_id,delete_user_by_id


load_dotenv()

# Access the variables
secret_key = os.getenv("SECRET_KEY")
session_type = os.getenv("SESSION_TYPE")
Database_Url=os.getenv("DATABASE_URL")
# Database_Url="sqlite:///./instance/example.db"
admin_emails = [ str(x) for x in str(os.getenv("ADMIN_MAIL_ID")).split(',')]

# flask app namess


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key  
app.config['SESSION_TYPE'] =  session_type 

# sqlalchemy setup

app.config['SQLALCHEMY_DATABASE_URI'] = Database_Url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def create_tables():
    with app.app_context():
        db.create_all()

@app.context_processor
def inject_userinfo():
    if 'user_info' in session and 'first_name' in session['user_info']:
        username = session['user_info']['first_name']
        return dict(username=username)
    else:
        return {'username': None} 

@app.route('/')
def index():
    if 'email' in session:

        print(session)
        return render_template('dashboard.html', page='home')
    else:
        return redirect(url_for('sign_in'))

    

@app.route('/auth-register-basic.html',methods=['POST','GET'])
def sign_up():
    # user_data=" "
    if request.method == 'POST':

        user_data = {
        "user_id":"",
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email": request.form['email'],
        "phone_number":request.form['phone_number'],
        "organization":request.form['organization'],
        "zip_code":request.form['zip_code'],
        "state":request.form['state'],
        "country":request.form['country'],
        "status": "None"
        }

        try:
            #create user data in Sql
            creat_sql_database(user_data)

            #get user id from sql 
            user_id=get_user_id(user_data['email'])
            user_data['user_id']=user_id
            print(user_data)

            #create db in firebase & send mail to college
            email_send.create_db(user_data)
            email_send.send_mail(user_data)

            return redirect (url_for('sign_in'))
        except Exception as error:
            db.session.rollback()
            w=str(error.orig)
            w=w.split()[-1:]
            if 'user.email' in w:
                print("Email already exist")
         
            elif 'user.username' in w:
                print("Username already exist")
            else:
                print("error occured",error)
    return render_template('auth-register-basic.html')





@app.route("/auth-login-basic.html", methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email-username']
        password = request.form['password']
        # remember_me = request.form.get('rememberMe')

        
        user_id = get_user_id(email)
        user_info=email_send.user_info(user_id)


        valid_credentials = email_send.sign_in(email, password)

        if valid_credentials:
            session['email'] = email 
            session['is_admin'] = False
            session['user_id']=user_id
            session['user_info']=user_info
            print(session)
            # print(email_send.display_data())
            
            print(session)

            if email in admin_emails: # 
                print(email)

                session['is_admin'] = True
                # return redirect(url_for('admin_auth'))
                return redirect(url_for('index'))

            return redirect(url_for('index'))

        error_message = "Invalid login credentials. Please try again."
        return render_template('auth-login-basic.html', error=error_message)

    return render_template('auth-login-basic.html')



@app.route("/sign-out", methods=['GET'])
def sign_out():
    session.clear()
    return redirect(url_for('sign_in'))


@app.route("/admin-auth", methods=['GET'])
def admin_auth():
    usersData=email_send.display_data()
    return render_template('admin/admin-auth.html',usersData=usersData)

@app.route('/password',methods=['POST','GET'])
def passwordPage():
    
    message = ""  
    if request.method == 'POST':
        password=request.form['password']
        ConPassword=request.form['ConformPassword']

        if password==ConPassword:
            #get email from the weblink
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
        # User(email)
        email_send.sendMail_requi(email)
    else:
        email_send.sendMail_reject(email)
        delete_user_by_id(user_id)

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
    return render_template('Filter_candidates.html', page='filter_candidates')

@app.route('/job_posting')
def job_posting ():
    return render_template('job_posting.html',page='job_posting')

@app.route('/create_learning_path')
def create_learning_path():
    return render_template('create_learning_path.html',page='create_learning_path')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html',page='notifications')

@app.route('/schedule_interview')
def schedule_interview():
    return render_template('schedule_interview.html',page='schedule_interview')

@app.route('/myProfile',methods=['POST','GET'])
def myProfile():

    user_info=session['user_info']

    if request.method == 'POST':

        if request.form['action']=='save':
            new_data={
                "first_name":request.form["firstName"],
                "last_name":request.form["lastName"],
                "country":request.form["country"],
                "email":request.form["email"],
                "phone_number":request.form["phoneNumber"] ,
                "state":request.form["state"],
                "zip_code":request.form["zipCode"],
                "organization":request.form["organization"]
            }
            user_info=email_send.user_info(session['user_id'],new_data=new_data)
            session['user_info']=user_info

            
            
        if request.form['action']=='reset':
            return render_template('account/myProfil.html',user_info=user_info)
    
    return render_template('account/myProfil.html',user_info=user_info)

@app.route('/myProfile/Deactivate',methods=['POST','GET'])
def deactivate():
    if request.method == 'POST':
        Deactivate=request.form.get('Deactivation')
        print(Deactivate)

        if request.form.get('Deactivation') != None:
            
            print(session['user_id'])
            print(session['user_id'])
            email_send.deleteUser(session['user_id'])
            delete_user_by_id(session['user_id'])
            session.clear()
            return redirect(url_for("sign_in"))
        else:
            return redirect(url_for("myProfile"))

if __name__ == '__main__':
    create_tables()  
    app.run(debug=True)

