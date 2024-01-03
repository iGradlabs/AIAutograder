from flask import *
from Controllers import email_send 



recruiter_Page = Blueprint('recruiter_Page', __name__, template_folder='/templates')


@recruiter_Page.route('/filter_candidates')
def filter_candidates():
    return render_template('Filter_candidates.html', page='filter_candidates')

@recruiter_Page.route('/job_posting')
def job_posting ():
    return render_template('job_posting.html',page='job_posting')

@recruiter_Page.route('/create_learning_path')
def create_learning_path():
    return render_template('create_learning_path.html',page='create_learning_path')

@recruiter_Page.route('/notifications')
def notifications():
    return render_template('notifications.html',page='notifications')

@recruiter_Page.route('/schedule_interview')
def schedule_interview():
    return render_template('schedule_interview.html',page='schedule_interview')

