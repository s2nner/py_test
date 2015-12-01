import time
import random
from clients import Clients, Crandom

start = True
clients = 2
api_url = 'http://127.0.0.1:5000/client_api/'
clientsList = []

for count in xrange(clients):
    if random.randint(1, 100) > 150:
        cltime = int(time.time()+random.randint(100, 1000))
    else:
        cltime = None
    x = Clients(count, cltime, random.randint(1, 100), random.randint(1, 100), api_url)
    clientsList.append(x)


while start:

    for client in clientsList:
        Crandom(client).client_run()

    print("--------------------------------------------")
    time.sleep(20)




