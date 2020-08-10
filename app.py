from flask import Flask, request, render_template
from db import Member, Facility, db
import json
import psycopg2
import config

app = Flask(__name__)
app.config["DEBUG"] = False

# app config
app.config["SQLALCHEMY_DATABASE_URI"] = config.URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello():
    return "Welcome to the Kalpataru Residency's ClubHouse Manager!"


@app.route('/list', methods=['GET'])
def list_facilities():
    facilities = Facility.query.all()
    facility_list = [facility.serialize() for facility in facilities]
    if facility_list:
        return json.dumps({'success': True, 'data': facility_list})

    return json.dumps({'success': False, 'error': 'No facilities Found'})


if __name__ == '__main__':
    app.run()
