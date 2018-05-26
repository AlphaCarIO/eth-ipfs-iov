#!/bin/bash

#UNLOCK_LIST="--password /root/password --etherbase=0xda83aee0f49802a331d455f503341a5fdcbde923 --unlock 0xbb65f9eb3a78ff3ebbc91e182ad9f3337b6329db,0x86daa582987c76b513574919163b9c2925ef7134,0x509665305fe40c916eedafc7442a25acd8896fb6,0xbca685cb5dfd40658eabe435c56559915aa1b815,0xda83aee0f49802a331d455f503341a5fdcbde923,0xcd98183b5497ab12ca22421a48c92864524da3f0"
UNLOCK_LIST="--password /root/password --etherbase=0xda83aee0f49802a331d455f503341a5fdcbde923 --unlock 0xda83aee0f49802a331d455f503341a5fdcbde923"

export UNLOCK_LIST

echo $UNLOCK_LIST

geth --testnet --syncmode "fast" --cache 1024 --datadir=/data_dir \
--rpcapi "admin,debug,eth,miner,net,personal,rpc,txpool,web3" \
--rpc --rpcaddr 0.0.0.0 --rpcport 8545 --port 30303 \
--bootnodes "enode://94c15d1b9e2fe7ce56e458b9a3b672ef11894ddedd0c6f247e0f1d3487f52b66208fb4aeb8179fce6e3a749ea\
93ed147c37976d67af557508d199d9594c35f09@192.81.208.223:30303,enode://20c9ad97c081d63397d7b685a412227a40e23c8bdc6688\
c6f37e97cfbc22d2b4d1db1510d8f61e6a8866ad7f0e17c02b14182d37ea7c3c8b9c2683aeb6b733a1@52.169.14.227:30303,enode://6ce0\
5930c72abc632c58e2e4324f7c7ea478cec0ed4fa2528982cf34483094e9cbc9216e7aa349691242576d552a2a56aaeae426c5303ded677ce45\
5ba1acd9d@13.84.180.240:30303,enode://cbe35181d8b56779d1ecc05400a86bccb2be5629eb0a910b1dc91427df50204f38c12ffa827e1\
235cae0013a22922869e0de579406393e04d2430111e58c828d@13.92.188.53:30303,enode://4027f297dc3f512ef1afb2866b0421e01a69\
83b255578fcd220df01899138ba200cf1aaecf9f870c6aef50cdaca4a932c1bbd41559117049b8b4da9d9fc81e9b@137.74.46.89:52101,\
enode://b82d691bab934fca0daefc735b88ef8dd818ca01308169ce9a8d95149aeb32fe39a8b61909c5e23b1de3ecbd1efd0b72d75061085b20\
c1cce8dbe2accdc17ab7@47.88.152.225:30903" \
 --rpccorsdomain '*' $UNLOCK_LIST >/data_dir/geth.log
#--mine --minerthreads $MINER_COUNT
