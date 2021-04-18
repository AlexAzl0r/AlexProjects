import pandas as pd
import datetime as dt
from sqlalchemy import create_engine

members = [{"id": None, "name": "Alex Neville",
            "dateJoined": pd.to_datetime("2019-01-04"),
            "dateLeft": None,
                'isActive': 1,
            }, {"id": None, "name": "Vern Spicer",
                "dateJoined": pd.to_datetime("2017-01-01"),
                "dateLeft": None, 'isActive': 1,
                }, {"id": None, "name": "Dylan LLoyd Meredith",
                    "dateJoined": pd.to_datetime("2012-01-01"),
                    "dateLeft": None, 'isActive': 1,
                    }, {"id": None, "name": "Aaron Thompson",
                        "dateJoined": pd.to_datetime("2015-01-01"),
                        "dateLeft": None, 'isActive': 1,
                        }, {"id": None, "name": "Dougal Hamilton",
                            "dateJoined": pd.to_datetime("2014-01-01"),
                            "dateLeft": None, 'isActive': 1,
                            }, {"id": None, "name": "Wookie",
                                "dateJoined": pd.to_datetime("2012-01-01"),
                                "dateLeft": None, 'isActive': 1,
                                }, {"id": None, "name": "Savi Savident",
                                    "dateJoined": pd.to_datetime("2012-01-01"),
                                    "dateLeft": None, 'isActive': 1,
                                    }, ]

session = create_engine("sqlite:///csmc.db")
members = pd.DataFrame.from_dict(members, orient='columns').sort_values(by="id", ascending=True)
members.update(members.select_dtypes('datetime').stack().dt.date.unstack())
members = members.drop(columns='id')
print(members)
members.to_sql("members", session.engine, if_exists="append", index=False)
