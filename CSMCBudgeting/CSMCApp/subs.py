import datetime

import pandas as pd


class Subscriptions:
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
            print(e)


class RemittanceSettler:
    def __init__(self, config, members):
        self.__config = config
        self.__members = members

    def query_item_from_database(self):
        pass

    def generate_outstanding_amount_for_member(self):
        pass
