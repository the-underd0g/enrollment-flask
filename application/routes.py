from application import app, db
from flask import render_template, request, Response, json
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

coursesData = [
    {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4,
     "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
     "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3,
                       "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4,
     "term": "Fall"}]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form, login=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):

    return render_template("courses.html", coursesData=coursesData, courses=True, term=term)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/enrollment", methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term  = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={ "id": id, "title": title, "term": term})

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if (idx == None):
        jdata = coursesData
    else:
        jdata = coursesData[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/user")
def use():
    User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="asdas").save()
    User(user_id=2, first_name="asda", last_name="Hasdur", email="christian@uta.com", password="asdas").save()

    users = User.objects.all();
    return render_template("user.html", users=users)