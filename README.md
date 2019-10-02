[![Latest Version](https://img.shields.io/pypi/v/mass-ping.svg)](https://pypi.org/project/mass-ping/)

# Mass Ping

A multi-threaded ICMP ping using /bin/ping, ping.exe.

## Features
* You can get a quick result.
* It detects ping flapping.
* You don't need root privilege to send a ping.
* It has no dependency as using only python standard library.


## Installation
Run the folowing to install:

```shell
pip install mass-ping
```

## Usage

```python
>>> from mass_ping import MassPing
>>> hosts = ['8.8.8.8', '8.8.4.4', 'yahoo.com', 'ns.speedvpn.net', 'noizze.net']
>>> ping = MassPing(hosts=hosts, thread_count=len(hosts), test_count=2)  # test_count=2 means when ping fails retry 1 more time
>>> result = ping.start()
>>> from pprint import pprint
>>> pprint(result)
{'alive': ['8.8.4.4', '8.8.8.8', 'noizze.net', 'ns.speedvpn.net', 'yahoo.com'],
 'dead': [],
 'flapping': []}
```
