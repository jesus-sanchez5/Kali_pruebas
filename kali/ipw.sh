#! /bin/bash

ifconfig wlan0 2>/dev/null | grep "inet " | awk '{print $2}'