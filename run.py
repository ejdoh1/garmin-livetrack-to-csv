import json
import requests
import time
import pandas
from pandas import json_normalize


def run(event, context):
    s = event['pathParameters']['session']
    # t0 = time.time_ns() // 1_000_000
    # t1 = int(t0 - 60 * 1e3)
    # u = f"https://livetrack.garmin.com/services/session/{s}/trackpoints?requestTime={t0}&from={t1}"
    u = f"https://livetrack.garmin.com/services/session/{s}/trackpoints"
    r = requests.get(u).json()
    n = json_normalize(r['trackPoints'][len(r['trackPoints'])-1])
    return {
        "statusCode": 200,
        "body": n.to_csv()
    }
