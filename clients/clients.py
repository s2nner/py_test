import urllib
import urllib2
import random
import json
import time

class Clients:

    def __init__(self, id, time, lat, lon, api_url):
        self.id = id
        self.time = time
        self.lat = lat
        self.lon = lon
        self.is_order = False
        self.t_reg = False
        self.api_url = api_url
        self.taxi = False

class Crandom:

    def __init__(self, object):
        self.client = object

    def taxi_run(self):
        # POST taxi register
        if self.client.t_reg is False:
            ordering = self.set_ordering(self.client)
            self.client.t_reg = True
            # print(ordering)

        # GET taxi order info
        if self.client.t_reg is True:
            resp = self.get_order(self.client)
            print(resp)


    def client_run(self):
        # POST client register
        if self.client.is_order is False:
            ordering = self.set_ordering(self.client)
            self.client.is_order = True
            # print(ordering)

        # PUT client time update
        if self.client.is_order is True and random.randint(0, 100) > 70:  # 30 percent
            ordering = self.update_ordering(self.client)
            # print(ordering)

        # DELETE client order del
        if self.client.is_order is True and random.randint(0, 100) > 90:  # 10 percent
            ordering = self.del_ordering(self.client)
            self.client.is_order = False
            # print(ordering)

        # GET client order info
        if self.client.is_order is True:
            resp = self.get_order(self.client)
            print(resp)

        # GETALL client order info
        # resp = self.get_all_order(self.client)
        print("======================================================")
        # print(resp)


    def set_ordering(self, client):
        values = {'client_id': client.id, 'time': client.time, 'lat': client.lat, 'lon': client.lon, 'is_order': client.is_order, 'taxi': client.taxi}
        opener = urllib2.build_opener()
        request = urllib2.Request(client.api_url+'api/v1.0/orders', json.dumps(values))
        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda: 'POST'
        url = opener.open(request)
        return url.read()

    def update_ordering(self, client):
        values = {'client_id': client.id, 'time': int(time.time()+random.randint(100, 10000)), 'lat': client.lat,
                  'lon': client.lon, 'is_order': client.is_order, 'taxi': client.taxi}
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(client.api_url+'api/v1.0/orders/{}'.format(client.id), json.dumps(values))
        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda: 'PUT'
        url = opener.open(request)
        return url.read()

    def del_ordering(self, client):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(client.api_url+'api/v1.0/orders/{}'.format(client.id))
        request.get_method = lambda: 'DELETE'
        url = opener.open(request)
        return url.read()

    def get_order(self, client):
        values = {'cid': client.id}
        data = urllib.urlencode(values)
        opener = urllib2.build_opener()

        request = urllib2.Request(client.api_url+'api/v1.0/orders/{}'.format(client.id), data)
        request.add_header('Content-Type', 'api/1.0')
        request.get_method = lambda: 'GET'
        url = opener.open(request)
        return url.read()

    def get_all_order(self, client):
        values = {'cid': client.id}
        data = urllib.urlencode(values)
        opener = urllib2.build_opener()

        request = urllib2.Request(client.api_url+'api/v1.0/orders', data)
        request.add_header('Content-Type', 'api/1.0')
        request.get_method = lambda: 'GET'
        url = opener.open(request)
        return url.read()


