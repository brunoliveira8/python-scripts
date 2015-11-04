# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:56:48 2015

@author: bruno
"""

import sys
import os

RTIMER_SECOND = 32768
RUNTIME = 30

PATH = "8-10"

def init_motes(number):
    motes = {}    
    for x in range(2,number+1):
        motes["ID:"+str(x)] = dict(cpu=[], lpm=[], tx=[], rx=[], sent=[], fw=[])
    return motes
    
def calculate_pmw(value, opt):
    
    voltage = 3.0    
    
    if opt == "cpu":
        current = 0.33
    elif opt == "lpm":
        current = 0.0011
    elif opt == "tx":
        current = 18.8
    elif opt == "rx":
        current = 17.4
    else:
        current = 0
        
    return (value*current*voltage)/RTIMER_SECOND/RUNTIME

def main():
    motes =init_motes(5)
    
    with open(os.path.join(PATH,sys.argv[1]), "rb") as f:
       
       for line in f.readlines():
           data = line.split()
           motes[data[1]]["cpu"].append(calculate_pmw(int(data[2]), "cpu"))
           motes[data[1]]["lpm"].append(calculate_pmw(int(data[3]), "lpm"))
           motes[data[1]]["tx"].append(calculate_pmw(int(data[4]), "tx"))
           motes[data[1]]["rx"].append(calculate_pmw(int(data[5]), "rx"))
           motes[data[1]]["sent"].append(int(data[6]))
           motes[data[1]]["fw"].append(int(data[7]))
          
       
       
       cpu_pw = reduce(lambda x,y: x+y, motes["ID:2"]["cpu"])
       lpm_pw = reduce(lambda x,y: x+y, motes["ID:2"]["lpm"])
       tx_pw = reduce(lambda x,y: x+y, motes["ID:2"]["tx"])
       rx_pw = reduce(lambda x,y: x+y, motes["ID:2"]["rx"])
       
       print cpu_pw, lpm_pw, tx_pw, rx_pw
       print cpu_pw+lpm_pw+tx_pw+rx_pw
       
       
        
       cpu_pw = reduce(lambda x,y: x+y, motes["ID:3"]["cpu"])
       lpm_pw = reduce(lambda x,y: x+y, motes["ID:3"]["lpm"])
       tx_pw = reduce(lambda x,y: x+y, motes["ID:3"]["tx"])
       rx_pw = reduce(lambda x,y: x+y, motes["ID:3"]["rx"])
       
       print cpu_pw, lpm_pw, tx_pw, rx_pw
       print cpu_pw+lpm_pw+tx_pw+rx_pw
       
    

if __name__ == '__main__':
    main()