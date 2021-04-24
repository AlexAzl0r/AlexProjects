import pandas as pd
from sqlalchemy import create_engine


class Config:
    member_table = "MEMBERS"
    subs_table = "Remittance"
    debts_table = "Payments"
    inventory_table = "Inventory"
    database = 'sqlite:///model/CSMC.db'
    database_engine = create_engine(database)


if __name__ == "__main__":
    test = pd.read_sql('select * from REMITTANCE', Config.database_engine.engine)

    print(test)
