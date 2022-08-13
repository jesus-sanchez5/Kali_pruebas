#!/usr/bin/python3
from concurrent.futures import process, thread
import re, sys, subprocess, os, time, threading, signal

interfaces  =[]
respuesta = ""
global inter 

def obtenerInterfaces():
    print("[*][*] Obteneniendo Interfaces [*][*]")
    x=0
    proc = subprocess.Popen(["ifconfig -s | awk 'NR>1{print $1}'", ""], stdout= subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    out = out.split()
    print(f"Interfaces:")
    for salida in out:
        interfaces.append(out[x].decode('utf-8'))
        print(f"{x} - {interfaces[x]}")    	
        x+=1
    
    print()
    
    
def modoMonitor():
    print("[*][*] Elige una interfaz: ", end="")
    inter = input()
    if inter in interfaces:
        print("Interfaz en lista, ¿activar modo monitor? (Y/n):")
        respuesta = input()   
        if respuesta == 'Y' or respuesta =='y' or respuesta == 'yes' or respuesta == 'Yes':
            subprocess.Popen(["sudo airmon-ng check kill", ""], stdout= subprocess.PIPE, shell=True)
            subprocess.Popen(["sudo ifconfig %s down " % inter, ""], stdout= subprocess.PIPE, shell=True)
            subprocess.Popen(["sudo airmon-ng check kill", ""], stdout= subprocess.PIPE, shell=True)
            subprocess.Popen(["sudo iwconfig %s mode monitor" % inter, ""], stdout= subprocess.PIPE, shell=True)
            os.system('sudo iwconfig '+inter+' mode monitor')
            subprocess.Popen(["sudo ifconfig %s up" % inter, ""], stdout= subprocess.PIPE, shell=True)
            print("\nInterfaz modo monitor\n")
            os.system('iwconfig '+inter) 
            time.sleep(3)
           
            
    else:
        print("No existe esta interfaz")

def escanearRedes():
    print("Vamos a escanear redes")
    print("Tiempo de escaneo:", end="")
    os.system('sudo airodump-ng wlan0')
    tiempo = 10
    signal.signal()
    while tiempo:    
        m, s = divmod(tiempo, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        #print(min_sec_format)
        time.sleep(1)
        tiempo -= 1
    signal.SIGINT()
    
    
    
if __name__ == '__main__':
    obtenerInterfaces()
    modoMonitor()
    escanearRedes()
    
   
   


