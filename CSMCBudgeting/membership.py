
from arguments import args_new_member
import pandas as pd
from model import Members
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from config import Config


args = args_new_member().parse_args()


def validate_table_columns(table, engine, new_table=None):
    options = ['Members', 'Remittance', 'Inventory', 'Payments']
    if new_table:
        options.append(new_table)
        print(f"warning, please append {new_table} to options")

    if table in options:
        try:
            cols = pd.read_sql(f"SELECT TOP(1) * FROM {table}", engine)
            return cols.columns.values.tolist()

        except Exception as e:
            print(e)

    else:
        print(f"failed to query {table}, it doesn't exist.")



class Membership:
    def __init__(self, config, table):
        self.config = config
        self.engine = config.database_engine
        self.table = table
        self.session = sessionmaker(bind=self.engine)



    def query_all_members(self):
        statement = f"""SELECT * FROM {self.table.__table__}"""
        data = pd.read_sql(statement, self.engine.engine, index_col='id')
        return data

    def add_new_member(self, name: str, date_of_birth: str, date_joined: str, rank_joined: str):
        new_row = pd.DataFrame(
            [{"Name": name, "DOB": date_of_birth, "DateJoined": date_joined, "RankJoined": rank_joined}])
        new_row['DOB'] = pd.to_datetime(new_row['DOB'])
        if new_row['Name'] in self.member_data:
            raise Exception

        return new_row

    def update_existing_member(self, member_name, col_to_update, new_value):
        session = self.session()
        updater = session.query(self.table).filter(self.table.name == member_name)
        date_cols = ["dateLeft", "dateJoined"]

        if col_to_update in date_cols:
            new_value = pd.to_datetime(new_value)

        data_to_update = {col_to_update: new_value}
        print(f"{col_to_update} for {member_name} updated, new value: {new_value}")
        if col_to_update == "dateLeft":
            if new_value:
                updater.update({'isActive': 0})
            else:
                updater.update({'isActive': 1})

        updater.update(data_to_update)

        session.commit()

