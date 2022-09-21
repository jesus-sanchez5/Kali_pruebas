#!/usr/bin/python3

import subprocess, re, sys

#ping -c 1 ipp
#whichsystem.py 

def return_ttl(address):
	proc = subprocess.Popen(["ping -c 1 %s" %address,""],stdout=subprocess.PIPE, shell=True)
	(out,err)=proc.communicate()
	out = out.split()
	print (str(out[12]))
	out2 = re.findall(r"\d{1,3}",str(out[12]))
	print(out2)

if len(sys.argv)!=2:
	print ("Error: Parametros erroneos\nUso:python3 " + sys.argv[1] + " ip-address")
	exit(1)


if __name__=='__main__':
	print ("Estoy en el main")
	addr = sys.argv[1]
	print (addr)

	ttl = return_ttl(addr)
