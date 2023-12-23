from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


# Access the variables
secret_key = os.getenv("SECRET_KEY")
session_type = os.getenv("SESSION_TYPE")
Database_Url=os.getenv("DATABASE_URL")

# Creating the SQLAlchemy database object
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'custom_user_table'

    user_id  = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    selected_candidates  = db.Column(db.Text) 
    exams_generated= db.Column(db.Integer,default=None)


    def __repr__(self):
        return '<User %r>' % self.username


def creat_sql_database(user_data):
    user_data_sql=User(email=user_data['email'],username=user_data['first_name'])
    db.session.add(user_data_sql)  
    db.session.commit()      
    
def get_user_id(email):
    user = User.query.filter_by(email=email).first()
    user_id=user.user_id
    
    return user_id

def delete_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True  # Deletion successful
    return False 