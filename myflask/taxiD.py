import time
import random
from clients import Clients, Crandom

start = True
api_url = 'http://127.0.0.1:5000/taxi_api/'
taxi = 10
taxiList = []

for count in xrange(taxi):
    x = Clients(count, int(time.time()+random.randint(100, 10000)), random.randint(1, 100), random.randint(1, 100))
    taxiList.append(x)


while start:

    for client in taxiList:
        Crandom(client).taxi_run()

    print("--------------------------------------------")
    time.sleep(1)




