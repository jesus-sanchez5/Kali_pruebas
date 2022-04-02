from os import system
import platform, subprocess
import os, datetime

sistema=""

def sistemaOP():
    global sistema
    sistema = platform.system()
    print ("Sistema operativo: ", sistema)

def pingwindows(): 
    a = subprocess.run('ping -n 4 192.168.1.1"')
    print (a)
   

#if len(sys.argv)!=2:
#	print ("Error: Parametros erroneos\nUso:python3 " + sys.argv[1] + " ip-address")
#	exit(1)

if __name__=='__main__':
    print ('Estoy en el main')
    sistemaOP()
    if (sistema == 'Windows'):
        pingwindows()
       