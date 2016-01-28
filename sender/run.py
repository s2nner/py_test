import time
from clients import Clients, Crandom

# curl -i -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d "{\"task\":\"Read a book\"}" http://127.0.0.1:5000/api/v1/testing
start = True
clc = 1
api_url = 'http://127.0.0.1:5000/api/v1/auth/signin'
# api_url = 'http://127.0.0.1:5000/api/v1/auth/signup'
clientsList = []
json = {'type': "simple", 'user': "user", 'pswd': "q"}

for count in range(clc):
    x = Clients(count, api_url, json)
    clientsList.append(x)

while start:
    for client in clientsList:
        Crandom(client).client_run()

    print("---"*20)
    time.sleep(2)

