from aiohttp import web
from db import DataBase

import os
import time


async def handle(request):
    request_type = request.rel_url.query.get("request_type")
    with open(os.path.join("sql_scripts",  request_type + ".sql"), "r") as f:
        query =  f.read()
    result = db.safe_fetch(query)
    print("Got result")
    print(result)
    print(type(result))
    x = web.Response(text=result)
    print(x)
    return x


async def hello_world(request):
    return web.Response(text='hello world') 


if __name__ == "__main__":
    while True:
        try:
            print("Started working")
            db_connection_url = os.environ["db_connection_url"]
            print(f"db connection url is {db_connection_url}")
            app = web.Application()
            print("App created")
            app.add_routes([web.get("/get_data", handle), web.get("/hw", hello_world)])
            print("routes added")
            db = DataBase(db_connection_url)
            print("DB instance created")
            web.run_app(app, port=1234)
        except Exception as e:
            print(f"Caught exception: e={e}")
            time.sleep(1)
