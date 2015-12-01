import time

class Helpers:
    @staticmethod
    def list_updater(target, list, repl):
        for idx, item in enumerate(list):
            if 'id' in item and target is item['id']:
                list[idx] = repl

        return list[idx]

    @staticmethod
    def list_del(target, list):
        for idx, item in enumerate(list):
            if 'id' in item and target is item['id']:
                del list[idx]

    @staticmethod
    def is_client(target, list):
        item = filter(lambda t: t['id'] == target, list)
        if len(item) == 0:
            return False
        return item

    @staticmethod
    def get_order(taxi, list2):
        rt = int(time.time()+300)  # +5 min
        item = filter(lambda t: t['time'] is None or t['time'] < rt, list2)
        min = 100 ** 2
        client = False

        for idx, item in enumerate(item):

            distance = (taxi['lat'] - item['lat']) ** 2 + (taxi['lon'] - item['lon']) ** 2
            if distance < min:
                min = distance
                client = item

        return client
