#!/bin/bash

dist_root=../../../alphacar-browser
dist=$dist_root/dist

if [ -n "$1" ]; then
    dist=$1
fi

rm -rf dist

if [ ! -d $dist ]; then
    cur_d=`pwd`
    echo 'cur_d:'$cur_d
    cd $dist_root
    npm run build
    cd $cur_d
fi

cp -rf $dist dist
