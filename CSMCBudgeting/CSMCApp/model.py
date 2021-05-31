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
    remittance = relationship("Remittance", back_populates="members")

    def __init__(self, name, dateJoined, dateLeft=None, isActive=None):
        self.name = name
        self.dateJoined = dateJoined
        self.dateLeft = dateLeft
        self.isActive = isActive

    def __repr__(self):
        return f"{self.name}:{self.dateJoined}:{self.dateLeft}:{self.isActive}:{self.remittance}"

    __table_args = {'sqlite_autoincrement': True}


class Remittance(db.Model):
    __tablename__ = "remittance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(10, 2))
    activeFrom = db.Column(db.Date)
    settlementDate = db.Column(db.Date, nullable=True)
    outstanding = db.Column(db.Boolean)
    name = db.Column(db.String)
    type = db.Column(db.String)
    memberId = db.Column(db.Integer, ForeignKey("members.id"))
    inventoryId = db.Column(db.Integer, ForeignKey("inventory.id"))
    inventory = relationship("Inventory", back_populates="remittance")
    payments = relationship("Payments")
    members = relationship("Members")

    def __init__(self, amount, active_from, date_settled, outstanding, name, type, member_id, inventory_id):
        self.amount = amount
        self.activeFrom = active_from
        self.settlementDate = date_settled
        self.outstanding = outstanding
        self.name = name
        self.type = type
        self.memberId = member_id
        self.inventoryId = inventory_id

    def __repr__(self):
        return f"{self.amount}:{self.activeFrom}:{self.settlementDate}:" \
               f"{self.outstanding}:{self.name}:{self.type}:{self.memberId}:{self.inventoryId}"


class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2), default=None, nullable=True)
    dateAdded = db.Column(db.Date)
    dateLeft = db.Column(db.Date, nullable=True)
    remittance = relationship("Remittance", uselist=False, back_populates="inventory")

    def __init__(self, name, price, date_added, date_left, remittance):
        self.name = name
        self.price = price
        self.dateAdded = date_added
        self.dateLeft = date_left

    def __repr__(self):
        return f"{self.name}:{self.price}:{self.dateAdded}:{self.dateLeft}"


class Payments(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column('amount', db.Numeric(10, 2))
    dateCreated = db.Column('dateCreated', db.Date)
    datePaid = db.Column('datePaid', db.Date)
    remittanceId = db.Column(db.Integer, ForeignKey("remittance.id"))

    def __init__(self, amount, date_created, date_paid, remittance_id):
        self.amount = amount
        self.dateCreated = date_created
        self.datePaid = date_paid
        self.remittanceId = remittance_id
