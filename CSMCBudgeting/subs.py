from dataretrieval import QueryDataTables
from config import Config as config

conn = config.conn

class MonthlySubs:
    def __init__(self, date, member_name):
        self.date = date
        self.member_name = member_name

    @staticmethod
    def return_active_members():
        member_instance = QueryDataTables(config.member_table,config.select_all_query)
        active_members = member_instance.run()
        active_members = active_members[~active_members.active == 1]
        return active_members

    def increment_subs_for_active_members(self, members):
        #need to add a row for each member if latest month in table is < current month

    def add_to_debts_table(self,subs):
        #need to ship rows to debts table if paid=0 AND month of row < current month

