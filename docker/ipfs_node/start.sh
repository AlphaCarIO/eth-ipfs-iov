#!/bin/bash

is_empty_dir() { 
    return `ls -A $1|wc -w`
}

DN="/root/.ipfs"

if [ -n "$1" ]; then
    DN=$1
fi

echo "DN: "$DN
l_fileCount=`ls ${DN} | wc -l`
echo "fileCount: ${l_fileCount}"

if [ ! -d $DN -o ! "$l_fileCount" -gt "0" ]; then
    echo "-----> ipfs init..."
    ipfs init
    echo "-----> ipfs config..."
    ipfs config Addresses.API /ip4/0.0.0.0/tcp/5001
    ipfs config Addresses.Gateway /ip4/0.0.0.0/tcp/8080
fi

ipfs daemon
