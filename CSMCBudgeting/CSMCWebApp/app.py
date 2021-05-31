from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, abort
import datetime

app = Flask(__name__)

db = SQLAlchemy()


class Members(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True)
    dateJoined = db.Column(db.Date())
    dateLeft = db.Column(db.Date(), nullable=True, default=None)
    isActive = db.Column(db.Boolean(), default=1)

    def __repr__(self):
        return f"{self.name}:{self.id}"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CSMC.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route("/")
def home():
    return "Healthy"


@app.route('/data/create', methods=['GET', 'POST'])
def get_new_member_data():
    if request.method == 'GET':
        return render_template('newdata.html')

    if request.method == 'POST':
        new_member_name = request.form['member_name']
        date_joined = request.form['date_joined']
        date_joined = datetime.datetime.strptime(date_joined, "%Y-%m-%d")
        employee = Members(name=new_member_name, dateJoined=date_joined)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')


@app.route('/data')
def retrieve_all_member_data():
    members = Members.query.all()
    return render_template('memberlist.html', members=members)


@app.route('/data/<int:id>')
def retrieve_single_member_data(id):
    member = Members.query.filter_by(id=id).first()
    if member:
        return render_template('data.html', member=member)
    return f"no member has id: {id} associated"


@app.route('/data/<int:member_id>/update', methods=['GET', 'POST'])
def update(member_id):
    member = Members.query.filter_by(id=member_id).first()
    if request.method == 'POST':
        if member:

            name = member.name
            date_joined = member.dateJoined

            db.session.delete(member)
            db.session.commit()

            date_left = request.form['date_left']
            updated_name = request.form['member_name']
            if updated_name:
                name = updated_name

            if date_left:
                is_active = 0
                date_left = datetime.datetime.strptime(date_left, '%Y-%m-%d')
            else:
                date_left = None
                is_active = 1

            member_update = Members(id=member_id, name=name, dateJoined=date_joined, dateLeft=date_left, isActive=is_active)

            db.session.add(member_update)
            db.session.commit()
            return redirect(f'/data/{member_id}')
        return f"No members with id: {member_id} exist"

    return render_template('memberupdate.html', member=member)


@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    member = Members.query.filter_by(id=id).first()
    if request.method == 'POST':
        if member:
            db.session.delete(member)
            db.session.commit()
            return redirect('/data')
        abort(404)

    return render_template('delete.html')


if __name__ == "__main__":
    app.run()