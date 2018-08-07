#!/bin/bash

dist=../../../alphacar-browser/dist

if [ -n "$1" ]; then
    dist=$1
fi

rm -rf dist
cp -rf $dist dist
