import random
import json
import time
import requests

class Clients:
    def __init__(self, id, api_url):
        self.id = id
        self.api_url = api_url


class Crandom:
    def __init__(self, object):
        self.client = object

    def client_run(self):
        # POST client register
        ordering = self.set_ordering(self.client)
        self.client.is_order = True
        print(ordering)

    def set_ordering(self, client):
        values = {'task': "dsfsdff sdf dsf"}
        user_agent = 'Mozilla/5.0 (compatible; Chrome/22.0.1229.94; Windows NT)'
        headers = {'User-Agent': user_agent, 'Content-Type':'application/json' }
        data = json.dumps(values)
        request = requests.post(client.api_url, data=data, headers=headers)
        response = request.json()
        return response

