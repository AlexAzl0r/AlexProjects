import datetime as dt
import pandas as pd
import argparse
import sqlite3

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument("--name", help="Name of member.")
parser.add_argument("--datejoined", help="Date joined - format YYYY-MM-DD")
parser.add_argument("--dateleft", help="Date Left, leave blank if new member", nargs='?',default=None)

args = parser.parse_args()
class MembershipUpdate:
    def __init__(self, name, date_joined, connection, date_left=None):
        self.name = name
        self.date_joined = date_joined
        self.date_left = date_left
        self.is_active = None if date_left is None else False
        self.connection = connection

    def format_new_member(self):
        cols = ['memberName','dateFrom','dateLeft','active']
        values = [self.name, self.date_joined, None if self.date_left is None else dt.datetime.strptime(self.date_left, "%Y-%m-%d"), True if self.is_active is None else self.is_active]
        dataframe = pd.DataFrame([values], columns=cols, index=None)
        return dataframe

    @staticmethod
    def output_to_database(new_member_dataframe): #staticmethod
        conn = sqlite3.connect("csmc.db")
        new_member_dataframe.to_sql(name="MEMBERS", con=conn, if_exists="append", index=False)

    def run(self):
        update_new_member = self.format_new_member()
        self.output_to_database(update_new_member)

if __name__ == "__main__":
    job = MembershipUpdate(connection=None, name=args.name, date_joined=args.datejoined, date_left=None if args.dateleft is None else args.dateleft)
    job.run()



