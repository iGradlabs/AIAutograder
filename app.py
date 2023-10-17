from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    total_marks = request.form['totalMarks']
    mcq_percentage = request.form['mcqQuestionsPercentage']
    coding_percentage = request.form['codingQuestionsPercentage']
    topics = request.form.getlist('topics')
    difficulty_level = request.form['difficultyLevel']


    info_json = {
        "Total Marks": total_marks,
        "MCQ Questions Percentage": mcq_percentage,
        "Coding Questions Percentage": coding_percentage,
        "Topics": topics,
        "Difficulty Level": difficulty_level
    }

    return jsonify(info_json)

if __name__ == '__main__':
    app.run(debug=True)

