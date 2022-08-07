#!/usr/bin/python3
from concurrent.futures import process
import re, sys, subprocess, os

interfaces=[]
respuesta = ""

def obtenerInterfaces():
    print("[*][*] Obteneniendo Interfaces [*][*]")
    x=0
    proc = subprocess.Popen(["ifconfig -s | awk 'NR>1{print $1}'", ""], stdout= subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    out = out.split()
    #pattern = r'\w+'
    #print(out)
    print(f"Interfaces:")
    for salida in out:
        interfaces.append(out[x].decode('utf-8'))
        print(f"{x} - {interfaces[x]}")    	
        x+=1
    
    print()
    
    
def elegirInterfaz():
    print("[*][*] Elige una interfaz: ", end="")
    inter = input()
    if inter in interfaces:
        print("Interfaz en lista, ¿activar modo monitor? (Y/n):")
        respuesta = input()   
        if respuesta == 'Y' | respuesta =='y' | respuesta == 'yes' | respuesta == 'Yes':
            print()
            os.system('sudo airmon-ng check kill')
            os.system('sudo ifconfig '+inter+' down ')
            os.system('sudo airmon-ng check kill')
            os.system('sudo iwconfig '+inter+' mode monitor')
            os.system('sudo ifconfig '+inter+' up')
            os.system('iwconfig'+inter)
    else:
        print("No existe esta interfaz")

if __name__ == '__main__':
    obtenerInterfaces()
    elegirInterfaz()
    
   
   


