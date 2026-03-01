import networkx as nx


# this was neccessary to change the undirected graph to a graph with bidirectional edges
# to calc travel distance and for path finding algorithms

# the cleaned up data with latitude and longitude
G = nx.read_gml("../data/output_updated.gml")

# create mulit-di graph (bidrectional links for travel)
MDG = nx.MultiDiGraph()

# re-add all edges and nodes that are existing to new graph
MDG.add_nodes_from(G.nodes(data=True))
for u, v, data in G.edges(data=True):
    MDG.add_edge(u, v, **data)
    MDG.add_edge(v, u, **data)


nx.write_gml(MDG, "../data/multi-di-graph.gml")
