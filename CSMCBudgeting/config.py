import sqlite3
from sqlalchemy import create_engine
import pandas as pd

class Config:

    member_table = "MEMBERS"
    subs_table = "Remittance"
    debts_table = "Payments"
    inventory_table = "Inventory"

    database = 'sqlite:///CSMC.db'
    database_engine = create_engine(database)

if __name__ == "__main__":
    test = pd.read_sql('select * from MEMBERS', Config.database_engine.engine)

    print(test.tail())
