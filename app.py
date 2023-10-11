from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/create_question')
def second():
    if request.method == 'POST':
        q1=request.form['Q1']
        q2=request.form['Q2']
        q3=request.form['Q3']
        q4=request.form['Q4']
        q5=request.form['Q5']
        return redirect(url_for('sample_form.html',q1=q1))
        
    return render_template('sample_form.html')


if __name__ == '__main__':
    app.run(debug=True)
