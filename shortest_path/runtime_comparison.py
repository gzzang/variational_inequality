# @Time    : 2020/2/24 20:14
# @Author  : gzzang
# @File    : runtime_comparison
# @Project : shortest_path

import igraph as ig
import networkx as nx
import time

edgelist_string = ['1 5 7 300',
                   '1 12 9 200',
                   '4 5 9 200',
                   '4 9 12 200',
                   '5 6 3 350',
                   '5 9 9 400',
                   '6 7 5 500',
                   '6 10 13 250',
                   '7 8 5 250',
                   '7 11 9 300',
                   '8 2 9 500',
                   '9 10 10 550',
                   '9 13 9 200',
                   '10 11 6 400',
                   '11 2 9 300',
                   '11 3 8 300',
                   '12 6 7 200',
                   '12 8 14 300',
                   '13 3 11 200']

g = nx.parse_edgelist(edgelist_string, nodetype=int, create_using=nx.DiGraph,
                      data=(('weight', int), ('capacity', int)))
nx.write_gml(g, path='nguyen_dupuis_gml_from_networkx')

n = 10 ** 5

g_nx = nx.read_gml(path='nguyen_dupuis_gml_from_networkx')
g_ig = ig.Graph.Read_GML('nguyen_dupuis_gml_from_networkx')
g_ig.vs['name'] = g_ig.vs['label']

start_nx = time.time()
for i in range(n):
    nx.shortest_path(g, 1, 2, weight='weight')
end_nx = time.time()
time_nx = end_nx - start_nx

start_ig = time.time()
for i in range(n):
    g_ig.get_shortest_paths('1', to='2', weights='weight')
end_ig = time.time()
time_ig = end_ig - start_ig

print(f'time_nx:{time_nx}')
print(f'time_ig:{time_ig}')
