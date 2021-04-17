
from arguments import args_new_member
import pandas as pd
from config import Config
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from createdatabases import Members

args = args_new_member().parse_args()


def validate_table_columns(table, engine, new_table=None):
    options = ['Members', 'Remittance', 'Inventory', 'Payments']
    if new_table:
        options.append(new_table)

    if table in options:
        try:
            cols = pd.read_sql(f"SELECT TOP(1) * FROM {table}", engine)
            return cols.columns.values.tolist()

        except Exception as e:
            print(e)

    else:
        print(f"failed to query {table}, it doesn't exist.")



class Members:
    def __init__(self, config, table):
        self.config = config
        self.sql_connection = config.sql_conn
        self.table = table


    def retrieve_members(self):
        connection = self.config.csmc_engine
        members = pd.read_sql('SELECT * FROM MEMBERS', connection)
        return members

    def add_new_member(self, name: str, date_of_birth: str, date_joined: str, rank_joined: str):
        new_row = pd.DataFrame(
            [{"Name": name, "DOB": date_of_birth, "DateJoined": date_joined, "RankJoined": rank_joined}])
        new_row['DOB'] = pd.to_datetime(new_row['DOB'])
        if new_row['Name'] in self.member_data:
            raise Exception

        return new_row


    def update_existing_member(self, member_name, new_value):
        connection = self.sql_connection.connect()
        updater = self.table.update().where(members.name=member_name.values(col=new_value))
        connection.execute(updater)
        return updater

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
