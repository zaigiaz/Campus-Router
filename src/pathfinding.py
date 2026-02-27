import networkx as nx 

# TODO: use the neighbors() function to get all neighbors in a graph
#       for pathfinding purposes?

# TODO: Djistrikas and A* search, where Euclidean between two lat,lon points is our hueristic
#       and haversine is what we used to calculate distance between points as our edge wieghts

# TODO: implement or get stacks and queues for the algorithms

# Djistrikas Algorithm Reference
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
 
stack = [] # .append, pop()
queue = [] # .append, .pop(0)

G = nx.read_gml("../data/final_graph.gml")

# TODO: complete helper functions for this algorithm
def Djistrikas_Algorithm():

    # Priority Queue
    # Min Distance choosen first

    pq = []
    dist = [False for _ in range(len(G.nodes()))]
    prev = [False for _ in range(len(G.nodes()))]
    
    for i,v in enumerate(G.nodes()):        
        pq.append((i, v))

    u = distance_to_target(G.nodes['1'], G.nodes['32'])
    print(pq)

    while pq:
        pq.pop(0)


      # TODO: translate and complete this
      #   for each edge (u, v) in Graph:
      #       alt ← dist[u] + Graph.Distance(u,v)
      #         if alt < dist[v]:
      #             dist[v] ← alt
      #             prev[v] ← u


  # return dist[], prev[]

        
# distance to the goal node from current node (calculated using Euclidean Distance)
# uses basic 3d projection of euclidean distance for distance estimate on earths surface
def distance_to_target(src, target):
    
    lat1 = src['latitude']  
    lon1 = src['longitude']

    lat2 = target['latitude']
    lon2 = target['longitude']

    
    print(lat1, lon1, lat2, lon2)

    # print(src, target)




Djistrikas_Algorithm()
print("Nodes: ", len(G.nodes()))
print("Edges: ", len(G.edges()))


