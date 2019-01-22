# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import multiprocessing
import analyze
import pymongo
from pymongo import MongoClient
import urllib.parse
import time

username = urllib.parse.quote_plus('rightcloud')
password = urllib.parse.quote_plus('H89lBgAg')

mongoClient = MongoClient('mongodb://%s:%s@10.68.6.3:27017' % (username, password))
print(mongoClient)

rightcloud = mongoClient["rightcloud"]

predictions = rightcloud["predictions"]
print(predictions)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome Analyze!'


@app.route('/job', methods=["POST"])
def add_job():
    # 处理和验证原始数据
    data = [{"time":x['time'], "average":x["average"]} for x in request.json['data']]

    p = multiprocessing.Process(target=analyze.worker,
                                args=(data, request.json['resourceId'], request.json['commonMetricName'],))
    p.start()

    return jsonify(
        code = 0,
        msg = 'Forecasting',
        resourceId = request.json['resourceId']
    )

@app.route('/preded', methods=["GET"])
def preded():
    start = time.time()
    prededList = predictions.find({}).sort("created_dt", pymongo.DESCENDING).limit(1)
    latested = None
    for p in prededList:
        latested = p
        break

    data = None
    if latested:
        data = {
            'avgValues': latested['avgValues'],
            'minValues': latested['minValues'],
            'maxValues': latested['maxValues'],
            'resource_id': latested['resource_id'],
            'commonMetricName': latested['commonMetricName'],
            'created_dt': latested['created_dt']
        }

    print('query time used %.2f sec' % (time.time() - start))

    return jsonify(
        code=0,
        msg='ok',
        data = data
    )

@app.route('/json', methods=["GET"])
def json():
    return jsonify(
        name='alex',
        age='18',
        data=[1,2,3],
        map={'Michael': 95, 'Bob': 75, 'Tracy': 85}
    )
