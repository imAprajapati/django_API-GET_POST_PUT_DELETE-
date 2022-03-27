from wsgiref import headers
import requests
import json
URL='http://127.0.0.1:8000/student/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        headers={'content-Type':'application/json'}
        r = requests.get(url=URL,headers=headers,data=json_data)
        data=r.json()
        print(data)
    else:
        # data={'id':None}
        json_data=json.dumps(data)
        headers={'content-Type':'application/json'}
        r=requests.get(url=URL,headers=headers,data=json_data)
        data=r.json()
        print(data)

def post_data():
    data={
        'name':'Arpit',
        'roll':104,
        'city':'Noida'
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)


def update_data():
    data={
        'id':2,
        'city':'Noida'
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

def delete_data():
    data={
        'id':2
    }
    json_data=json.dumps(data)
    header={'content-Tyep':'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

delete_data()

# update_data()

# post_data()

# get_data()
