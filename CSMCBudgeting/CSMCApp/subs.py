import datetime

import pandas as pd
from sqlalchemy.orm import sessionmaker


class MonthlySubscriptions:
    def __init__(self, config, members):
        self.__config = config
        self.__engine = config.database_engine
        self.__members = members

    def generate_subs_for_active_members(self) -> pd.DataFrame:
        """
        Generates monthly subs for all active members, agnostic as to there rank/situation
        :return: pd.DataFrame
        """

        remittance_list = []
        for id in self.__members.id:
            new_sub_values = pd.DataFrame([{"amount": 20,
                                            "dateActive": datetime.datetime.now(),
                                            "dateSettled": None,
                                            "outstanding": True,
                                            "name": "monthly_subs",
                                            "type": "subs",
                                            "memberId": id,
                                            "inventoryId": None}])
            remittance_list.append(new_sub_values)
        remittance_frame = pd.concat(remittance_list).set_index("memberId")
        return remittance_frame

    def commit_new_subs_to_database(self, monthly_subscriptions: pd.DataFrame):
        """
        Adds new subs to database. Monthly.
        :param monthly_subscriptions: pd.DataFrame
        :return: to_sql stuff
        """
        print(f"{len(monthly_subscriptions)} subs added for: {datetime.datetime.now()}")

        try:
            monthly_subscriptions.to_sql("remittance", self.__engine.engine, if_exists="append")
        except Exception as e:
            raise e


class OutstandingDebts:
    def __init__(self, config, members, table):
        self.__config = config
        self.__engine = config.database_engine
        self.__table = table
        self.__members = members

    def get_all_unpaid_remittance(self, member_name=None):
        query = """SELECT m.[id], m.[name], s.[amount],
                s.[dateActive], s.[outstanding], s.[name] as 'remittanceName', s.[type]
                FROM members m
                JOIN remittance s on m.id=s.memberId"""

        member_string = f""" WHERE m.name = '{member_name}'"""

        if member_name:
            member_string = query + member_string
            outstanding_remittance = pd.read_sql(member_string, self.__engine.engine)

            return outstanding_remittance
        else:
            outstanding_remittance = pd.read_sql(query, self.__engine.engine)

        return outstanding_remittance


class DebtManager:
    def __init__(self, member_data, config, remittance_table, name):
        self.member_data = member_data[member_data['Name'] == name]
        self.config = config
        self.__engine = config.database_engine
        self.__table = remittance_table
        self.member_name = name

    def __create_session(self):
        session = sessionmaker(bind=self.__engine)
        return session()

    def summarize_outstanding_payments(self):
        member_balance = self.member_data.loc[self.member_data.outstanding == 1]
        member_balance = member_balance.groupby(by=['remittanceName'])['amount'].sum()
        if member_balance.empty:
            print(f"No outstanding debts for {self.member_name}")
            return None

        return member_balance

    def pay_remittance(self, category=None, date=None):
        filtered_data = self.member_data
        if date:
            date = pd.to_datetime(date)

        if date and category:
            filtered_resultset = filtered_data.loc[
                (filtered_data['type'] == category) & (pd.to_datetime(filtered_data['dateActive']) > date)]
        elif category:
            filtered_resultset = filtered_data[filtered_data['type'] == category]
        elif date:
            filtered_resultset = filtered_data[pd.to_datetime(filtered_data['dateActive']) > date]
        else:
            raise Exception(f"Error, no category or date selected for type: {category} or date {date}")

        if filtered_resultset.empty:
            raise Exception(f"No outstanding debts for {self.member_name}")

        with self.__create_session() as session:
            date_settled = datetime.datetime.now().date()
            outstanding = False
            member_id = filtered_resultset['id'].values[0]

            query = f"""UPDATE remittance
            SET dateSettled = '{date_settled}', outstanding = {outstanding}
            WHERE memberId = '{member_id}'"""

            if date:
                date_active = pd.to_datetime(filtered_resultset['dateActive']).dt.date.item()
                date_portion = f""" AND dateActive >= '{date_active}'"""
                query = query+date_portion


            session.execute(query)
            session.commit()

    def update_remittance(self, date, type):
        date = datetime.datetime.strptime("%Y-%m-%d")
