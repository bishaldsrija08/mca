import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("Adjacency List:")

for vertex in graph:
    print(vertex, ":", graph[vertex])

G = nx.Graph()

for vertex in graph:
    for neighbor in graph[vertex]:
        G.add_edge(vertex, neighbor)

nx.draw(
    G,
    with_labels=True,
    node_size=2000
)

plt.title("Graph using Adjacency List")
plt.show()