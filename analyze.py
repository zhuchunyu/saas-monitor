# -*- coding: utf-8 -*-
import time

import pandas as pd
import prediction_seasonal as prediction_seasonal
from pymongo import MongoClient
import urllib.parse

import envconfig
config = envconfig.getConfig()

username = urllib.parse.quote_plus(config['MONGO_USER'])
password = urllib.parse.quote_plus(config['MONGO_PWD'])

mongoClient = MongoClient('mongodb://%s:%s@%s:%s' % (username, password, config['MONGO_HOST'], config['MONGO_PORT']))
print(mongoClient)

rightcloud = mongoClient[config['MONGO_DATABASE']]

predictions = rightcloud["predictions"]
print(predictions)

def worker(data, resourceId, commonMetricName):
    print(resourceId)

    data = pd.DataFrame(data)
    data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')
    data.set_index(['time'], inplace=True)

    pred = prediction_seasonal.prediction_seasonal_pred(data, start=data.index[-5], end=pd.to_datetime('2019-01-18 16:00:00'))
    pred_ci = pred.conf_int()

    avgValues = toList(pred.predicted_mean)
    minValues = toList(pred_ci.iloc[:, 0])
    maxValues = toList(pred_ci.iloc[:, 1])

    print('Save to mongo...')
    pred_data = {
        'avgValues': avgValues,
        'minValues': minValues,
        'maxValues': maxValues,
        'resource_id': resourceId,
        'commonMetricName': commonMetricName,
        'created_dt': time.time()
    }

    inserted = predictions.insert_one(pred_data)
    print(inserted.inserted_id)

def toList(series):
    values = []
    for idx in series.index:
        values.append({
            'time': idx.to_pydatetime().strftime("%Y-%m-%d %H:%M:%S"),
            'value': series[idx]
        })

    return values