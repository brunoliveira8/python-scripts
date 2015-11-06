# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:56:48 2015

@author: bruno
"""

import sys
import os

RTIMER_SECOND = 32768
RUNTIME = 30

PATH = "data"



nodes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
    31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 
    44, 45, 46, 47,48, 49]



    
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

  for node in nodes:
    with open('data/mote{}.txt'.format(node), 'r') as f:
      mote = {'tx': [], 'rx' : []}
      for line in f.readlines():
             data = line.split() 
             mote['tx'].append(calculate_pmw(int(data[0]), 'tx'))
             mote['rx'].append(calculate_pmw(int(data[1]), 'rx'))
    
      
      if len(mote['rx']) > 0:
        tx_pw = reduce(lambda x,y: x+y, mote["tx"])
        rx_pw = reduce(lambda x,y: x+y, mote["rx"])

        with open('power.txt', 'a') as f1:
          f1.write('mote{}: tx = {}  rx = {}  total = {}\n'.format(node, tx_pw, rx_pw, tx_pw+rx_pw))
          f1.close()



if __name__ == '__main__':
    main()