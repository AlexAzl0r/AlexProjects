from membership import Membership
from config import Config
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model import Members


member_object = Membership(Config, Members)

update_alex = member_object.update_existing_member("Vern Spicer", "dateLeft", None)

result_set = member_object.query_all_members()

print(result_set)

