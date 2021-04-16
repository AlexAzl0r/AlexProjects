import datetime as dt
import sqlite3
from arguments import args_new_member
import pandas as pd
from config import Config
from sqlalchemy import MetaData, Table, Column, Integer, create_engine

args = args_new_member().parse_args()

def connect_to_members_table(sql):
    engine = create_engine(Config.engine)

class Members:
    def __init__(self, config):
        self.config = config
        self.sql_data = config.sql_conn

    def add_new_member(self, name: str, date_of_birth: str, date_joined: str, rank_joined: str):
        new_row = pd.DataFrame(
            [{"Name": name, "DOB": date_of_birth, "DateJoined": date_joined, "RankJoined": rank_joined}])
        new_row['DOB'] = pd.to_datetime(new_row['DOB'])
        if new_row['Name'] in self.member_data:
            raise Exception

        return new_row

    def update_existing_member(self):
        pass

    def increment_subs_for_active_members(self,):


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
