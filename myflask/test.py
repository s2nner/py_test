import time
import random
rt = int(time.time()+300)  # +5 min
a = 1
nl = []
taxi = [{'id': 4, 'lat': 1, 'taxi': False, 'lon': 2,  'time': int(time.time()+random.randint(300, 3500))}]

list = [{'id': 4, 'lat': 7, 'taxi': False, 'lon': 97,  'time': int(time.time()+random.randint(300, 3500))},
        {'id': 5, 'lat': 5, 'taxi': False, 'lon': 9,  'time': None},
        {'id': 6, 'lat': 1, 'taxi': False, 'lon': 1,  'time': int(time.time()+random.randint(100, 300))}]


item = filter(lambda t: t['time'] is None or t['time'] < rt, list)
cl = filter(lambda t: t['lat'] <= 10 and t['lon'] < 10, item)

tlat = 10
tlon = 99
min = 100 ** 2

for idx, item in enumerate(list):

    distance = (tlat - item['lat']) ** 2 + (tlon - item['lon']) ** 2
    print item
    print (tlat - item['lat']) ** 2
    print (tlon - item['lon']) ** 2
    print distance
    print "-----------------------"
    if distance < min:
        min = distance
        nl = item


print nl
print "-----------------------"
print cl


# print item, rt
# if len(cl) is not 0:
#     pass

# print dir(b)
# print b