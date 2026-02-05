import networkx as nx


# list of every building on campus that a student would want to use
building_list = ["Peck_Hall", "Morris_Center", "LoveJoy_Library", "Science_West", "Science_East", 
                "Founders_Hall", "Katherine_Dunham_Hall", "Rendleman_Hall", "Alumni_Hall", "Fitness_Center",
                 "SIUE_Pharmacy", "Engineering_Building", "Art_and_Design_East", "Bluff_Hall", "Evergreen_Residence"]


# list of every node in our graph for traversal purposes
# TODO: finish list of nodes that we need for our graph

# TODO: add edges between all nodes
edge_list = [{"Peck_Hall", "Morris_Center"}, {"Katherine_Dunham_Hall", "Engineering_Building"}, {"Peck_Hall", "Fitness_Center"}, 
             {"Rendleman_Hall", "SIUE_Pharmacy"}, {"Art_and_Design_East", "Science_West"}]


# main list of nodes split off into different categories to make my work faster for creating dataset

# main square of university just the 11 in the circle, for now
main_square = ["M_centerA", "M_centerB", "M_centerC", "M_centerD","M_centerE","M_centerF","M_centerG","M_centerH","M_centerI","M_centerJ",
               "Lovejoy_Front", "Morris_Front", "Morris_SideA", "Morris_SideB", "Morris_Back"] 

dunham = ["Dunham_Front", "Dunham_Back"]

peck_hall = ["Peck_Front", "Peck_Back", "Peck_SideA"]

# all nodes around Engineering and Art Buildings
Engineering_Art = ["Engineering_EntranceFront", "Engineering_EntranceBack", "Engineerng_side", "Art_front", "Art_sideA", "Art_sideB"]

Science = ["Science_East_Main", "Science_West_Main", "Science_East_SideA", "Science_East_SideB", "Science_East_Back"]

Theatre = ["Theatre_Front", "Theatre_Back", "Theatre_Side"]

# All nodes around Founder and Alumni
Founder_Alumni = []

# All nodes around Parking Lots 4 to 10
P4_P10 =  []

# all nodes around the University Drive Circle
Uni_Drive =  []

# all nodes around Parking Lot A and the Vandabelene Center
PA_VCenter =  []

# all nodes Science East and West

# all nodes behind morris and dunham hall
Morris_back = []

# misc
extras = []

def create_graph():
    G = nx.Graph()

    G.add_nodes_from(main_square)
    G.add_nodes_from(dunham)
    G.add_nodes_from(Science)
    G.add_nodes_from(peck_hall)
    G.add_nodes_from(Engineering_Art)
    G.add_nodes_from(Theatre)

    # G.add_edges_from(edge_list)

    return G

def main():    
    graph = create_graph()
    
    nx.write_gexf(graph, "../img/graph.gexf")
    nx.write_gml(graph, "../img/graph.gml")



print("reached end of program")




