# -*- coding: utf-8 -*-

import os

def getConfig():
    MONGO_HOST = os.getenv('MONGO_HOST', '10.68.6.3')
    MONGO_PORT = os.getenv('MONGO_IP', '27017')
    MONGO_DATABASE = os.getenv('MONGO_IP', 'rightcloud')
    MONGO_USER = os.getenv('MONGO_IP', 'rightcloud')
    MONGO_PWD = os.getenv('MONGO_IP', 'H89lBgAg')

    return {
        'MONGO_HOST': MONGO_HOST,
        'MONGO_PORT': MONGO_PORT,
        'MONGO_DATABASE': MONGO_DATABASE,
        'MONGO_USER': MONGO_USER,
        'MONGO_PWD': MONGO_PWD
    }