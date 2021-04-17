import pandas as pd

from sqlalchemy import create_engine

members = [{"id": 7, "name": "Alex Neville",
            "dateJoined": pd.to_datetime("2019-01-04"),
            "dateLeft": None,
            }, {"id": 6, "name": "Vern Spicer",
                "dateJoined": pd.to_datetime("2017-01-01"),
                "dateLeft": None,
                }, {"id": 2, "name": "Dylan LLoyd Meredith",
                    "dateJoined": pd.to_datetime("2012-01-01"),
                    "dateLeft": None,
                    }, {"id": 5, "name": "Aaron Thompson",
                        "dateJoined": pd.to_datetime("2015-01-01"),
                        "dateLeft": None,
                        }, {"id": 4, "name": "Dougal Hamilton",
                            "dateJoined": pd.to_datetime("2014-01-01"),
                            "dateLeft": None,
                            }, {"id": 1, "name": "Wookie",
                                "dateJoined": pd.to_datetime("2012-01-01"),
                                "dateLeft": None,
                                }, {"id": 3, "name": "Savi Savident",
                                    "dateJoined": pd.to_datetime("2012-01-01"),
                                    "dateLeft": None,
                                    }, ]

session = create_engine("sqlite:///csmc.db")
members = pd.DataFrame.from_dict(members, orient='columns').sort_values(by="id", ascending=True)

members.to_sql("members", session.engine, if_exists="append", index=False)
