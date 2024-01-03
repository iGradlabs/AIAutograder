from flask import *
import Models.firebase as fb


admin = Blueprint('admin', __name__, template_folder='/templates')


@admin.route("/admin-auth", methods=['GET'])
def admin_auth():
    if 'email' in session:
        usersData=fb.display_data()
        return render_template('admin/admin-auth.html',usersData=usersData)
    else:
        return redirect(url_for('login_process.sign_in'))