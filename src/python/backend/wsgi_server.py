# -*- coding: utf-8 -*-
from gevent.wsgi import WSGIServer
from app.app import app

http_server = WSGIServer(('', 8800), app)
http_server.serve_forever()
