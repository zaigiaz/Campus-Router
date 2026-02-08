import networkx as nx

g = nx.read_gml("../img/finished_nodes.gml")

print(len(g.nodes()))
print(len(g.edges()))
