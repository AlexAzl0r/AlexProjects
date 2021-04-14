import datetime as dt
import sqlite3
from arguments import args_new_member
import pandas as pd

args = args_new_member().parse_args()


class Members:
    def __init__(self, config, existing_data):
        self.config = config
        self.member_data = existing_data

    def add_new_member(self, name, date_of_birth, date_joined, rank_joined):
        pass

    def update_existing_member(self, rows):
        pass





def output_to_database(data: pd.DataFrame, connection=None, server="csmc.db", table_name=None):
    """
    Outputs resultset to predefined table
    :param data: Data, could be members, subs or debts
    :param connection: connection string
    :param server: server (default is csmc)
    :param table_name: table to commit data to
    :return: n/a
    """
    data.to_sql(name=table_name, con=connection, if_exists="append", index=False)
    return f"{print(len(data))} rows committed to Database"
