# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:56:48 2015

@author: bruno
"""

import sys


def main():
    motes = {}
    
    with open(sys.argv[1], "rb") as f:
       for line in f.readlines():
           data = line.split()
           print data

if __name__ == '__main__':
    main()