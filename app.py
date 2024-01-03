# import Controllers.email_send as email_send 
# from flask_session import Session
from dotenv import load_dotenv
from Models.sqlAlcamy import  User,creat_sql_database,get_user_id,delete_user_by_id,update_user
from Models import db

from flask import *
from Routes.login_process import login_process
from Routes.admin import admin
import os



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





app.register_blueprint(login_process)
app.register_blueprint(admin)


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
        return redirect(url_for('login_process.sign_in'))


if __name__ == '__main__':
    create_tables()  
    app.run(debug=True)

