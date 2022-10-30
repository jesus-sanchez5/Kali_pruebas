#! /usr/bin/env python

import sys
from scapy import *

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()
    sr1(p)
