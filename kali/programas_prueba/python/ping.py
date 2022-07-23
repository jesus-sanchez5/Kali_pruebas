from concurrent.futures import process
import re, sys, subprocess


if __name__ == '__main__':
	ip="8.8.8.8"
	proc = subprocess.Popen(["ping -c 1 %s" % ip, ""], stdout= subprocess.PIPE, shell=True)
	print(proc.communicate())
   