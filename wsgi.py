from exerciseapp import app, socketio
from exerciseapp.database import database

if __name__ == '__main__':
    with app.app_context(): 
        database.create_all()
    socketio.run(app, use_reloader=False, debug=True)