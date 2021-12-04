import os
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
import uuid


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# @login_required decorator
# Credit: https://flask.palletsprojects.com/en/2.0.x/
# patterns/viewdecorators/#login-required-decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if no user is in session
        if "user" not in session:
            flash("Please Log In To View This Page")
            return redirect(url_for("login"))
        # if a user is in session
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/index")
def index():
    breeds = mongo.db.breed_groups.find()
    return render_template("index.html", breeds=breeds)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows users to register to the site and create an account
    to access site features
    """
    if request.method == "POST":
        # check if username already exists on database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists, please select another")
            return redirect(url_for("register"))
            # first check that confirmation password matches
            # password then grab form input values
        if request.form.get("password") != request.form.get(
                "password-confirm"):
            flash("Passwords Must Match")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get(
                "password")),
            "email": request.form.get("email").lower(),
            "is_admin": bool(False),
            "is_verified": bool(False),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows registered user to log in to the site
    """
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                # create session admin user/s (
                # Credit: https://github.com/irasan/hackpride2021)
                check_admin = mongo.db.users.find_one(
                        {"username": request.form.get("username").lower()})
                if check_admin["is_admin"]:
                        session["admin"] = True
                flash(f"""Arooo! Welcome back {request.form.get(
                    "username")}""")
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    """
    Profile page for user in session
    """
    if session["user"]:
        # grab the session user's username from database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # grab only dog profiles created by session user
        user = mongo.db.users.find_one({"username": session["user"]})
        dogs = list(mongo.db.dogs.find(
            {"created_by": ObjectId(user["_id"])}))
        return render_template(
            "profile.html", username=username, dogs=dogs)
    flash("Please log in to view your profile")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Logout user by removing session cookies
    """
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_dog", methods=["GET", "POST"])
@login_required
def add_dog():
    """
    User can add a new dog profile to database
    """
    # Credit: https://github.com/MelindaZhang2020(
    # guidance in using ObjectId)
    if request.method == "POST":
        breed = mongo.db.breed_groups.find_one(
            {"breed_name": request.form.get("breed_group")}
        )
        neutered = bool(True) if request.form.get(
            "neutered") else bool(False)
        user = mongo.db.users.find_one({"username": session["user"]})
        rand = uuid.uuid4()
        dog = {
            "breed_group": ObjectId(breed["_id"]),
            "breed_name": request.form.get("breed_name"),
            "dog_name": request.form.get("dog_name"),
            "age": int(request.form.get("age")),
            "sex": request.form.get("sex"),
            "image_url": request.form.get("image"),
            "size": request.form.get("size"),
            "neutered": neutered,
            "location": request.form.get("location"),
            "personality": request.form.get("personality"),
            "created_by": ObjectId(user["_id"]),
            "reference": str(rand)[:8],
        }
        mongo.db.dogs.insert_one(dog)
        flash(f"""Welcome to the pack {request.form.get(
            "dog_name")}!""")
        return redirect(url_for("profile", username=session["user"]))
    breeds = mongo.db.breed_groups.find().sort("breed_name", 1)
    return render_template("add_dog.html", breeds=breeds)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
