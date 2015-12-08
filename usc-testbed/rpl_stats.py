# -*- coding: utf-8 -*-
import sys 

nodes = [2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
    31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 
    44, 45, 46, 47,48]

motes_tree_size = {'6ce6': 0, 'edbc': 0 , '50f4': 0, '629b': 0,
            '6658':0, '619e':0, 'cf11':0, 'f361': 0,
            '6300':0, '209c':0, '79b6':0, '62b9':0,
            'f078':0, '4baa':0, '76e7': 0, 'cdeb': 0,
            '81fc': 0, '53b8': 0, '1d33': 0, '4d6a':0,
            '7233': 0, '4527': 0, '46a3':0, 'fcaf':0,
            'c006': 0, '44ea':0, 'e886':0, '823d': 0,
            'b6c8': 0, '4d05': 0, 'e61f': 0, '667e': 0,
            '7f43': 0, '6449': 0, '117a': 0, '5966': 0,
            '4d35': 0, '6fb1':0,'ea5d':0, 'f23f':0,
            '4960':0,
            } 

motes_ip = ['edbc' , '50f4', '629b',
            '6658', '619e', 'cf11', 'f361',
            '6300', '209c', '79b6', '62b9',
            'f078', '4baa', '76e7', 'cdeb',
            '81fc', '53b8', '1d33', '4d6a',
            '7233', '4527', '46a3', 'fcaf',
            'c006', '44ea', 'e886', '823d',
            'b6c8', '4d05', 'e61f', '667e',
            '7f43', '6449', '117a', '5966',
            '4d35', '6fb1','ea5d', 'f23f',
            '4960']

motes_hop = {}

def sub_tree_size():
     for node in nodes:
        with open('normal-rpl-tree/mote{}.txt'.format(node), 'r') as f:
            lines = f.readlines()
            max_line = len(lines)
            
            u = lines[max_line-1].split(':')[1] #edita aqui para mudar o instantes da arvore
            u = u.split('\n')[0]
            motes_tree_size[u] = motes_tree_size[u]+1
        

def get_hops():
    count = 0
    for node in nodes:
            with open('normal-rpl-tree/mote{}.txt'.format(node), 'r') as f:
                lines = f.readlines()
                max_line = len(lines)
                u = lines[max_line-1].split(':')[1] #edita aqui para mudar o instantes da arvore
                u = u.split('\n')[0]
                motes_hop[motes_ip[count]] = u
                count = count + 1
                

def main():
    sub_tree_size()
    get_hops()
    for x in motes_ip:
        print x


if __name__ == '__main__':
    main()