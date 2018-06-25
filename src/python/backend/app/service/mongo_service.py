# -*- coding: utf-8 -*-

from alphacar.mongo_wrapper import MongoWrapper

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_mongo():
    if 'mongo' not in g:
        conf = current_app.config['CONF']['mongo']

        db_name = conf['db_name']
        username = conf['username']
        password = conf['password']
        print('conf', conf)
        g.mongo = MongoWrapper(conf)
        g.mongo.connect_db(db_name, username, password)
    return g.mongo

def close_mongo(e=None):
    mongo = g.pop('mongo', None)
    if mongo is not None:
        mongo.close()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    get_mongo()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_mongo)
    app.cli.add_command(init_db_command)

#service methods
def getAllInfosByDate(date_str):
    mongo = get_mongo()
    result = mongo.db[date_str].find({}, {'_id' : 0})
    lst = list()
    lst = [item for item in result]
    return lst
