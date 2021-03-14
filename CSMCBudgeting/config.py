import sqlite3


class Config:
    sql_dir = "SQLQueries"
    select_all_query = "SELECTDATA.sql"
    database = "csmc.db"
    member_table = "MEMBERS"
    subs_table = "SUBS"
    debts_table = "DEBTS"
    conn = sqlite3.connect(database)
