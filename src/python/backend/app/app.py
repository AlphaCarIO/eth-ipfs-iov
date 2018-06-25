# -*- coding: utf-8 -*-
import connexion
from connexion.resolver import RestyResolver
import app.service.mongo_service as mongo_service

import os
import yaml

from optparse import OptionParser

app = connexion.FlaskApp(__name__, specification_dir='../swagger/')

app.add_api('swagger.yaml', arguments={'title': 'AlphaCar Blockchain API Service'},
    resolver=RestyResolver('api'))

print("#####")
print('\n'.join(['%s:%s' % item for item in app.__dict__.items()]))
print("#####")

def init():

    filePath = os.path.dirname(__file__)
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    yamlPath = os.path.join(fileNamePath, '../../conf/config.yaml')

    conf = None

    with open(yamlPath, "r", encoding='utf-8') as f:
        tmp = f.read()
        conf = yaml.load(tmp)

    app.app.config.update(CONF = conf)
    mongo_service.init_app(app.app)

init()

if __name__ == '__main__':

    app.run(port = 8080, debug = True)
