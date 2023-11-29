from flask_sqlalchemy import SQLAlchemy

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
    

    