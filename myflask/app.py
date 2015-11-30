from flask import Flask
from flask_apscheduler import APScheduler
from client_api import client_api
from taxi_api import taxi_api
import sheld
import storage

Flask.tmpl = storage.clientsList
# print(Flask.tmpl)

app = Flask(__name__)
app.config.from_object(sheld.Config())
app.debug = True

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

app.register_blueprint(client_api)
app.register_blueprint(taxi_api)

@app.route('/')
def hel():
    return 'welcome'

app.run(use_reloader=False)
# app.run()