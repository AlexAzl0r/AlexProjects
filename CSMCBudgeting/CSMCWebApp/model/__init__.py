from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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


class Remittance(db.Model):
    __tablename__ = "remittance"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(10, 2))
    activeFrom = db.Column(db.Date)
    settlementDate = db.Column(db.Date, nullable=True)
    outstanding = db.Column(db.Boolean)
    name = db.Column(db.String)
    type = db.Column(db.String)
    memberId = db.Column(db.Integer, ForeignKey("members.id"))
    inventoryId = db.Column(db.Integer, ForeignKey("inventory.id"))
    inventory = relationship("Inventory", back_populates="remittance")
    # payments = relationship("Payments")
    members = relationship("Members")

    def __repr__(self):
        return f"{self.id}:{self.activeFrom}:{self.name}:{self.amount}"


class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2), default=None, nullable=True)
    dateAdded = db.Column(db.Date)
    dateLeft = db.Column(db.Date, nullable=True)
    remittance = relationship("Remittance", uselist=False, back_populates="inventory")

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.price}:{self.dateAdded}"


class Payments(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column('amount', db.Numeric(10, 2))
    dateCreated = db.Column('dateCreated', db.Date)
    datePaid = db.Column('datePaid', db.Date)
    remittanceId = db.Column(db.Integer, ForeignKey("remittance.id"))

    def __repr__(self):
        return f"{self.id}:{self.amount}:{self.dateCreated}"
