from membership import Membership
from config import Config
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model import Members


member_object = Membership(Config, Members)


# Adds Member
member_object.add_new_member("Madara Dziedataja", "2021-04-18")

# Updates Member
# update_alex = member_object.update_existing_member("Vern Spicer", "dateLeft", "2021-04-18")

# Queries all Members
result_set = member_object.query_all_members()
print(result_set)

# Deletes all data (cant be undone)
# member_object.delete_row()
