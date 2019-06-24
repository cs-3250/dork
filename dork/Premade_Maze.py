import networkx as nx
import matplotlib.pyplot as plt
import yaml_parser_Maze

G = nx.Graph()

G.add_node("Empty Room")
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge("Empty Room", 2)
G.add_edge(3, 4)
G.add_edge(4, "Empty Room")
G.add_edge(2, 3)
G.add_edge(4, 5)

print(nx.info(G))

nx.draw(G)
plt.show()