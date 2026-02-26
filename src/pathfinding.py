import networkx as nx 


# TODO: use the neighbors() function to get all neighbors in a graph
#       for pathfinding purposes

# TODO: Djistrikas and A* search, where Euclidean between two lat,lon points is our hueristic
#       and haversine is what we used to calculate distance between points as our edge wieghts

# TODO: implement or get stacks and queues for the algorithms


stack = [] # .append, pop()
queue = [] # .append, .pop(0)

G = nx.read_gml("../data/haversine.gml")

F = G.to_undirected()

print(nx.is_weighted(F, weight='distance'))
