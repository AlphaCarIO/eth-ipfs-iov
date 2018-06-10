# -*- coding: utf-8 -*-
from backend.app.lib.web3_wrapper import Web3Wrapper

import datetime
import json

WEB3_CONFIG = {
    'config': 'config.json',
}

if __name__ == "__main__":

    w3 = Web3Wrapper('config.json')

    CONTRACT_CONFIG = None
    abi_dat = None
    bin_dat = None
    
    with open('deploy.json', "r") as load_f:
        CONTRACT_CONFIG = json.load(load_f)
    
    with open(CONTRACT_CONFIG['abi'], "r") as load_f:
        abi_dat = json.load(load_f)
    
    #print(abi_dat)

    with open(CONTRACT_CONFIG['bin'], "r") as load_f:
        bin_dat = load_f.read()

    #print(bin_dat)

    contract_interface = { 
        'abi': abi_dat,
        'bin': bin_dat
    }
    
    blockInfo = w3.getBlock()

    nonce = blockInfo['nonce']

    print('nonce:', bytes(nonce))

    tx = w3.deployContractLocal(contract_interface['bin'], gasPrice = 30 * 10 ** 9)

    print('tx:', tx)
    