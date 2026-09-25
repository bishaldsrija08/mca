import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

vertices = ['A', 'B', 'C', 'D']

matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
])

print("Adjacency Matrix:")
print(matrix)

G = nx.from_numpy_array(matrix)

mapping = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D'
}

G = nx.relabel_nodes(G, mapping)

nx.draw(
    G,
    with_labels=True,
    node_size=2000
)

plt.title("Graph using Adjacency Matrix")
plt.show()