import httplib

conn = httplib.HTTPSConnection("localhost", 5000)
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
