from concurrent.futures import process
import re, sys, subprocess, os


if __name__ == '__main__':
	os.system('ping -c 3 8.8.8.8 | grep bytes ')
   