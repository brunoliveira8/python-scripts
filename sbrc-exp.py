# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:56:48 2015

@author: bruno
"""

import sys

RTIMER_SECOND = 32768
RUNTIME = 30


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
    
    with open(sys.argv[1], "rb") as f:
       for line in f.readlines():
           data = line.split()
           motes[data[1]]["cpu"].append(calculate_pmw(int(data[2]), "cpu"))
           motes[data[1]]["lpm"].append(calculate_pmw(int(data[3]), "lpm"))
           motes[data[1]]["tx"].append(calculate_pmw(int(data[4]), "tx"))
           motes[data[1]]["rx"].append(calculate_pmw(int(data[5]), "rx"))
           motes[data[1]]["sent"].append(int(data[6]))
           motes[data[1]]["fw"].append(int(data[7]))
           
    print motes["ID:2"]

if __name__ == '__main__':
    main()