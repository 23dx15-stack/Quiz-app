from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5"],
        "answer": "4"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for i in range(len(questions)):
        if request.form.get(f"q{i}") == questions[i]["answer"]:
            score += 1
    return render_template('result.html', score=score)
