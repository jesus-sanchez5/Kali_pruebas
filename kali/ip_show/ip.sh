#! /bin/bash

ifconfig eth0 2>/dev/null | grep "inet " | awk '{print $2}'