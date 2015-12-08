# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:56:48 2015

@author: bruno
"""

import sys
import os

FLAG = 1

nodes = [2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
    31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 
    44, 45, 46, 47,48]


def main():

  if FLAG == 0:
    for node in nodes:
      with open('final-results/balanced-rpl-80-8/mote{}.txt'.format(node), 'r') as f:
        lines =  f.readlines()

        MAX = len(lines)
        
        if MAX > 0:
          print lines[MAX-1].split()[5]
      

  else:
    for node in nodes:
      with open('final-results/balanced-rpl-80-12/mote{}.txt'.format(node), 'r') as f:
        lines =  f.readlines()

        MAX = len(lines)
        
        if MAX > 0:
          if lines[MAX-1].split()[0] == '#1':
            print lines[MAX-1].split()[3]
          else:
            print lines[MAX-2].split()[3]



if __name__ == '__main__':
    main()