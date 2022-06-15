from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("select_account.html", title="Home")

# Function to convert status number to string.
def status(status_id):
    if status_id == 0:
        return "Not Started."
    elif status_id == 1:
        return "Warm Up Complete. Exercise Pending."
    elif status_id == 2:
        return "Exercise Complete. Cool Down Pending."
    else:
        return "Complete."