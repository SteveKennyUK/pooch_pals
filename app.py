import os
import uuid
from functools import wraps
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


# @login_required decorator
# Credit: https://flask.palletsprojects.com/en/2.0.x/
# patterns/viewdecorators/#login-required-decorator
def login_required(f):
    """
    Restrict page access to logged in users only
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if no user is in session
        if "user" not in session:
            flash("Please Log In To View This Page")
            return redirect(url_for("login"))
        # if a user is in session
        return f(*args, **kwargs)
    return decorated_function


# Credit: admin only decorator taken from (
# https://github.com/irasan/hackpride2021/blob/master/app.py)
def is_admin(f):
    """
    Restrict page access to admin users only
    """
    @wraps(f)
    @login_required  # must be logged-in to access this function
    def decorated_function(*args, **kwargs):
        # get session user
        user = mongo.db.users.find_one({"username": session["user"].lower()})
        if not user["is_admin"]:
            flash("This Page Is Restricted To Admin Access")
            return redirect(url_for("index"))
        # user is an admin
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/index")
def index():
    """
    Displays the six most recently added dog profiles
    """
    dogs = list(mongo.db.dogs.find().sort("_id", -1).limit(6))
    return render_template("index.html", dogs=dogs)


@app.route("/breed_groups")
def breed_groups():
    """
    Displays information about dog breed groups
    """
    breeds = list(mongo.db.breed_groups.find())
    return render_template("breed_groups.html", breeds=breeds)


@app.route("/filter/breed_group/<breed_group_id>")
@login_required
def filter_breed_group(breed_group_id):
    """
    Filters dog profiles by breed group
    """
    # Credit: https://github.com/Edb83/self-isolution(
    # guidance in creating a filter)
    breeds = list(mongo.db.breed_groups.find())
    breed = mongo.db.breed_groups.find_one({"_id": ObjectId(breed_group_id)})
    dogs = list(mongo.db.dogs.find({"breed_group": breed["_id"]}))
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template(
        "all_dogs.html",
        dogs=dogs,
        user=user,
        breeds=breeds)


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
    Profile page for user in session or admin user
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
            "profile.html", username=username, dogs=dogs, user=user)
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
        # Capitalise each sentence in the personality description
        # Credit: https://codehandbook.org/
        #     python-capitalize-first-letter-of-all-sentences/
        personality = request.form.get("personality")
        personality_cap = '. '.join(
            [i.lstrip().capitalize() for i in personality.split('.')])
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
            "personality": personality_cap,
            "created_by": ObjectId(user["_id"]),
            "reference": str(rand)[:8],
        }
        mongo.db.dogs.insert_one(dog)
        flash(f"""Welcome to the pack {request.form.get(
            "dog_name").title()}!""")
        return redirect(url_for("profile", username=session["user"]))
    breeds = mongo.db.breed_groups.find().sort("breed_name", 1)
    return render_template("add_dog.html", breeds=breeds)


@app.route("/edit_dog/<dog_id>", methods=["GET", "POST"])
@login_required
def edit_dog(dog_id):
    """
    User can edit their dog profiles and update the database
    """
    dog = mongo.db.dogs.find_one({"_id": ObjectId(dog_id)})
    # keep the same reference number
    reference = dog["reference"]
    if request.method == "POST":
        breed = mongo.db.breed_groups.find_one(
            {"breed_name": request.form.get("breed_group")}
        )
        neutered = bool(True) if request.form.get(
            "neutered") else bool(False)
        user = mongo.db.users.find_one({"username": session["user"]})
        # Capitalise each sentence in the personality description
        # Credit: https://codehandbook.org/
        #     python-capitalize-first-letter-of-all-sentences/
        personality = request.form.get("personality")
        personality_cap = '. '.join(
            [i.lstrip().capitalize() for i in personality.split('.')])
        update_dog = {
            "breed_group": ObjectId(breed["_id"]),
            "breed_name": request.form.get("breed_name"),
            "dog_name": request.form.get("dog_name"),
            "age": int(request.form.get("age")),
            "sex": request.form.get("sex"),
            "image_url": request.form.get("image"),
            "size": request.form.get("size"),
            "neutered": neutered,
            "location": request.form.get("location"),
            "personality": personality_cap,
            "created_by": ObjectId(user["_id"]),
            "reference": reference,
        }
        mongo.db.dogs.update({"_id": ObjectId(dog_id)}, update_dog)
        flash(f"""{request.form.get(
            "dog_name").title()}'s profile updated!""")
        return redirect(url_for("profile", username=session["user"]))
    breeds = mongo.db.breed_groups.find().sort("breed_name", 1)
    return render_template("edit_dog.html", dog=dog, breeds=breeds)


@app.route("/delete_dog/<dog_id>")
@login_required
def delete_dog(dog_id):
    """
    User can delete their dog profile
    """
    mongo.db.dogs.remove({"_id": ObjectId(dog_id)})
    flash("Dog Profile Removed")
    return redirect(url_for("index"))


@app.route("/all_dogs")
@login_required
def all_dogs():
    """
    Displays all dog profiles on database
    """
    dogs = list(mongo.db.dogs.find())
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template("all_dogs.html", dogs=dogs, user=user)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Users can search all dog profiles for keywords
    """
    query = request.form.get("query")
    dogs = list(mongo.db.dogs.find({"$text": {"$search": query}}))
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template("all_dogs.html", dogs=dogs, user=user)


@app.route("/view_dog/<dog_id>", methods=["GET", "POST"])
@login_required
def view_dog(dog_id):
    """
    Allows user to view individual dog profile page
    """
    dog = mongo.db.dogs.find_one({"_id": ObjectId(dog_id)})
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template("view_dog.html", dog=dog, user=user)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Allows users to contact the site
    """
    return render_template("contact.html")


@app.route("/admin")
@login_required
@is_admin
def admin():
    """
    Admin only page
    """
    users = list(mongo.db.users.find())
    return render_template("admin.html", users=users)


@app.route("/profile/admin/<username>", methods=["GET", "POST"])
@login_required
@is_admin
def profile_admin(username):
    """
    Admin user to view all profile pages
    """
    if session["admin"]:
        # grab the username fed through from admin page
        username = username
        # grab only dog profiles created by the user
        user = mongo.db.users.find_one({"username": username})
        dogs = list(mongo.db.dogs.find(
            {"created_by": ObjectId(user["_id"])}))
        return render_template(
            "profile.html", username=username, dogs=dogs, user=user)
        flash("Please log in to view your profile")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
