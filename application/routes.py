from application import app, db
from flask import render_template, request, Response, json, redirect, flash, url_for
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
    if (form.validate_on_submit() == True):
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()

        if user and user.get_password(password):
            flash(" {user.first_name} You are successfully lcoursesogged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, try again", "danger")

    return render_template("login.html", title="login", form=form, login=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term=None):

    if(term is None):
        term = "Spring 2019"

    classes = Course.objects.order_by("courseID")

    return render_template("courses.html", coursesData=classes, courses=True, term=term)

@app.route("/register", methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count();
        user_id += 1

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User(user_id = user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        print(user)
        user.save()

        flash("You are successfully registered!")
        return redirect("/index")
    return render_template("register.html", title="register", form=form, register=True)

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