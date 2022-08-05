
from concurrent.futures import process
import re, sys, subprocess, os


if __name__ == '__main__':
	os.system('ifconfig -s | awk 'NR>1{print $1}'')
   


