import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'


def get_data(id=None):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data = json_data) # --> get is use for fetching the data
    data = req.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name':'Umar',
        'roll': 4,
        'city': 'Gojra'
    }
    '''Converting the Python data into Json Data'''
    json_data = json.dumps(data)
    res = requests.post(url=URL, data = json_data) # --> POST is used for creating the object. Here, we will be getting the reponse from the View and storing in Var.
    data = res.json()
    print(data)

# post_data()

'''Now we will go to the views.py to write the View for the request'''

def update_data():
    data = {
        'id': 2,
        'name':'Umar',
        'roll': 4,
        'city': 'Chuk 24'
    }
    '''Converting the Python data into Json Data'''
    json_data = json.dumps(data)
    res = requests.put(url=URL,data=json_data) # --> PUT use for updating the whole object.
    data = res.json()
    print(data)

# update_data()

'''Delete data from the database: Permanent delete'''

def delete_data():
    data = {
        'id': 1
    }
    '''Converting the Python data into Json Data'''
    json_data = json.dumps(data)
    res = requests.delete(url=URL,data=json_data) # --> PUT use for updating the whole object.
    data = res.json()
    print(data)

delete_data()


