import requests
import configuration
import data

def create_order (body) :
    response = requests.post(configuration.URL + configuration.CREATE_ORDER, json=body, headers=data.headers)
    track = response.json()
    return track["track"]

order_track = create_order(data.order)

def get_order_status (track) :
    response = requests.get(configuration.URL + configuration.GET_ORDER, params={'t': track})
    return response.status_code
