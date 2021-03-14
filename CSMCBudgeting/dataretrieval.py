import pandas as pd
from config import Config
import argparse

parser = argparse.ArgumentParser(description='Retrieve data from database')
parser.add_argument("--table", help="Table you wish to query.")
parser.add_argument("--query", help="Supply a valid query file name without extension (foo.sql would be jut foo)")
args = parser.parse_args()


class QueryDataTables:
    def __init__(self, table_name, query_name):
        self.table_name = table_name
        self.query_name = query_name

    def read_query_from_file(self):
        with open(f'{Config.sql_dir}/{self.query_name}.sql', 'r') as sql_file:
            try:
                query = sql_file.read()
                return query
            except Exception as e:
                print(f"Unable to read query, reason: {e}")
            finally:
                print(f"folder: {Config.sql_dir} read, {len(query)} queries read.")

    @staticmethod
    def run_query_file(query):
        df = pd.read_sql(query, Config.conn)
        return df

    def run(self):
        query = self.read_query_from_file()
        returned_data = self.run_query_file(query.replace('xxxx', self.table_name))
        return returned_data


if __name__ == "__main__":
    job = QueryDataTables(table_name=args.table,query_name=args.query)
    job.run()
