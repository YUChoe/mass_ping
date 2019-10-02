import subprocess
import threading
from socket import inet_aton
import time


def is_format_ip(ip):
    try:
        inet_aton(ip)
        return True
    except:
        return False

class MassPing(object):

    def __init__(self, hosts=[], thread_count=4, test_count=1):
        self.status = {'alive': [], 'dead': [], 'flapping': []}
        self.hosts = hosts
        self.test_count = test_count
        self.thread_count = thread_count
        self.lock = threading.Lock()

    """
    status = {'alive': [], 'dead': [], 'flapping': []}
    hosts = []

    thread_count = 4  # default
    test_count = 1

    lock = threading.Lock()

    """
    def each_ping(self, ip):
        ping_cmd = ['ping', '-c', '1', '-W', '1', ip]
        ret = subprocess.call(ping_cmd, stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
        return ret == 0

    def ping(self, ip, test_count):
        flapping = False
        for x in range(test_count):
            if self.each_ping(ip):
                return (flapping, "alive")
            flapping = True
            if x != test_count - 1:  # sleep 1 only not last item
                time.sleep(1)
        return (flapping, "dead")

    def pop_queue(self):
        ip = None
        self.lock.acquire()
        if self.hosts:
            ip = self.hosts.pop()
        self.lock.release()
        return ip

    def dequeue(self):
        while True:
            ip = self.pop_queue()

            if not ip:
                return None

            (flapping, result) = self.ping(ip, self.test_count)
            if result == 'alive' and flapping == True:
                self.status['flapping'].append(ip)
                # also ip is 'alive' too

            self.status[result].append(ip)

    def start(self):
        threads = []

        for i in range(self.thread_count):
            t = threading.Thread(target=self.dequeue)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        return self.status


if __name__ == '__main__':
    pass
    ping = MassPing()
    ping.thread_count = 6
    ping.test_count = 1
    ping.hosts = ['8.8.8.8', '8.8.4.4', 'yahoo.com', 'ns.speedvpn.net', 'noizze.net', '1.1.1.1']

    stime = time.time()
    new_result = ping.start()
    ftime = time.time()

    print('result:', new_result)
    print('delta:', ftime-stime, 'msec')