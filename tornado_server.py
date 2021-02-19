import asyncio
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from manage import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(22222)
IOLoop.instance().start()

# 部署用法 python tornado_server.py
# linux