import sqlalchemy
from sqlalchemy import create_engine
import json
from utils import dict_to_string




class DataBase:
    def __init__(self, url):
        print("Started initing db")
        self.db = create_engine(url)
        self.conn = None


    def _fetch_db(self, query):
        self.conn = self.db.connect()
        result = self.conn.execute(query).fetchall()
        return dict_to_string(result)
        


    def safe_fetch(self, query):
        try:
            return self._fetch_db(query)
        except Exception  as e:
            print(f"Error fetching data. query={query}, e={e}")
        finally:
            if self.conn:
                self.conn.close()
