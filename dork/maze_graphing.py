import networkx as nx
import matplotlib.pyplot as plt
import yaml

G = nx.Graph()
nx.write_yaml(G, 'maze.yml')
G = nx.read_yaml('maze.yml')

G.add_edge("Empty Room", "Kitchen")
G.add_edge("Office", "Boss")
G.add_edge("Boss", "Empty Room")
G.add_edge("Kitchen", "Office")
G.add_edge("Boss", "Exit")

elarge = [(u, v) for (u, v, d) in G.edges(data=True)]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx_edges(G, pos, edgelist=elarge,width=6)

nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

plt.show()