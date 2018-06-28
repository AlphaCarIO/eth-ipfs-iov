# -*- coding: utf-8 -*-
import app.service.mongo_service as mongo_service
import json

def getLatestUBIInfo() -> dict:
    res = mongo_service.getLatestUBIInfo()
    print ('getLatestUBIInfo:', res)
    return res

def getUbiInfo(ubi_code: str) -> dict:
    res = mongo_service.getUbiInfo(ubi_code)
    return res

def getUbiInfoList(search_type: str, search_txt: str) -> list:
    res = mongo_service.getUbiInfoList(search_type, search_txt)
    return res

def getAllUbiInfoList() -> list:
    res = mongo_service.getUbiInfoList('', '')
    return res
    