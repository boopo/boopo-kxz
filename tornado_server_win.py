import asyncio
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from manage import app

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(22222)
IOLoop.instance().start()
