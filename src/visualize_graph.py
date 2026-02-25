import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml("../data/haversine.gml")


# nx.draw_networkx(G, arrows=None)
# pos = nx.forceatlas2_layout(G, scaling_ratio=5, gravity=5.0)
pos = nx.kamada_kawai_layout(G)

plt.figure(3,figsize=(13,13), dpi=100)
nx.draw_networkx(G,pos,node_size=170,font_size=8,node_color='red') 

plt.savefig("../data/matplot.png")

