# @Time    : 2020/2/24 17:19
# @Author  : gzzang
# @File    : main_igraph
# @Project : shortest_path

import igraph as ig

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
with open('nguyen_dupuis', mode='w') as f:
    f.write('\n'.join(edgelist_string))

g = ig.Graph(directed=True)

node_list = tuple([str(i) for i in range(1, 14)])
g.add_vertices(node_list)

with open('nguyen_dupuis', mode='r') as f:
    edge_list = []
    weight_list = []
    capacity_list = []
    for line in f.readlines():
        values = [int(string) for string in line.split()]
        edge_list.append((str(values[0]), str(values[1])))
        weight_list.append(values[2])
        capacity_list.append(values[3])

g.add_edges(edge_list)
g.es['weight'] = weight_list
g.es['capacity'] = capacity_list

g.write_gml('nguyen_dupuis_gml_from_igraph')
g.write_edgelist('nguyen_dupuis_edgelist_from_igraph')

print(g)
print('nodes')
print([(v.index, v.attributes()) for v in g.vs])
print('edges')
print([(e.tuple, e.attributes()) for e in g.es])

print('shortest_path_length (weighted):')
print(g.shortest_paths_dijkstra(source='1', target='2', weights='weight'))
print('all_shortest_paths (weighted):')
print('method 1 (node):')
for shortest_path in g.get_shortest_paths('1', to='2', weights='weight'):
    print([g.vs[node]['name'] for node in shortest_path])
    print([f'{(g.vs[i]["name"], g.vs[j]["name"])}: {g.es[g.get_eid(i, j)]["weight"]}' for i, j in
           zip(shortest_path[:-1], shortest_path[1:])])
print('method 2 (edge):')
for shortest_path in g.get_shortest_paths('1', to='2', weights='weight', output='epath'):
    print(shortest_path)
    print(
        [f'{(g.vs[edge.source]["name"], g.vs[edge.target]["name"])}: {edge["weight"]}' for edge in g.es[shortest_path]])

print('shortest_path_length:')
print(g.shortest_paths_dijkstra(source='1', target='2'))
print('all_shortest_paths:')
print('method 1 (node):')
for shortest_path in g.get_shortest_paths('1', to='2'):
    print([g.vs[node]['name'] for node in shortest_path])
    print([f'{(g.vs[i]["name"], g.vs[j]["name"])}: {g.es[g.get_eid(i, j)]["weight"]}' for i, j in
           zip(shortest_path[:-1], shortest_path[1:])])
print('method 2 (edge):')
for shortest_path in g.get_shortest_paths('1', to='2', output='epath'):
    print(shortest_path)
    print(
        [f'{(g.vs[edge.source]["name"], g.vs[edge.target]["name"])}: {edge["weight"]}' for edge in g.es[shortest_path]])

g.vs.find(name="1")['string'] = 'test_string'
g.es[g.get_eid('1', '5')]['weight'] = 4.5
print(g)

