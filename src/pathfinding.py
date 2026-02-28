import networkx as nx 
import math
import sys
import heapq

# TODO: use the neighbors() function to get all neighbors in a graph
#       for pathfinding purposes?

# TODO: Djistrikas and A* search, where Euclidean between two lat,lon points is our hueristic
#       and haversine is what we used to calculate distance between points as our edge wieghts

# TODO: implement or get stacks and queues for the algorithms

# Djistrikas Algorithm Reference
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode

# for Euclidean Heuristic 
EARTH_RADIUS_FT = 20_902_900.0

G = nx.read_gml("../data/final_graph.gml")

def Djistrikas_Algorithm():

    # example case  testing
    start_node = '1'
    end_node = '33'
    
    dist = {node: math.inf for node in G.nodes()}
    dist[start_node] = 0

    prev = {}
    pq = [(0, start_node)] 
    visited = set()
    
    while pq:
        cur_dist, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        if u == end_node:
            break
            
        for v in G.neighbors(u):
            weight = G[u][v].get('distance', 1.0)
            alt = cur_dist + weight
            
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))
    

    if end_node not in prev and end_node != start_node:
        return None
    
    path = []
    cur = end_node

    while cur != start_node:
        path.append(cur)
        cur = prev[cur]
    path.append(start_node)
    path.reverse()

    return path, dist[end_node]

        
# distance to the goal node from current node (calculated using Euclidean Distance)
# uses basic 3d projection of euclidean distance for distance estimate on earths surface
def Euclidean_Heuristic(src, target):
    
    lat1 = math.radians(src['latitude'])
    lon1 = math.radians(src['longitude'])
    lat2 = math.radians(target['latitude'])
    lon2 = math.radians(target['longitude'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    x = dlon * math.cos(0.5 * (lat1 + lat2))
    y = dlat

    return EARTH_RADIUS_FT * math.hypot(x,y)




path, distance = Djistrikas_Algorithm()

print(path, distance)
print("Nodes: ", len(G.nodes()))
print("Edges: ", len(G.edges()))



