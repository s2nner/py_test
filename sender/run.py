import time
from clients import Clients, Crandom


start = True
clc = 1
api_url = 'http://127.0.0.1:5000/api/v1/auth/signup'
clientsList = []

for count in range(clc):
    x = Clients(count, api_url)
    clientsList.append(x)

while start:
    for client in clientsList:
        Crandom(client).client_run()

    print("---"*20)
    time.sleep(2)




