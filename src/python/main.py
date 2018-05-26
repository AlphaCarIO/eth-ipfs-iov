# -*- coding: utf-8 -*-
from lib.mongo_wrapper import MongoWrapper
from lib.ipfs_wrapper import IPFSWrapper
from lib.web3_wrapper import Web3Wrapper

import datetime

import json

MONGODB_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
    'db_name': 'alphacar',
    'username': None,
    'password': None
}

IPFS_CONFIG = {
    'host': '127.0.0.1',
    'port': 5001
}

FOLDER_PATH = '../iov-prj/build/IOVContract'

FILE_PREFIX = 'IOVContract'

if __name__ == "__main__":

    mongo_wrapper = MongoWrapper(MONGODB_CONFIG, True)
    ipfs_api = IPFSWrapper(IPFS_CONFIG['host'], IPFS_CONFIG['port'])

    today = datetime.datetime.today()
    today_str = today.strftime('%Y-%m-%d')
    print('today_str:', today_str)
    
    datas = [
        {'datetime': today_str, 'user': {'name': 'leo', 'cid': '1070701'}},
        {'datetime': today_str, 'car': {'name': 'c4l'}},
    ]

    hashVal = ipfs_api.addJsonData(datas)

    print('hash:', hashVal)

    mongo_wrapper.db[today_str].insert(datas)

    print('data:', datas)

    res = mongo_wrapper.db[today_str].find({})

    for item in res:
        print (item)

    #store hash data on blockchain

    abi_dat = None
    
    with open('%s/%s.abi' % (FOLDER_PATH, FILE_PREFIX), "r") as load_f:
        abi_dat = json.load(load_f)
    
    ETH_CONFIG = None

    with open('main_conf.json') as load_f:
        ETH_CONFIG = json.load(load_f)

    w3 = Web3Wrapper('config.json')

    w3.storeHash(today_str, hashVal, ETH_CONFIG['contract_address'], abi_dat, gas = 10 ** 6, gasPrice = 10 * 10 ** 9)
