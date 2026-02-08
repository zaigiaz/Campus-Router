import networkx as nx

g = nx.read_gexf("../img/campus.gexf")

print(len(g.nodes()))
print(len(g.edges()))

G = nx.to_undirected(g)

nx.write_gexf(G, "../img/undirected.gexf")
