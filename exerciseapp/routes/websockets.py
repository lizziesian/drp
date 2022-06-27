from flask_socketio import send, emit

from exerciseapp import socketio
from exerciseapp.database import database
from exerciseapp.models.user import ChildUser

# Used to test socket is correctly connected. 
@socketio.on("connected")
def handle_connection(json):
    print("server received event: " + str(json))

# Parental approval/denial
@socketio.on("parental confirmation")
def handle_parental_confirmation(json, methods=['GET', 'POST']):
    child_id = int(json['child'])
    parent_id = int(json['parent'])
    result = json['decision']
    status = parent_update_status(child_id, result)
    new_json = {'child': child_id, 'parent': parent_id, 'status': status}
    socketio.emit("status updated", new_json)

# Update the child with id <child_id> based on the decision argument from the parental confirmation. 
def parent_update_status(child_id, decision):
    child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    status = 3
    if decision == "approved":
        status = 4
    if decision == "denied":
        status = 0
    child.mission_status = status
    child.status_confirmed = True
    database.session.commit()
    return status

# Child has watched an exercise video
@socketio.on("video watched")
def handle_video_watched(json, methods=['GET', 'POST']):
    child_id = int(json['child'])
    parent_id = int(json['parent'])
    old_status = int(json['status'])
    status = child_update_status(child_id, old_status)
    new_json = {'child': child_id, 'parent': parent_id, 'status': status}
    socketio.emit("status updated", new_json)

def child_update_status(child_id, old_status):
    child = ChildUser.query.get_or_404(child_id, "Child user not found.")
    status = old_status + 1
    child.mission_status = status
    database.session.commit()
    return status