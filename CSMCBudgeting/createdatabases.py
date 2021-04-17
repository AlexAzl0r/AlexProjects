from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import Config

engine = create_engine(Config.csmc_engine, echo=True)
Base = declarative_base()


class Members(Base):

    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column('Name', String)
    dateJoined = Column('dateJoined', Date)
    dateLeft = Column('dateLeft', Date)
    isActive = Column('isActive', Boolean)
    remittance = relationship("Remittance", back_populates="members")


class Remittance(Base):

    __tablename__ = "remittance"

    id = Column(Integer, primary_key=True)
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


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    dateAdded = Column('dateAdded', Date)
    dateLeft = Column('dateLeft', Date, nullable=True)
    remittance = relationship("Remittance", uselist=False, back_populates="inventory")


class Payments(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    amount = Column('amount', Numeric(10, 2))
    dateCreated = Column('dateCreated', Date)
    datePaid = Column('datePaid', Date)
    remittanceId = Column(Integer, ForeignKey("remittance.id"))



# Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
