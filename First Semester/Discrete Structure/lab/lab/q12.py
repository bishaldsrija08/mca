import networkx as nx
import matplotlib.pyplot as plt

A = [1, 2, 3]

R = {(1, 1), (1, 2), (2, 3), (3, 1)}

G = nx.DiGraph()

G.add_nodes_from(A)
G.add_edges_from(R)

nx.draw(
    G,
    with_labels=True,
    node_size=2000,
    arrows=True
)

plt.title("Digraph of Relation")
plt.show()