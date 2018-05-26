# -*- coding: utf-8 -*-
from lib.web3_wrapper import Web3Wrapper

import datetime
import json

WEB3_CONFIG = {
    'config': 'config.json',
}

FOLDER_PATH = '../iov-prj/build/IOVContract'

FILE_PREFIX = 'IOVContract'

if __name__ == "__main__":

    w3 = Web3Wrapper('config.json')

    abi_dat = None
    bin_dat = None
    
    with open('%s/%s.abi' % (FOLDER_PATH, FILE_PREFIX), "r") as load_f:
        abi_dat = json.load(load_f)
    
    #print(abi_dat)

    with open('%s/%s.bin' % (FOLDER_PATH, FILE_PREFIX), "r") as load_f:
        bin_dat = load_f.read()

    #print(bin_dat)

    contract_interface = { 
        'abi': abi_dat,
        'bin': bin_dat
    }
    
    blockInfo = w3.getBlock()

    nonce = blockInfo['nonce']
    
    #print('getBlock:', w3.getBlock())

    print('nonce:', bytes(nonce))

    tx = w3.deployContractLocal(contract_interface['bin'], gasPrice = 30 * 10 ** 9)

    print('tx:', tx)
    