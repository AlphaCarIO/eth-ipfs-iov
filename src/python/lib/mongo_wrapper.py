# -*- coding: utf-8 -*-
import pymongo
import sys
import traceback

class Singleton(object):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MongoWrapper(object):

    def __init__(self, MONGODB_CONFIG, reCreated = False):
        
        try:
            self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            if reCreated:
                self.conn.drop_database(MONGODB_CONFIG['db_name'])
            self.db = self.conn[MONGODB_CONFIG['db_name']]
            self.username=MONGODB_CONFIG['username']
            self.password=MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except Exception:
            print(traceback.format_exc())
            print('Connect Statics Database Fail.')
            sys.exit(1)
