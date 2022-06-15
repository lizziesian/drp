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
        return "Pending Confirmation" # Confirmation of warm-up completion.
    elif status_id == 2:
        return "Warm Up Complete."
    elif status_id == 3:
        return "Pending Confirmation" # Confirmation of exercise completion.
    elif status_id == 4:
        return "Exercise Complete."
    elif status_id == 5:
        return "Pending Confirmation" # Confirmation of cool-down completion.
    else:
        return "Complete."