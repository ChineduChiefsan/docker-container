import json

import  requests


def getdata():
    api_call = requests.get("https://randomuser.me/api/")
    res = api_call.json()
    result = res['results'][0]
    return result

def formatdata(res):
    data = {}
    data['firstname']= res['name']['first']
    data['lastname']= res['name']['last']

    return data


def data():

    res=getdata()
    res=formatdata(res)
    print(json.dumps(res, indent=3))


data()

