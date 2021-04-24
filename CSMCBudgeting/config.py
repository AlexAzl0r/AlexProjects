import pandas as pd
from sqlalchemy import create_engine


class Config:
    member_table = "MEMBERS"
    subs_table = "Remittance"
    debts_table = "Payments"
    inventory_table = "Inventory"
    model_database = 'sqlite:///CSMC.db'
    database = 'sqlite:///model/CSMC.db'
    model_database_engine = create_engine(model_database)
    database_engine = create_engine(database)

if __name__ == "__main__":
    test = pd.read_sql('select * from inventory', Config.database_engine.engine)

    print(test)
