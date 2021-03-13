# import kivy
# import pandas as pd
# from datetime import datetime, timedelta
import sqlite3

conn = sqlite3.connect("csmc.db")
conn.execute("PRAGMA foreign_keys = 1")
c = conn.cursor()

c.execute("""CREATE TABLE MEMBERS([id] INTEGER PRIMARY KEY,[memberName] text, [dateFrom] datetime, [dateLeft] datetime, [active] bool)""")
c.execute(""" CREATE TABLE SUBS([id] INTEGER PRIMARY KEY,[dateDue] date, [amount] real,[memberId] int, FOREIGN KEY (memberId) REFERENCES MEMBERS (id))""")
c.execute(""" CREATE TABLE DEBTS([id] INTEGER PRIMARY KEY, [paid] bool, [name] text, [notes] text, [startDate] date, [datePaid] date, [memberId] int, [subId] int, FOREIGN KEY (memberId) REFERENCES MEMBERS (id),FOREIGN KEY (subId) REFERENCES SUBS (id))""")

conn.commit()