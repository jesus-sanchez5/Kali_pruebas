#!/usr/bin/python3
from concurrent.futures import process, thread
import re, sys, subprocess, os, time, threading

interfaces=[]
respuesta = ""
inter = ""

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
    os.system('sudo airodump-ng '+inter)
    
    
    
if __name__ == '__main__':
    obtenerInterfaces()
    modoMonitor()
    timer_runs= threading.Event()
    timer_runs.set()
    t = threading.Thread(target=escanearRedes)
    t.start()
    time.sleep(10)
    timer_runs.clear()
    
   
   


