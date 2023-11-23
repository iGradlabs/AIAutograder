from flask import Flask, render_template, request
import randomizer1
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input_form', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        language = request.form['language']
        percentage_coding = request.form['percentage_coding']
        tags = request.form.getlist('tags')
        total_marks = request.form['total_marks']
        difficulty_level = request.form['difficulty_level']
        # print(total_marks)
        # print(type(total_marks))
        total_marks=int(total_marks)
        percentage_coding=int(percentage_coding)
        print(type(total_marks))

        randomizer1.main(language, percentage_coding, tags, total_marks, difficulty_level)
        return 'Form submitted successfully!'
    return render_template('main.html',total_marks=total_marks)

    # return render_template('main.html', language=language, percentage_coding=percentage_coding, tags=tags, total_marks=total_marks, difficulty_level=difficulty_level)

if __name__ == '__main__':
    app.run(debug=True)