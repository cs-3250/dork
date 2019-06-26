import networkx as nx

G.add_edge('Empty Room', 'Kitchen', direction='ne')
G.add_edge('Office', 'Boss', direction='ne')
G.add_edge('Boss', 'Kitchen', direction='se')
G.add_edge('Empty Room', 'Office', direction='nw')
G.add_edge('Boss', 'Exit', direction='n')
print("1")
nx.write_yaml(G, 'snarf.yml')
print("2")


G.add_edge('A', 'B', direction='w')
G.add_edge('B', 'C', direction='n')
print("1")
nx.write_yaml(G, 'snarf.yml')
print("2")