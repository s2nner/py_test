import time
import storage

class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'sheld:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        },
        {
            'id': 'push',
            'func': 'sheld:push',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 25
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True

def job1(a, b):
    """
    Test
    """
    print("========================================================")
    print (storage.clientsList)
    # print(__name__)
    # print(time.time())

def push(a, b):
    """
    Push data to client
    """
    pass

