from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

users = {}
scores = {}

# EASY (15)
easy = [
{"question":"Cloud computing means?","options":["Internet-based service","Local storage","USB storage","None"],"answer":"Internet-based service"},
{"question":"AWS stands for?","options":["Amazon Web Services","Web App System","Advanced Web Service","None"],"answer":"Amazon Web Services"},
{"question":"Cloud uses?","options":["Internet","Cable","USB","Disk"],"answer":"Internet"},
{"question":"Which is SaaS example?","options":["Gmail","CPU","RAM","Hard disk"],"answer":"Gmail"},
{"question":"Azure is owned by?","options":["Microsoft","Google","Amazon","IBM"],"answer":"Microsoft"},
{"question":"Cloud storage means?","options":["Online storage","USB storage","Offline","None"],"answer":"Online storage"},
{"question":"Cloud gives scalability means?","options":["Increase resources","Delete data","Stop system","None"],"answer":"Increase resources"},
{"question":"Which cloud provider is Google?","options":["GCP","AWS","Azure","None"],"answer":"GCP"},
{"question":"Cloud access requires?","options":["Internet","USB","Cable","None"],"answer":"Internet"},
{"question":"Which is public cloud?","options":["AWS","Laptop","Desktop","None"],"answer":"AWS"},
{"question":"Cloud data stored in?","options":["Remote server","Local PC","USB","CD"],"answer":"Remote server"},
{"question":"Cloud computing is?","options":["Online service","Offline tool","Device","None"],"answer":"Online service"},
{"question":"Which device uses cloud?","options":["Mobile","Laptop","Tablet","All"],"answer":"All"},
{"question":"Cloud helps in?","options":["Storage","Processing","Backup","All"],"answer":"All"},
{"question":"Cloud platform example?","options":["AWS","MS Word","Notepad","Excel"],"answer":"AWS"}
]

# MEDIUM (15)
medium = [
{"question":"SaaS full form?","options":["Software as a Service","System as a Service","Server as a Service","None"],"answer":"Software as a Service"},
{"question":"PaaS full form?","options":["Platform as a Service","Process as a Service","Program as a Service","None"],"answer":"Platform as a Service"},
{"question":"IaaS full form?","options":["Infrastructure as a Service","Internet as a Service","Input as a Service","None"],"answer":"Infrastructure as a Service"},
{"question":"Which service gives virtual machines?","options":["IaaS","PaaS","SaaS","None"],"answer":"IaaS"},
{"question":"Which service gives ready apps?","options":["SaaS","PaaS","IaaS","None"],"answer":"SaaS"},
{"question":"AWS EC2 is used for?","options":["Compute","Storage","Database","None"],"answer":"Compute"},
{"question":"AWS S3 is used for?","options":["Storage","Compute","Network","None"],"answer":"Storage"},
{"question":"Cloud region refers to?","options":["Data center location","City","Country","None"],"answer":"Data center location"},
{"question":"Load balancing means?","options":["Distribute traffic","Store data","Delete files","None"],"answer":"Distribute traffic"},
{"question":"Cloud scaling is?","options":["Increase resources","Decrease speed","Delete data","None"],"answer":"Increase resources"},
{"question":"Virtualization means?","options":["Creating virtual machines","Deleting data","Coding","None"],"answer":"Creating virtual machines"},
{"question":"Which ensures security?","options":["Encryption","Firewall","Backup","All"],"answer":"All"},
{"question":"Cloud OS supports?","options":["Linux","Windows","Both","None"],"answer":"Both"},
{"question":"HTTPS is used for?","options":["Secure communication","Data delete","Storage","None"],"answer":"Secure communication"},
{"question":"Which service stores database?","options":["RDS","EC2","Lambda","S3"],"answer":"RDS"}
]

# HARD (15)
hard = [
{"question":"AWS Lambda is an example of?","options":["Serverless computing","Storage","Database","None"],"answer":"Serverless computing"},
{"question":"CDN stands for?","options":["Content Delivery Network","Cloud Data Node","Central Data Network","None"],"answer":"Content Delivery Network"},
{"question":"CloudWatch is used for?","options":["Monitoring","Storage","Compute","None"],"answer":"Monitoring"},
{"question":"Elasticity means?","options":["Auto scaling","Manual scaling","No scaling","None"],"answer":"Auto scaling"},
{"question":"Fault tolerance means?","options":["System continues working","System stops","Deletes data","None"],"answer":"System continues working"},
{"question":"SLA full form?","options":["Service Level Agreement","System Level Access","Storage Level Access","None"],"answer":"Service Level Agreement"},
{"question":"Edge computing means?","options":["Processing near data","Central processing","Offline","None"],"answer":"Processing near data"},
{"question":"Cloud migration means?","options":["Move apps to cloud","Delete apps","Install apps","None"],"answer":"Move apps to cloud"},
{"question":"DevOps stands for?","options":["Development + Operations","Design + Operations","Dev + Output","None"],"answer":"Development + Operations"},
{"question":"CI/CD means?","options":["Continuous Integration & Delivery","Cloud Input Data","Central Integration Data","None"],"answer":"Continuous Integration & Delivery"},
{"question":"Hybrid cloud means?","options":["Public + Private","Public only","Private only","None"],"answer":"Public + Private"},
{"question":"Private cloud means?","options":["Single organization","Public use","Hybrid use","None"],"answer":"Single organization"},
{"question":"Public cloud means?","options":["Shared infrastructure","Private use","Local system","None"],"answer":"Shared infrastructure"},
{"question":"Cloud backup means?","options":["Online backup","Offline backup","USB","None"],"answer":"Online backup"},
{"question":"Cloud monitoring tools?","options":["CloudWatch","Nagios","Zabbix","All"],"answer":"All"}
]

@app.route('/')
def home():
    if "user" not in session:
        return redirect('/login')
    return render_template("index.html", user=session["user"])

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        if u in users and users[u] == p:
            session["user"] = u
            return redirect('/')
        return "Invalid login"
    return render_template("login.html")

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        users[request.form['username']] = request.form['password']
        return redirect('/login')
    return render_template("signup.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/select')
def select():
    return render_template("select.html")

@app.route('/quiz/<level>')
def quiz(level):
    if level == "easy":
        q = easy
    elif level == "medium":
        q = medium
    else:
        q = hard

    session["questions"] = q
    return render_template("quiz.html", questions=q)

@app.route('/result', methods=['POST'])
def result():
    q = session.get("questions", [])
    score = 0

    for i in range(len(q)):
        if request.form.get(f"q{i}") == q[i]["answer"]:
            score += 1

    scores[session["user"]] = score
    return render_template("result.html", score=score, total=len(q))

@app.route('/performance')
def performance():
    user = session["user"]
    user_score = scores.get(user, 0)
    return render_template("performance.html", score=user_score)

@app.route('/tips')
def tips():
    return render_template("tips.html")

if __name__ == "__main__":
    app.run()
