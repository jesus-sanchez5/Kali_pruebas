import re, sys, subprocess


if __name__ == '__main__':

	proc = subprocess.Popen(["/usr/bin/ping -c 1 8.8.8.8"], stdout= subprocess.PIPE, shell=True)