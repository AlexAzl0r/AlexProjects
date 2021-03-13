import datetime as dt
import pandas as pd
import argparse
import sqlite3

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument("--name", help="Name of member.")
parser.add_argument("--datejoined", help="Date joined - format YYYY-MM-DD")
parser.add_argument("--dateleft", help="Date Left, leave blank if new member", nargs='?',default=None)

args = parser.parse_args()
print(args)
class MembershipUpdate:
    def __init__(self, name, datejoined, connection, dateleft=None):
        self.name = name
        self.datejoined = datejoined
        self.dateleft = dateleft
        self.isactive = None if dateleft is None else False
        self.connection = connection

    def formatnewmember(self):
        cols = ['memberName','dateFrom','dateLeft','active']
        vals = [self.name, self.datejoined,None if self.dateleft is None else dt.datetime.strptime(self.dateleft, "%Y-%m-%d"), True if self.isactive is None else self.isactive]
        emptydf = pd.DataFrame([vals], columns=cols,index=None)
        return emptydf

    def commitmember(self, memberdf):
        conn = sqlite3.connect("csmc.db")
        memberdf.to_sql(name="MEMBERS",con=conn,if_exists="append",index=False)

if __name__ == "__main__":
    obj = MembershipUpdate(connection=None,name=args.name, datejoined=args.datejoined,dateleft=None if args.dateleft is None else args.dateleft)
    df = obj.formatnewmember()
    print(df)
    out = obj.commitmember(df)




