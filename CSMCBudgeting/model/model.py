from sqlalchemy import Column, Date, Integer, String, Boolean, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from CSMCBudgeting.config import Config

engine = Config.model_database_engine
Base = declarative_base()


class Members(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('Name', String, unique=True)
    dateJoined = Column('dateJoined', Date)
    dateLeft = Column('dateLeft', Date, nullable=True, default=None)
    isActive = Column('isActive', Boolean, default=1)
    remittance = relationship("Remittance", back_populates="members")

    __table_args = {'sqlite_autoincrement': True}


class Remittance(Base):
    __tablename__ = "remittance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column('amount', Numeric(10, 2))
    datCreated = Column('dateActive', Date)
    dateSettled = Column('dateSettled', Date, nullable=True)
    outstanding = Column('outstanding', Boolean)
    name = Column('name', String)
    type = Column('type', String)
    memberId = Column(Integer, ForeignKey("members.id"))
    inventoryId = Column(Integer, ForeignKey("inventory.id"))
    inventory = relationship("Inventory", back_populates="remittance")
    payments = relationship("Payments")
    members = relationship("Members")


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
    price = Column('price', Numeric(10, 2), default=None, nullable=True)
    dateAdded = Column('dateAdded', Date)
    dateLeft = Column('dateLeft', Date, nullable=True)
    remittance = relationship("Remittance", uselist=False, back_populates="inventory")


class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column('amount', Numeric(10, 2))
    dateCreated = Column('dateCreated', Date)
    datePaid = Column('datePaid', Date)
    remittanceId = Column(Integer, ForeignKey("remittance.id"))


Base.metadata.create_all(engine)
