import pandas as pd

from sqlalchemy import create_engine

members = [{"id": 7, "name": "Alex Neville",
            "dateJoined": pd.to_datetime("2019-01-04"),
            "dateLeft": None,
                'isActive': 1,
            }, {"id": 6, "name": "Vern Spicer",
                "dateJoined": pd.to_datetime("2017-01-01"),
                "dateLeft": None, 'isActive': 1,
                }, {"id": 2, "name": "Dylan LLoyd Meredith",
                    "dateJoined": pd.to_datetime("2012-01-01"),
                    "dateLeft": None, 'isActive': 1,
                    }, {"id": 5, "name": "Aaron Thompson",
                        "dateJoined": pd.to_datetime("2015-01-01"),
                        "dateLeft": None, 'isActive': 1,
                        }, {"id": 4, "name": "Dougal Hamilton",
                            "dateJoined": pd.to_datetime("2014-01-01"),
                            "dateLeft": None, 'isActive': 1,
                            }, {"id": 1, "name": "Wookie",
                                "dateJoined": pd.to_datetime("2012-01-01"),
                                "dateLeft": None, 'isActive': 1,
                                }, {"id": 3, "name": "Savi Savident",
                                    "dateJoined": pd.to_datetime("2012-01-01"),
                                    "dateLeft": None, 'isActive': 1,
                                    }, ]

session = create_engine("sqlite:///csmc.db")
members = pd.DataFrame.from_dict(members, orient='columns').sort_values(by="id", ascending=True)

members.to_sql("members", session.engine, if_exists="replace", index=False)
