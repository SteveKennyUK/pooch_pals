import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


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
        return render_template("register.html")
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
                    flash(f"""Arooo! Welcome back {request.form.get(
                        'username')}""")
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
