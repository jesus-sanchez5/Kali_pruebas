#!/usr/bin/python3
from concurrent.futures import process
import re, sys, subprocess, os

interfaces=[]


def obtenerInterfaces():
    print("[*][*] Obteneniendo Interfaces [*][*]")
    x=0
    proc = subprocess.Popen(["ifconfig -s | awk 'NR>1{print $1}'", ""], stdout= subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    out = out.split()
    pattern = r'\w+'
    #print(out)
    print(f"Interfaces:")
    for salida in out:
    	interfaces.append(out[x].decode('utf-8'))
    	print(f"{x} - {interfaces[x]}")    	
    	x+=1
    x=0
    
    print()
    
    
def elegirInterfaz():
	print("[*][*] Elige una interfaz: ", end="")
	inter = input()
	if inter in interfaces:
		print("Interfaz en lista")
	else:
		print("No existe esta interfaz")

if __name__ == '__main__':
	obtenerInterfaces()
	elegirInterfaz()
    
   


