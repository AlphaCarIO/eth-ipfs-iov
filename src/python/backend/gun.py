import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

log_folder = 'log'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

debug = True
loglevel = 'debug'
bind = '0.0.0.0:8800'
pidfile = log_folder + '/gunicorn.pid'
logfile = log_folder + '/debug.log'

#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'
