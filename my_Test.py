import datetime
import time
import random


def list_print(_list):
    print('#####################')
    for x in _list:
        print(x)
    print('#####################')
    return


ts = []
for _ in range(10):
    now = datetime.datetime.today()
    delta = datetime.timedelta(hours=random.randint(1, 10),
                               minutes=random.randint(1, 100),
                               seconds=random.randint(1, 100),
                               milliseconds=random.randint(1, 1000),
                               microseconds=random.randint(1, 1000))
    ts.append(now + delta)


list_print(ts)

ts_str = list(map(lambda x: x.strftime('%Y%m%d%H%M%S%f'), ts))
list_print(ts_str)

ts_str.sort()
list_print(ts_str)

ts_retime = list(map(lambda x: datetime.datetime.strptime(x, '%Y%m%d%H%M%S%f'), ts_str))
list_print(ts_retime)

ts_timestamp = list(map(lambda x: x.timestamp(), ts_retime))
list_print(ts_timestamp)

