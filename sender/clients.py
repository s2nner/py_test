import random
import json
import time
import requests

class Clients:
    def __init__(self, id, api_url, json):
        self.id = id
        self.api_url = api_url
        self.json = json


class Crandom:
    def __init__(self, object):
        self.client = object

    def client_run(self):
        # POST client register
        request = self.set_ordering(self.client)
        print("{}  {}".format(request.status_code, request.json()))

    def set_ordering(self, client):
        user_agent = 'Mozilla/5.0 (compatible; Chrome/22.0.1229.94; Windows NT)'
        headers = {'User-Agent': user_agent, 'Content-Type':'application/json' }
        data = json.dumps(client.json)
        request = requests.post(client.api_url, data=data, headers=headers)
        return request

