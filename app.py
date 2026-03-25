from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Temporary user storage (no DB)
users = {}

questions = [
    {"question": "Capital of India?", "options": ["Delhi", "Mumbai", "Chennai"], "answer": "Delhi"},
    {"question": "2 + 2?", "options": ["3", "4", "5"], "answer": "4"}
]

@app.route('/')
def home():
    if "user" in session:
        return render_template('index.html', user=session["user"])
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session["user"] = username
            return redirect('/')
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users[username] = password
        return redirect('/login')

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/login')

@app.route('/quiz')
def quiz():
    if "user" not in session:
        return redirect('/login')
    return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for i in range(len(questions)):
        if request.form.get(f"q{i}") == questions[i]["answer"]:
            score += 1
    return render_template('result.html', score=score)
