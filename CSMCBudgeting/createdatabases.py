from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///D:\\Programs\\GIT\\AlexProjects\\CSMCBudeting\\Databases\\CSMC.db', echo=True)
Base = declarative_base()


class Members(Base):

    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column('Name', String)
    date_joined = Column('dateJoined', Date)
    date_left = Column('dateLeft', Date)
    is_active = Column('isActive', Boolean)


class Subs(Base):

    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    amount = Column('amount', Numeric(10, 2))
    date_created = Column('dateActive', Date)
    date_settled = Column('dateSettled', Date, nullable=True)
    name = Column('name', String)
    type = Column('type', String)
    member_id = Column(Integer, ForeignKey("members.id"))
    member = relationship("Members")


Session = sessionmaker(bind=engine)

session = Session
print(session)