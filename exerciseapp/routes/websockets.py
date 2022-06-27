from flask_socketio import send, emit

from exerciseapp import socketio
from exerciseapp.database import database
from exerciseapp.models.user import ChildUser

@socketio.on("connected")
def handle_connection(json):
    print("received my event: " + str(json))

# Parental approval/denial
@socketio.on("parental confirmation")
def handle_parental_confirmation(json, methods=['GET', 'POST']):
    child_id = int(json['child'])
    parent_id = int(json['parent'])
    result = json['decision']
    status = update_status(child_id, result)
    new_json = {'child': child_id, 'parent': parent_id, 'status': status}
    socketio.emit("status updated", new_json)

# Update the child with id <child_id> based on the decision argument from the parental confirmation. 
def update_status(child_id, decision):
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