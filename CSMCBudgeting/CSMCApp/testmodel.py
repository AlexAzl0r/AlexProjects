from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Members(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True)
    dateJoined = db.Column(db.Date())
    dateLeft = db.Column(db.Date(), nullable=True, default=None)
    isActive = db.Column(db.Boolean(), default=1)

    def __repr__(self):
        return f"{self.name} inserted, id: {self.id}"
