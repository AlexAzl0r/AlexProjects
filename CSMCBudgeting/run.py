from membership import Membership
from config import Config
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model import Members


member_object = Membership(Config, Members)


updatealex = member_object.update_existing_member("Vern Spicer", "dateLeft", None)
resultset = member_object.retrieve_members()
print(resultset)

