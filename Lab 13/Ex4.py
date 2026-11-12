from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Quiz questions
QUESTIONS = [
    {
        'question': 'Which keyword creates a function in Python?',
        'options': ['function', 'def', 'create'],
        'answer': 'def'
    },
    {
        'question': 'What does Flask use to display an HTML template?',
        'options': ['render_template', 'print', 'input'],
        'answer': 'render_template'
    },
    {
        'question': 'Which method sends this quiz form?',
        'options': ['GET', 'POST', 'DELETE'],
        'answer': 'POST'
    }
]

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Quiz page
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0

        for i, question in enumerate(QUESTIONS):
            if request.form.get('q' + str(i)) == question['answer']:
                score += 1

        return redirect(url_for('result', score=score))

    return render_template('quiz.html', questions=QUESTIONS)

# Result page
@app.route('/result')
def result():
    score = request.args.get('score', 0, type=int)
    return render_template('result.html',
                           score=score,
                           total=len(QUESTIONS))

if __name__ == '__main__':
    app.run(debug=True)
