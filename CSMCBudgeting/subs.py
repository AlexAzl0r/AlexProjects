import datetime
import pandas as pd

class Subscriptions:
    def __init__(self, config, members):
        self.config = config
        self.connection = config.connection
        self.members = members

    def generate_subs_for_active_members(self):
        """
        Generates monthly subs for all active members, agnostic as to there rank/situation
        :return: pd.DataFrame
        """

        rows = []
        for id in self.members.member_ids:
            new_sub_values = pd.DataFrame([{"amount": 20,
                               "datCreated": datetime.datetime.now(),
                               "dateSettled": None,
                               "outstanding": True,
                               "name": "monthly_subs",
                               "type": "subs",
                               "memberId": id,
                               "inventoryId": None}])
            new_sub_values.append(rows)
        rows = pd.concat(rows)
        return rows




