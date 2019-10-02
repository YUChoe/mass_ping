from src.mass_ping import MassPing
import time
from pprint import pprint

def test_ping1():
    hosts = ['8.8.8.8', '8.8.4.4', 'yahoo.com', 'ns.speedvpn.net', 'noizze.net']
    ping1 = MassPing(hosts=hosts, thread_count=len(hosts), test_count=1)

    stime = time.time()
    new_result = ping1.start()
    ftime = time.time()

    return {'result': new_result, 'delta': (ftime-stime)}

def test_ping2():
    hosts = ['1.1.1.1', '1.1.2.2', '1.1.3.3', '1.1.4.4']
    ping2 = MassPing(hosts=hosts, thread_count=len(hosts), test_count=1)

    stime = time.time()
    new_result = ping2.start()
    ftime = time.time()

    return {'result': new_result, 'delta': (ftime-stime)}

def test_ping3():
    hosts = []
    ping3 = MassPing(hosts=hosts, thread_count=len(hosts), test_count=1)

    stime = time.time()
    new_result = ping3.start()
    ftime = time.time()

    return {'result': new_result, 'delta': (ftime-stime)}

if __name__ == '__main__':
    test_result = test_ping1()
    pprint(test_result['result'])
    print('delta:', '{0:.3f}'.format(test_result['delta']), 'msec')
    test_result = {}

    test_result = test_ping2()
    pprint(test_result['result'])
    print('delta:', '{0:.3f}'.format(test_result['delta']), 'msec')
    test_result = {}

    test_result = test_ping3()
    pprint(test_result['result'])
    print('delta:', '{0:.3f}'.format(test_result['delta']), 'msec')