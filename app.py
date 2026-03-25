from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

users = {}
scores = {}

# EASY (15)
easy = [
{"question":"Cloud means?","options":["Internet","CPU","RAM","None"],"answer":"Internet"},
{"question":"AWS stands for?","options":["Amazon Web Services","Web System","None","Server"],"answer":"Amazon Web Services"},
{"question":"Cloud uses?","options":["Internet","Disk","USB","None"],"answer":"Internet"},
{"question":"Which is SaaS?","options":["Gmail","CPU","Disk","None"],"answer":"Gmail"},
{"question":"Azure by?","options":["Microsoft","Google","Amazon","IBM"],"answer":"Microsoft"},
{"question":"Cloud storage?","options":["Online","Offline","USB","None"],"answer":"Online"},
{"question":"Cloud gives?","options":["Scalability","Speed","Cost","All"],"answer":"All"},
{"question":"Cloud access?","options":["Internet","USB","Offline","None"],"answer":"Internet"},
{"question":"Which cloud?","options":["AWS","Laptop","USB","None"],"answer":"AWS"},
{"question":"Cloud is?","options":["Online","Offline","Local","None"],"answer":"Online"},
{"question":"Cloud uses?","options":["Server","USB","Cable","None"],"answer":"Server"},
{"question":"Cloud data?","options":["Remote","Local","USB","None"],"answer":"Remote"},
{"question":"Which is GCP?","options":["Google Cloud","Amazon","Azure","None"],"answer":"Google Cloud"},
{"question":"Cloud benefit?","options":["Flexibility","Speed","Cost","All"],"answer":"All"},
{"question":"Cloud service?","options":["Online","Offline","USB","None"],"answer":"Online"}
]

# MEDIUM (15)
medium = [
{"question":"SaaS full form?","options":["Software as a Service","None","System","Server"],"answer":"Software as a Service"},
{"question":"PaaS full form?","options":["Platform as a Service","Program","None","Server"],"answer":"Platform as a Service"},
{"question":"IaaS full form?","options":["Infrastructure as a Service","Internet","None","Server"],"answer":"Infrastructure as a Service"},
{"question":"Which provides VM?","options":["IaaS","SaaS","PaaS","None"],"answer":"IaaS"},
{"question":"Which provides apps?","options":["SaaS","PaaS","IaaS","None"],"answer":"SaaS"},
{"question":"Which handles platform?","options":["PaaS","IaaS","SaaS","None"],"answer":"PaaS"},
{"question":"AWS EC2 is?","options":["Compute","Storage","Network","None"],"answer":"Compute"},
{"question":"AWS S3 is?","options":["Storage","Compute","DB","None"],"answer":"Storage"},
{"question":"Cloud region?","options":["Data center","City","Country","None"],"answer":"Data center"},
{"question":"Load balancing?","options":["Distribute load","Store data","Delete","None"],"answer":"Distribute load"},
{"question":"Cloud scaling?","options":["Auto scale","Manual","None","USB"],"answer":"Auto scale"},
{"question":"Cloud security?","options":["Encryption","Firewall","Backup","All"],"answer":"All"},
{"question":"Virtualization?","options":["VM creation","Delete","None","USB"],"answer":"VM creation"},
{"question":"Cloud protocol?","options":["HTTP","HTTPS","FTP","All"],"answer":"All"},
{"question":"Cloud OS?","options":["Linux","Windows","Both","None"],"answer":"Both"}
]

# HARD (15)
hard = [
{"question":"AWS Lambda is?","options":["Serverless","Storage","Compute","None"],"answer":"Serverless"},
{"question":"CDN stands for?","options":["Content Delivery Network","None","Server","Cloud"],"answer":"Content Delivery Network"},
{"question":"CloudWatch is?","options":["Monitoring","Storage","Compute","None"],"answer":"Monitoring"},
{"question":"Elasticity means?","options":["Auto scale","Manual","None","USB"],"answer":"Auto scale"},
{"question":"Fault tolerance?","options":["System continues","Stops","Delete","None"],"answer":"System continues"},
{"question":"SLA full form?","options":["Service Level Agreement","None","Server","System"],"answer":"Service Level Agreement"},
{"question":"Edge computing?","options":["Near data","Central","Offline","None"],"answer":"Near data"},
{"question":"Cloud migration?","options":["Move to cloud","Delete","Install","None"],"answer":"Move to cloud"},
{"question":"DevOps?","options":["Development+Operations","Testing","Design","None"],"answer":"Development+Operations"},
{"question":"CI/CD?","options":["Continuous Integration & Delivery","None","Server","System"],"answer":"Continuous Integration & Delivery"},
{"question":"Hybrid cloud?","options":["Public+Private","Public","Private","None"],"answer":"Public+Private"},
{"question":"Private cloud?","options":["Single org","Public","Hybrid","None"],"answer":"Single org"},
{"question":"Public cloud?","options":["Shared","Private","None","Local"],"answer":"Shared"},
{"question":"Cloud backup?","options":["Online","Offline","USB","None"],"answer":"Online"},
{"question":"Cloud monitoring?","options":["Tracking","Deleting","None","USB"],"answer":"Tracking"}
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
