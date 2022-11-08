from aiohttp import web
from db import DataBase
from utils import get_query
import os
import time



async def handle(request):
    query = get_query(request.rel_url.query.get("request_type"))
    result = db.safe_fetch(query)
    return web.Response(text=result)

def hw(request):
	return web.Response(text='hello world')

def init_app():
    app = web.Application()
    app.add_routes([web.get("/get_data", handle), web.get("/hw", hw)])
    db_connection_url = os.environ["db_connection_url"]
    db = DataBase(db_connection_url)
    return app, db 


if __name__ == "__main__":
    while True:
        try:
            app, db = init_app()
            web.run_app(app, port=1234)
        except Exception as e:
            print(f"Caught exception: e={e}")
            time.sleep(1)
