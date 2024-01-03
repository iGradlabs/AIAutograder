from flask import *
# from Routes import user_view
from Controllers import email_send 
from Models.sqlAlcamy import db, User,creat_sql_database,get_user_id,delete_user_by_id,update_user
import Models.firebase as fb
import os


login_process = Blueprint('login_process', __name__, template_folder='/templates')



admin_emails = [ str(x) for x in str(os.getenv("ADMIN_MAIL_ID")).split(',')]



@login_process.route('/auth-register-basic.html',methods=['POST','GET'])
def sign_up():
    # user_data=" "
    mes=''
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
            #create db in firebase & send mail to college
            fb.create_db_fb(user_data)
            email_send.send_mail(user_data)

            return redirect (url_for('login_process.sign_in'))
        
        except Exception as error:
            db.session.rollback()
            print(error)
            w=str(error.orig)
            # # print(w)
            # # w=w.split()[-1:]
            if w:
                mes="User already exist"
    
                
            else:
                mes="error occured"
                
    return render_template('auth-register-basic.html',mes=mes)


@login_process.route("/auth-login-basic.html", methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email-username']
        password = request.form['password']
        # remember_me = request.form.get('rememberMe')
        valid_credentials = fb.sign_in(email, password)

        if valid_credentials:
            user_id = get_user_id(email)
            user_info=fb.user_info(user_id)
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

@login_process.route("/sign-out", methods=['GET'])
def sign_out():
    session.clear()
    return  redirect (url_for('login_process.sign_in'))

@login_process.route('/password',methods=['POST','GET'])
def passwordPage():
    
    message = ""  
    if request.method == 'POST':
        password=request.form['password']
        ConPassword=request.form['ConformPassword']

        if password==ConPassword:
            #get email from the weblink
            email=request.args.get('email')
            authPassword=password
            fb.create_user_id(email,password)
            print(email,authPassword)
            return redirect("/auth-login-basic.html")
        else:
            message="different match on password"
            
    return render_template('password.html',error=message)

@login_process.route('/auth-forgot-password-basic.html',methods=['POST','GET'])
def forgot_password():

    if request.method == 'POST':
        email=request.form['email']

        validation=email_send.forgot_password(email)

        if validation==True:
            msg="Please check your mail for the reset link"
            return redirect (url_for('login_process.sign_in',error=msg))


    return render_template("auth-forgot-password-basic.html")


@login_process.route('/process/<action>/<user_id>/<email>')
def process_user(action, user_id,email):
    approvel=fb.approve(action,user_id)
    if approvel ==  True:
        # User(email)
        email_send.sendMail_requi(email)
    else:
        email_send.sendMail_reject(email)
        delete_user_by_id(user_id)

        print("hey you Fbi open up the door")
    return redirect('/admin-auth')


@login_process.route('/myProfile',methods=['POST','GET'])
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
            # User.update_user(new_username='NewUsername', new_email='newemail@example.com', new_selected_candidates='New candidates', new_exams_generated=5)


            # print(user.update_user(new_username=new_data['first_name'],new_email=new_data['email']))
            update_user(session['user_id'],new_username=new_data['first_name'],email=new_data['email'])
            user_info=fb.user_info(session['user_id'],new_data=new_data)
            # User.update_user(new_username='NewUsername', new_email='newemail@example.com', new_selected_candidates='New candidates', new_exams_generated=5)

            session['user_info']=user_info

            
            
        if request.form['action']=='reset':
            return render_template('account/myProfil.html',user_info=user_info)
    
    return render_template('account/myProfil.html',user_info=user_info)

@login_process.route('/myProfile/Deactivate',methods=['POST','GET'])
def deactivate():
    if request.method == 'POST':
        Deactivate=request.form.get('Deactivation')
        print(Deactivate)

        if request.form.get('Deactivation') != None:
            
            # print(session['user_id'])
            # print(session['user_id'])
            fb.deleteUser(session['user_id'])
            delete_user_by_id(session['user_id'])
            session.clear()
            return redirect(url_for("login_process.sign_in"))
        else:
            return redirect(url_for("login_process.myProfile"))

