import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml("../data/final_graph.gml")

# draw base graph
def draw_graph(G):
    pos = nx.kamada_kawai_layout(G)

    plt.figure(3,figsize=(13,13), dpi=100)    
    nx.draw_networkx(G,pos,node_size=170,font_size=8,node_color='red') 


# highlight the edges that were choosen from pathfinding.py
def highlight_edges(nodes):
    pos = nx.kamada_kawai_layout(G)

    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            edge = (nodes[i], nodes[j])
            if G.has_edge(*edge):  # Only highlight if edge exists
                nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='#00008b', width=4)

            plt.savefig("../img/matplot.png")

# save figure to data dir

