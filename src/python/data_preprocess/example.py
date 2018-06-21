# -*- coding: utf-8 -*-

from alphacar.web3_wrapper import Web3Wrapper
from alphacar.mongo_wrapper import MongoWrapper
from alphacar.ipfs_wrapper import IPFSWrapper

import datetime

import os

import json, yaml

from optparse import OptionParser

from decimal import *

import pymongo

import copy

if __name__ == "__main__":

    print('---iov demo---')

    parser = OptionParser()
    parser.add_option("-r", "--recreate", action = "store_true", default = False, dest = "recreate")

    (options, args) = parser.parse_args()
    
    filePath = os.path.dirname(__file__)
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    yamlPath = os.path.join(fileNamePath, 'config.yaml')

    conf = None

    with open(yamlPath, "r", encoding='utf-8') as f:
        tmp = f.read()
        conf = yaml.load(tmp)

    mongo_wrapper = MongoWrapper(conf['mongo'])

    ipfs_api = IPFSWrapper(conf['ipfs'])

    w3 = Web3Wrapper(conf['web3'])

    db_name = conf['mongo']['db_name']
    username = conf['mongo']['username']
    password = conf['mongo']['password']

    print('options.recreate:', options.recreate)

    if options.recreate == True:
        mongo_wrapper.drop_database(db_name)
    mongo_wrapper.connect_db(db_name, username, password)

    today = datetime.datetime.today()
    today_str = today.strftime('%Y-%m-%d')

    print('today_str:', today_str)
    
    mongo_wrapper.create_index(today_str, [('datetime', pymongo.ASCENDING), ('user', pymongo.ASCENDING)], True)
    
    datas = [
        {'datetime': today_str, 'user': {'name': 'leo', 'cid': '1070701'}},
        {'datetime': today_str, 'user': {'name': 'nicolas', 'cid': '1070701'}},
    ]
    
    tmp_datas = copy.deepcopy(datas)

    mongo_wrapper.insert_data(today_str, tmp_datas)

    print('tmp_datas:', tmp_datas)
    print('datas:', datas)

    hashVal = ipfs_api.addJsonData(datas)

    print('hash:', hashVal)

    res = mongo_wrapper.db[today_str].find({})

    for item in res:
        print (item)

    #store hash data on blockchain

    abi_dat = None
    
    with open(conf['deploy']['abi'], "r") as load_f:
        abi_dat = json.load(load_f)

    gas = int(Decimal(conf['deploy']['gas']))
    gasPrice = int(Decimal(conf['deploy']['gasPrice']))
    contract_address = conf['web3']['contract_address']

    print('contract_address:', contract_address, 'gas:', gas, ' gasPrice:', gasPrice)

    w3.initContract(contract_address, abi_dat)

    getCount = w3.getCount()
    print('getCount:',  getCount)
    getTimestamp = w3.getTimestamp(today_str)
    print('getTimestamp:',  getTimestamp)
    getHash = w3.getHash(today_str)
    print('getHash:',  getHash)

    for ind in range(0, getCount):
        getDateTime = w3.getDateTime(ind)
        print('ind:', ind, ' getDateTime:',  getDateTime)
    #exit(0)

    tx = w3.putHash(today_str, hashVal, gas = gas, gasPrice = gasPrice)
    print('store hash tx:', tx)
