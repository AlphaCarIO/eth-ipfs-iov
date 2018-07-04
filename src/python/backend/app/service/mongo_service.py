# -*- coding: utf-8 -*-

from alphacar.mongo_wrapper import MongoWrapper

import click
from flask import current_app, g
from flask.cli import with_appcontext
import pymongo

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
def getLatestUBIInfo():
    mongo = get_mongo()
    result = mongo.db['ubi_info'].find({}, { '_id' : 0 }).sort([('timestamp', pymongo.DESCENDING)]).limit(1)
    for item in result:
        return item
    return {}

def getUbiInfo(ubi_code):
    mongo = get_mongo()
    result = mongo.db['ubi_info'].find({ 'ubi_code': ubi_code }, {'_id' : 0}).limit(1)
    for item in result:
        return item
    return {}

def getUbiInfoList(search_type, search_txt):
    #type: 0.all 1.ubi_code 2.vincode 3.driving license
    mongo = get_mongo()

    cond = {}

    if search_txt == '':
        pass
    elif search_type == '0' :
        cond = { '$or' : [ 
                    {'ubi_code': search_txt}, 
                    {'car_info.vin_code': search_txt}, 
                    {'user.driving_license': search_txt},
                    {'user.name': search_txt}, 
                    ]
                }
    elif search_type == '1' :
        cond = {'ubi_code': search_txt}
    elif search_type == '2' :
        cond = {'car_info.vin_code': search_txt}
    elif search_type == '3' :
        cond = {'user.name': search_txt}
    elif search_type == '4' :
        cond = {'user.driving_license': search_txt}

    result = mongo.db['ubi_info'].find(cond, {'_id' : 0}).sort([('timestamp', pymongo.DESCENDING)])
    lst = list()
    lst = [item for item in result]
    return lst
