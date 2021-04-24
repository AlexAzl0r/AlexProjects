"""
Membership class - just stuff to create/retrieve/update/delete member data
"""

import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from CSMCBudgeting.TODO.arguments import args_new_member

args = args_new_member().parse_args()


class Membership:
    def __init__(self, config, sql_table):
        self.__config = config
        self.__engine = config.database_engine
        self.__table = sql_table

    def __create_session(self):
        session = sessionmaker(bind=self.__engine)
        return session()

    def __member_validator(self, member_name):
        session = self.__create_session()
        member_record = session.query(self.__table).filter(self.__table.name == member_name).all()

        return member_record

    def query_all_members(self):
        statement = text("""SELECT * FROM members""")
        data = pd.read_sql(statement, self.__engine.engine)

        return data

    def add_new_member(self, member_name: str, date_joined: str):
        member_validation = self.__member_validator(member_name=member_name)

        session = self.__create_session()

        if len(member_validation) == 0:
            session.add(self.__table(name=member_name, dateJoined=pd.to_datetime(date_joined)))
            session.commit()

        else:
            raise Exception(f"Cannot add {member_name}, they already exist")

    def update_existing_member(self, member_name, col_to_update, new_value):
        session = self.__create_session()
        updater = session.query(self.__table).filter(self.__table.name == member_name)
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

    def delete_row(self, member_name=None):
        session = self.__create_session()
        with session as session:
            if member_name is None:
                session.query(self.__table).delete()
            else:
                try:
                    session.query(self.__table).filter(self.__table.name == member_name).delete()
                except Exception as e:
                    print(f"Could not delete {member_name} - {e}")
            session.commit()
