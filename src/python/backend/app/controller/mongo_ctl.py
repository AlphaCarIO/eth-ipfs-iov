# -*- coding: utf-8 -*-
import app.service.mongo_service as mongo_service
import json

def getAllInfosByDate(date_str: str) -> str:
    res = mongo_service.getAllInfosByDate(date_str)
    #print('getAllInfosByDate:', res)
    return res
    