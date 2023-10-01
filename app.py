from flask import Flask, render_template, request, redirect, url_for, session

#what 
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/create_question')

def second():
    return render_template('sample_form.html')


if __name__ == '__main__':
    app.run(debug=True)
