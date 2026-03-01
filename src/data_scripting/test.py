import networkx as nx

g = nx.read_graphml("../img/graph.graphml")



for n, data in g.nodes(data=True):
    print(n, data.get("label"))




