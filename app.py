import os
import uuid
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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


# @is_admin decorator
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


# Pagination
# Credit: https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
# Credit: https://github.com/Edb83/self-isolution/blob/master/app.py
PER_PAGE = 6


def paginated(dogs):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return dogs[offset: offset + PER_PAGE]


def pagination_args(dogs):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(dogs)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


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
    dogs_paginated = paginated(dogs)
    pagination = pagination_args(dogs)
    return render_template(
        "all_dogs.html",
        dogs=dogs_paginated,
        pagination=pagination,
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
        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get(
                "password")),
            "email": request.form.get("email").lower(),
            "is_admin": bool(False),
            "is_verified": bool(False),
        }
        mongo.db.users.insert_one(registration)

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
        reviews = list(mongo.db.reviews.find(
            {"created_by": ObjectId(user["_id"])}))
        for review in reviews:
            review_dog = mongo.db.dogs.find_one(
                {"_id": ObjectId(review["dog_id"])})
            # if dog profile has not been deleted
            if review_dog is not None:
                review["dog_name"] = review_dog["dog_name"]
            else:
                review["dog_name"] = "deleted dog"
        return render_template(
            "profile.html",
            username=username,
            dogs=dogs,
            user=user,
            reviews=reviews)
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
    # keep the same reference number and created_by user
    reference = dog["reference"]
    created_by = dog["created_by"]
    if request.method == "POST":
        breed = mongo.db.breed_groups.find_one(
            {"breed_name": request.form.get("breed_group")}
        )
        neutered = bool(True) if request.form.get(
            "neutered") else bool(False)
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
            "created_by": created_by,
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
    dogs_paginated = paginated(dogs)
    pagination = pagination_args(dogs)
    return render_template(
        "all_dogs.html",
        dogs=dogs_paginated,
        user=user,
        pagination=pagination)


@app.route("/search")
def search():
    """
    Users can search all dog profiles for keywords
    """
    query = request.args.get("query")
    dogs = list(mongo.db.dogs.find({"$text": {"$search": query}}))
    user = mongo.db.users.find_one({"username": session["user"]})
    dogs_paginated = paginated(dogs)
    pagination = pagination_args(dogs)
    flash(f"See results for '{request.args.get('query')}' below")
    return render_template(
        "all_dogs.html",
        user=user,
        dogs=dogs_paginated,
        pagination=pagination)


@app.route("/view_dog/<dog_id>", methods=["GET", "POST"])
@login_required
def view_dog(dog_id):
    """
    Allows user to view individual dog profile page
    Allows user reviews to be added and displayed
    """
    # grab dog profile by its ObjectId
    dog = mongo.db.dogs.find_one({"_id": ObjectId(dog_id)})
    # grab session user
    user = mongo.db.users.find_one({"username": session["user"]})
    # grab user who created the dog profile
    creator = mongo.db.users.find_one({"_id": ObjectId(dog["created_by"])})
    # grab reviews for each dog profile
    reviews = list(mongo.db.reviews.find(
        {"dog_id": ObjectId(dog_id)}))
    # grab creator of review
    for review in reviews:
        review_user = mongo.db.users.find_one(
            {"_id": ObjectId(review["created_by"])})
        # if user has not been deleted
        if review_user is not None:
            review["created_by"] = review_user["username"]
        else:
            review["created_by"] = "deleted user"
    # Credit: add reviews code modified from (
    # https://github.com/irasan/hackpride2021/blob/master/app.py)
    if request.method == "POST":
        # Capitalise each sentence in the user review
        # Credit: see edit_dog above
        review = request.form.get("review")
        review_cap = '. '.join(
            [i.lstrip().capitalize() for i in review.split('.')])
        user_review = {
            "review": review_cap,
            "dog_id": ObjectId(dog_id),
            "created_by": user["_id"],
            "created_on": datetime.now().strftime("%d %B, %Y"),
        }
        mongo.db.reviews.insert_one(user_review)
        flash("Thank You For Your Review")
        return redirect(url_for("view_dog", dog_id=dog_id))
    return render_template(
        "view_dog.html",
        dog=dog,
        user=user,
        creator=creator,
        reviews=reviews)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
@login_required
def edit_review(review_id):
    """
    Allows user or admin to edit reviews
    """
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    # keep dog_id and created_by unchanged
    dog_id = review["dog_id"]
    created_by = review["created_by"]
    if request.method == "POST":
        # Capitalise each sentence in the user review
        # Credit: see edit_dog above
        rev = request.form.get("edit-review")
        review_cap = '. '.join(
            [i.lstrip().capitalize() for i in rev.split('.')])
        update_review = {
            "review": review_cap,
            "dog_id": dog_id,
            "created_by": created_by,
            "created_on": datetime.now().strftime("%d %B, %Y"),
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, update_review)
        flash("Review Updated")
        return redirect(url_for("view_dog", dog_id=dog_id))


@app.route("/delete_review/<review_id>")
@login_required
def delete_review(review_id):
    """
    User can delete reviews they have left
    """
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Removed")
    return redirect(url_for("all_dogs"))


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
        name = username
        # grab only dog profiles created by the user
        user = mongo.db.users.find_one({"username": name})
        dogs = list(mongo.db.dogs.find(
            {"created_by": ObjectId(user["_id"])}))
        reviews = list(mongo.db.reviews.find(
            {"created_by": ObjectId(user["_id"])}))
        for review in reviews:
            review_dog = mongo.db.dogs.find_one(
                {"_id": ObjectId(review["dog_id"])})
            # if dog profile has not been deleted
            if review_dog is not None:
                review["dog_name"] = review_dog["dog_name"]
            else:
                review["dog_name"] = "deleted dog"
        return render_template(
            "profile.html",
            username=username,
            dogs=dogs,
            user=user,
            reviews=reviews)
    flash("Please log in to view profile")
    return redirect(url_for("login"))


@app.route("/verify_user/<user_id>")
@login_required
@is_admin
def verify_user(user_id):
    """
    Allows admin to verify users
    """
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    username = user["username"]
    # if user is already verified
    if user["is_verified"]:
        flash(f"{username} Is Already Verified")
    # verify user
    else:
        mongo.db.users.find_one_and_update(
            {"_id": ObjectId(user_id)}, {"$set": {"is_verified": bool(True)}})
        flash(f"{username} Has Been Verified")
    return redirect(url_for("admin"))


@app.route("/delete_user/<user_id>")
@login_required
@is_admin
def delete_user(user_id):
    """
    Admin can delete user profile from database
    """
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Profile Removed")
    return redirect(url_for("admin"))


@app.errorhandler(400)
def bad_request(error):
    """
    400 error page, code from
    https://flask.palletsprojects.com/en/2.0.x/errorhandling/
    """
    return render_template("400.html", error=error), 400


@app.errorhandler(401)
def unauthorised_access(error):
    """
    401 error page, code from
    https://flask.palletsprojects.com/en/2.0.x/errorhandling/
    """
    return render_template("401.html", error=error), 401


@app.errorhandler(404)
def error404(error):
    """
    404 error page, code from
    https://flask.palletsprojects.com/en/2.0.x/errorhandling/
    """
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def server_error(error):
    """
    500 error page, code from
    https://flask.palletsprojects.com/en/2.0.x/errorhandling/
    """
    return render_template("500.html", error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
