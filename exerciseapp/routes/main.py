from flask import Blueprint, render_template
from exerciseapp import socketio
from flask_socketio import send, emit

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("select_account.html", title="Home")

@main.route("/test")
def test():
    return render_template("test.html", title="Test")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


# Function to convert status number to string.
def status(status_id):
    if status_id == 0:
        return "Not Started."
    elif status_id == 1:
        return "Warm Up Complete."
    elif status_id == 2:
        return "Exercise Complete."
    elif status_id == 3:
        return "Pending Confirmation" # Confirmation of mission completion.
    else:
        return "Complete."
