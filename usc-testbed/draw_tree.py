# -*- coding: utf-8 -*-
import pydot
import sys 

nodes = [2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
    31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 
    44, 45, 46, 47,48]

motes_ip = {'6ce6':'1', 'edbc':'2', '50f4':'3', '629b':'4',
            '6658':'5', '619e':'8', 'cf11':'9', 'f361':'10',
            '6300':'11', '209c':'12', '79b6':'13', '62b9':'14',
            'f078':'15', '4baa':'18', '76e7':'19', 'cdeb':'20',
            '81fc':'21', '53b8':'22', '1d33':'23', '4d6a':'24',
            '7233':'25', '4527':'26', '46a3':'27', 'fcaf':'28',
            'c006':'31', '44ea':'32', 'e886':'33', '823d':'34',
            'b6c8':'36', '4d05':'37', 'e61f':'38', '667e':'39',
            '7f43':'40', '6449':'41', '117a':'42', '5966':'43',
            '4d35':'44', '6fb1':'45','ea5d':'46', 'f23f':'47',
            '4960':'48',
            }

def print_graph():
    graph = pydot.Dot(graph_type='graph')
    

    for node in nodes:
        with open('normal-rpl-tree/mote{}.txt'.format(node), 'r') as f:
            lines = f.readlines()
            max_line = len(lines)
            v = str(node)
            u = lines[max_line-1].split(':')[1] #edita aqui para mudar o instantes da arvore
            u = u.split('\n')[0]
            u = motes_ip[u]
        
            edge = pydot.Edge(u, v)
            graph.add_edge(edge)

            graph.write_png('rpl_tree.png'.format())
  





def print_graph1(file):
    graph = pydot.Dot(graph_type='graph')
    try:
        f = open(file, "r")
        
        for line in f.readlines()[1:]:
            u,v =  line.split("=")
            edge = pydot.Edge(v[:len(v)-1], u[1:])
            graph.add_edge(edge)

        graph.write_png('{}.png'.format(file))
        print "{} was successful".format(file)

    except:
        print "{} does not exist".format(file)

def get_tree_files():

  for node in nodes:
    with open('normal-rpl-v3/mote{}.txt'.format(node), 'r') as f:
      for line in f.readlines():
        data = line.split() 
        if data[0] == '#2':
            with open('normal-rpl-tree/mote{}.txt'.format(node), 'a') as f1:
                f1.write('{}\n'.format(data[2]));
                f1.close()


def main():
    print_graph()


if __name__ == '__main__':
    main()