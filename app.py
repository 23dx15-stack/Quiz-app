from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Quiz Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Chennai", "Delhi", "Mumbai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "Java", "All"],
        "answer": "All"
    }
]

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Quiz Page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

# Result Page
@app.route('/result', methods=['POST'])
def result():
    score = 0

    for i, q in enumerate(questions):
        user_answer = request.form.get(f"q{i}")
        if user_answer == q["answer"]:
            score += 1

    return render_template('result.html', score=score, total=len(questions))

# Run App
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)