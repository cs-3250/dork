import networkx as nx
import matplotlib.pyplot as plt
from networkx.utils import open_file
import yaml

G = nx.Graph()
G = nx.read_yaml('maze.yml')

#nx.write_yaml(G, 'maze.yml')

for line in nx.generate_adjlist(G):
    print(line)
exit(0)

elarge = [(u, v) for (u, v, d) in G.edges(data=True)]

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)

nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

plt.show()
