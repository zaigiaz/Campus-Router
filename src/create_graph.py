import networkx as nx


# list of every building on campus that a student would want to use
building_list = ["Peck_Hall", "Morris_Center", "LoveJoy_Library", "Science_West", "Science_East", 
                "Founders_Hall", "Katherine_Dunham_Hall", "Rendleman_Hall", "Alumni_Hall", "Fitness_Center",
                 "SIUE_Pharmacy", "Engineering_Building", "Art_and_Design_East", "Bluff_Hall", "Evergreen_Residence"]


# list of every node in our graph for traversal purposes
# TODO: finish list of nodes that we need for our graph
node_list = ["M_centerA", "M_centerB", "M_centerC", "PLotA", "PlotB", "PlotC"]

# TODO: add edges between all nodes
edge_list = [{"Peck_Hall", "Morris_Center"}, {"Katherine_Dunham_Hall", "Engineering_Building"}, {"Peck_Hall", "Fitness_Center"}, 
             {"Rendleman_Hall", "SIUE_Pharmacy"}, {"Art_and_Design_East", "Science_West"}]


def create_graph():
    G = nx.Graph()

    G.add_nodes_from(building_list)
    G.add_edges_from(edge_list)

    return G

def main():    
    graph = create_graph()
    
    nx.write_gexf(graph, "../img/graph.gexf")
    nx.write_gml(graph, "../img/graph.gml")



print("reached end of program")




