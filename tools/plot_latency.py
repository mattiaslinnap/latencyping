#!/usr/bin/env python
# As close to Python3 as 2.7 can get
from __future__ import absolute_import, division, print_function, unicode_literals
from collections import defaultdict
from future_builtins import *  # ascii, filter, hex, map, oct, zip

from matplotlib import pyplot as pp
import re
import datetime

from pyshort import plot

FILENAME = 'latency_data.txt'


def parse_line(line):
    m = re.match(r'^([A-Za-z0-9]+) .* delay=([0-9]+)ms, start=([0-9]+):([0-9]+):([0-9]+)$', line)
    assert m, 'No match in line %r' % line
    network = m.group(1)
    delay = int(m.group(2))
    hour = int(m.group(3))
    minute = int(m.group(4))
    second = int(m.group(5))
    return network, delay, datetime.datetime(2013, 8, 18, hour, minute, second)


def read_data():
    network_delays = defaultdict(list)
    network_times = defaultdict(list)
    with open(FILENAME) as f:
        for line in f:
            network, delay, time = parse_line(line)
            delay /= 1000
            network = network.replace('Tmobile', 'T-Mobile')
            network_delays[network].append(delay)
            network_times[network].append(time)
    return network_delays, network_times


def main():
    delays, times = read_data()

    plot.close_figure_on_key(pp.figure())
    for network in sorted(delays):
        pp.plot(times[network], delays[network], label=network)
    pp.legend(loc='upper left')
    pp.xlabel('Wall clock time')
    pp.ylabel('Time to download 5KB (seconds)')
    plot.vertical_x_labels(pp.gca())
    pp.show()

    print(sorted(delays))

if __name__ == '__main__':
    main()

