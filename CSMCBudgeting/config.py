import sqlite3
import sqlalchemy
import pandas as pd

class Config:
    sql_dir = "SQLQueries"
    select_all_query = "SELECTDATA.sql"
    database = "csmc.db"
    member_table = "MEMBERS"
    subs_table = "SUBS"
    debts_table = "DEBTS"
    conn = sqlite3.connect(database)
    engine = sqlalchemy.create_engine('sqlite:////D:/Programs/GIT/AlexProjects/csmc.db/')

if __name__ == "__main__":
    test = pd.read_sql('select * from MEMBERS', Config.engine)

    print(test.head())
