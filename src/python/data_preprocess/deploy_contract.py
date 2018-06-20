# -*- coding: utf-8 -*-
from alphacar.web3_wrapper import Web3Wrapper

import datetime

import json, yaml
import os

from decimal import *

if __name__ == "__main__":
    
    filePath = os.path.dirname(__file__)
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    yamlPath = os.path.join(fileNamePath, 'config.yaml')

    conf = None

    with open(yamlPath, "r", encoding='utf-8') as f:
        tmp = f.read()
        conf = yaml.load(tmp)

    #print('conf[web3]:', conf['web3'])
    
    w3 = Web3Wrapper(conf['web3'])

    abi_dat = None
    bin_dat = None
    
    with open(conf['deploy']['abi'], "r") as load_f:
        abi_dat = json.load(load_f)
    
    #print(abi_dat)

    with open(conf['deploy']['bin'], "r") as load_f:
        bin_dat = load_f.read()

    #print(bin_dat)

    gasPrice = int(Decimal(conf['deploy']['gasPrice']))

    contract_interface = {
        'abi': abi_dat,
        'bin': bin_dat
    }
    
    blockInfo = w3.getBlock()

    nonce = blockInfo['nonce']

    print('nonce:', bytes(nonce))

    tx = w3.deployContractLocal(contract_interface['bin'], gasPrice = gasPrice)

    print('tx:', tx)
    