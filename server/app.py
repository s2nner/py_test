from flask import Flask
from flask_apscheduler import APScheduler

import logging
from logging.handlers import RotatingFileHandler

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
    app.logger.info('Info')
    return 'welcome'


formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler('logs/foo.log', maxBytes=10000000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
app.logger.addHandler(handler)


app.run(use_reloader=False)
# app.run()
