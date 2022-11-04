import sqlalchemy
from sqlalchemy import create_engine
import json


def dict_to_string(d):
    fin_row = ''
    for el in d:
        fin_row += ";".join(
            map(
                lambda v: f"{v[0]}: {v[1]}", 
                el._asdict().items()
            )
        ) + "\n"
    print(fin_row)
    return fin_row


class DataBase:
    def __init__(self, url):
        print("Started initing db")
        self.db = create_engine(url)
        self.conn = None


    def _fetch_db(self, query):
        self.conn = self.db.connect()
        result = self.conn.execute(query)
        res_dict =  result.fetchall()
        return dict_to_string(res_dict)


    def safe_fetch(self, query):
        try:
            return self._fetch_db(query)
        except Exception  as e:
            print(f"Error fetching data. query={query}, e={e}")
        finally:
            if self.conn:
                self.conn.close()
