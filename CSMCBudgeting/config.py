import sqlite3

import pandas as pd

class Config:
    sql_dir = "SQLQueries"
    select_all_query = "SELECTDATA.sql"
    database = "csmc.db"
    member_table = "MEMBERS"
    subs_table = "SUBS"
    debts_table = "DEBTS"
    csmc_engine = 'sqlite:///CSMC.db'

if __name__ == "__main__":
    test = pd.read_sql('select * from MEMBERS', Config.csmc_engine)

    print(test.head())
