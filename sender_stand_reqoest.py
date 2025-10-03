import requests
import configuration
import data


def create_order(body):
    response = requests.post(configuration.URL + configuration.CREATE_ORDER, json=body, headers=data.headers)
    if response.status_code == 201:
        print("\n1. Order created successfully")
    else:
        print(response.status_code)
    order = response.json()
    return order


def get_order_status(track):
    response = requests.get(configuration.URL + configuration.GET_ORDER, params={'t': track})
    if response.status_code == 200:
        print("3. Getting order by status successfully")
    else:
        print(response.status_code)
    return response