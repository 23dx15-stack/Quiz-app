from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# User storage
users = {}

# 50 Cloud Computing Questions
questions = [
{"question":"What is Cloud Computing?","options":["Local storage","Internet-based computing","Hardware","None"],"answer":"Internet-based computing"},
{"question":"Which service model provides virtual machines?","options":["SaaS","PaaS","IaaS","DaaS"],"answer":"IaaS"},
{"question":"Which model provides ready apps?","options":["IaaS","PaaS","SaaS","None"],"answer":"SaaS"},
{"question":"Which cloud is public?","options":["AWS","Private cloud","Local server","None"],"answer":"AWS"},
{"question":"Which company provides Azure?","options":["Google","Microsoft","Amazon","IBM"],"answer":"Microsoft"},
{"question":"Which is a cloud platform?","options":["Windows","AWS","Linux","MS Word"],"answer":"AWS"},
{"question":"Full form of SaaS?","options":["Software as a Service","Storage as a Service","Server as a Service","None"],"answer":"Software as a Service"},
{"question":"Full form of PaaS?","options":["Platform as a Service","Program as a Service","Process as a Service","None"],"answer":"Platform as a Service"},
{"question":"Full form of IaaS?","options":["Infrastructure as a Service","Internet as a Service","Input as a Service","None"],"answer":"Infrastructure as a Service"},
{"question":"Which storage used in cloud?","options":["Block storage","Cloud storage","File storage","All"],"answer":"All"},

{"question":"Which service scales automatically?","options":["Cloud","Local PC","USB","None"],"answer":"Cloud"},
{"question":"Which is cloud provider?","options":["Amazon","Google","Microsoft","All"],"answer":"All"},
{"question":"Which deployment model is private?","options":["Private","Public","Hybrid","Community"],"answer":"Private"},
{"question":"Hybrid cloud is combination of?","options":["Public & Private","Public only","Private only","None"],"answer":"Public & Private"},
{"question":"Which is database service?","options":["RDS","EC2","S3","Lambda"],"answer":"RDS"},
{"question":"Which is compute service?","options":["S3","EC2","RDS","None"],"answer":"EC2"},
{"question":"Which is storage service?","options":["S3","EC2","Lambda","RDS"],"answer":"S3"},
{"question":"Which AWS service is serverless?","options":["Lambda","EC2","S3","RDS"],"answer":"Lambda"},
{"question":"Which cloud is scalable?","options":["Cloud","Laptop","Desktop","None"],"answer":"Cloud"},
{"question":"Which uses internet?","options":["Cloud","Offline","USB","None"],"answer":"Cloud"},

{"question":"Which is cloud security tool?","options":["Firewall","Antivirus","Encryption","All"],"answer":"All"},
{"question":"Which ensures data safety?","options":["Backup","Encryption","Firewall","All"],"answer":"All"},
{"question":"Which is cloud advantage?","options":["Scalability","Flexibility","Cost","All"],"answer":"All"},
{"question":"Which is disadvantage?","options":["Security risk","Internet dependency","Downtime","All"],"answer":"All"},
{"question":"Which service is Google cloud?","options":["GCP","AWS","Azure","None"],"answer":"GCP"},
{"question":"Which is virtualization?","options":["Creating virtual machine","Deleting files","Coding","None"],"answer":"Creating virtual machine"},
{"question":"Which tool for virtualization?","options":["VMware","VirtualBox","Hyper-V","All"],"answer":"All"},
{"question":"Which is cloud OS?","options":["Windows","Linux","Both","None"],"answer":"Both"},
{"question":"Which protocol used?","options":["HTTP","HTTPS","FTP","All"],"answer":"All"},
{"question":"Which is SaaS example?","options":["Gmail","Google Docs","Dropbox","All"],"answer":"All"},

{"question":"Which is PaaS example?","options":["Heroku","Google App Engine","Azure App Service","All"],"answer":"All"},
{"question":"Which is IaaS example?","options":["AWS EC2","Azure VM","Google Compute","All"],"answer":"All"},
{"question":"Which handles infrastructure?","options":["IaaS","PaaS","SaaS","None"],"answer":"IaaS"},
{"question":"Which handles platform?","options":["PaaS","SaaS","IaaS","None"],"answer":"PaaS"},
{"question":"Which handles software?","options":["SaaS","IaaS","PaaS","None"],"answer":"SaaS"},
{"question":"Which is public cloud?","options":["AWS","Azure","GCP","All"],"answer":"All"},
{"question":"Which is cloud region?","options":["Data center location","Country","City","None"],"answer":"Data center location"},
{"question":"Which is load balancing?","options":["Distribute traffic","Store data","Delete data","None"],"answer":"Distribute traffic"},
{"question":"Which ensures availability?","options":["Redundancy","Backup","Replication","All"],"answer":"All"},
{"question":"Which is CDN?","options":["Content delivery network","Data center","Storage","None"],"answer":"Content delivery network"},

{"question":"Which is cloud monitoring?","options":["CloudWatch","Nagios","Zabbix","All"],"answer":"All"},
{"question":"Which is serverless computing?","options":["No server management","Hardware free","Manual setup","None"],"answer":"No server management"},
{"question":"Which is elasticity?","options":["Auto scaling","Manual scaling","No scaling","None"],"answer":"Auto scaling"},
{"question":"Which is fault tolerance?","options":["System continues working","Stops working","Deletes data","None"],"answer":"System continues working"},
{"question":"Which is SLA?","options":["Service Level Agreement","Storage Level Access","Server Load Access","None"],"answer":"Service Level Agreement"},
{"question":"Which is edge computing?","options":["Processing near data","Central processing","Offline","None"],"answer":"Processing near data"},
{"question":"Which is cloud backup?","options":["Online backup","Offline backup","USB","None"],"answer":"Online backup"},
{"question":"Which is cloud migration?","options":["Moving apps to cloud","Deleting apps","Installing apps","None"],"answer":"Moving apps to cloud"},
{"question":"Which is DevOps?","options":["Development + Operations","Design","Testing","None"],"answer":"Development + Operations"},
{"question":"Which is CI/CD?","options":["Continuous Integration","Continuous Delivery","Both","None"],"answer":"Both"}
]

@app.route('/')
def home():
    if "user" in session:
        return render_template("index.html", user=session["user"])
    return redirect('/login')

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

@app.route('/quiz')
def quiz():
    return render_template("quiz.html", questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for i in range(len(questions)):
        if request.form.get(f"q{i}") == questions[i]["answer"]:
            score += 1
    return render_template("result.html", score=score)
