
from concurrent.futures import process
import re, sys, subprocess, os

a=[]

if __name__ == '__main__':
    
    a.append(os.system("ifconfig -s | awk 'NR>1{print $1}' | grep lo"))
    print(a[0])
   
   


