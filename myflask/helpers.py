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
    def get_order(taxi, list):
        item = filter(lambda t: t['id'] == None, list)

        return item
