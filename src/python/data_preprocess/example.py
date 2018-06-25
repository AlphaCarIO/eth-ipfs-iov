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

def addHash(x, hash):
    x['hash'] = hash
    return x

if __name__ == "__main__":

    print('---iov demo---')

    parser = OptionParser()
    parser.add_option("-r", "--recreate", action = "store_true", default = False, dest = "recreate")

    (options, args) = parser.parse_args()
    
    filePath = os.path.dirname(__file__)
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    yamlPath = os.path.join(fileNamePath, '../conf/config.yaml')

    conf = None

    with open(yamlPath, "r", encoding='utf-8') as f:
        tmp = f.read()
        conf = yaml.load(tmp)

    mongo_wrapper = MongoWrapper(conf['mongo'])

    ipfs_api = IPFSWrapper(conf['ipfs'])

    web3_conf = conf['web3']
    w3 = Web3Wrapper(web3_conf)

    db_name = conf['mongo']['db_name']
    username = conf['mongo']['username']
    password = conf['mongo']['password']

    print('options.recreate:', options.recreate)

    today = datetime.datetime.today()
    today_str = today.strftime('%Y-%m-%d')
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

    if options.recreate == True:
        mongo_wrapper.drop_database(db_name)
    mongo_wrapper.connect_db(db_name, username, password)

    print('today_str:', today_str)
    
    datas = None

    with open('sample.json', "r", encoding='utf-8') as f:
        datas = json.load(f)

    nonce = w3.getNonce()

    for data in datas:

        if (len(data) == 0):
            continue

        dt = data[0]['datetime']
    
        mongo_wrapper.create_index(dt, [('datetime', pymongo.ASCENDING), ('user', pymongo.ASCENDING)], True)

        hashVal = ipfs_api.addJsonData(data)

        print('hash:', hashVal)

        print('datas:', data)
    
        tmp_data = copy.deepcopy(data)

        tmp_data = [addHash(x, hashVal) for x in tmp_data]

        mongo_wrapper.insert_data(dt, tmp_data)

        print('tmp_datas:', tmp_data)

        res = mongo_wrapper.db[dt].find({})

        for item in res:
            print (item)

        tx = w3.putHash(dt, hashVal, gas = gas, gasPrice = gasPrice, nonce = nonce)
        nonce += 1
        print('store hash tx:', tx)
