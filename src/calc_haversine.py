import networkx as nx


G = nx.read_gml("../data/output_updated.gml")


for n in list(G.nodes()):

    lat = G.nodes[n]["x"]
    lon = G.nodes[n]["y"]

    print(G.nodes[n]["x"])
    






