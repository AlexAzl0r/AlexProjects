import datetime
import os

from flask import Flask, render_template, request
from model import Members
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir, "CSMC.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:

        new_member = Members(name=request.form.get("membername"), dateJoined=request.form.get("dateadded"))
        db.session.add(new_member)
        db.session.commit()
        print(f"User input: {request.form} at {datetime.datetime.now()}")
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
