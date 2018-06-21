# -*- coding: utf-8 -*-

from alphacar.web3_wrapper import Web3Wrapper
from alphacar.mongo_wrapper import MongoWrapper
from alphacar.ipfs_wrapper import IPFSWrapper

import datetime

import os

import json, yaml

from decimal import *

if __name__ == "__main__":

    print('iov demo')
    
    filePath = os.path.dirname(__file__)
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    yamlPath = os.path.join(fileNamePath, 'config.yaml')

    conf = None

    with open(yamlPath, "r", encoding='utf-8') as f:
        tmp = f.read()
        conf = yaml.load(tmp)

    mongo_wrapper = MongoWrapper(conf['mongo'])
    ipfs_api = IPFSWrapper(conf['ipfs'])

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
    
    with open(conf['deploy']['abi'], "r") as load_f:
        abi_dat = json.load(load_f)

    w3 = Web3Wrapper(conf['web3'])

    gas = int(Decimal(conf['deploy']['gas']))
    gasPrice = int(Decimal(conf['deploy']['gasPrice']))
    contract_address = conf['web3']['contract_address']

    print('contract_address:', contract_address, 'gas:', gas, ' gasPrice:', gasPrice)
    #exit(0)

    tx = w3.storeHash(today_str, hashVal, contract_address, abi_dat, gas = gas, gasPrice = gasPrice)
    print('store hash tx:', tx)
