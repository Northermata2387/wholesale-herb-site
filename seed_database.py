import os
import json

import crud
import model
import server

os.system("dropdb rising-sun-herbs")
os.system("createdb rising-sun-herbs")


model.connect_to_db(server.app)


with server.app.app_context():
    model.db.create_all()