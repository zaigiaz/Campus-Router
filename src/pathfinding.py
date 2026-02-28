import networkx as nx 
import math
import sys
import heapq

# TODO: CHeck this data for correctness
# 0.13732771944621822 M_centerB Lovejoy_Front
# 0.9791639734434642 Science_East_Back 65
# 0.7593135823466972 Alumni Founders_Back
# 0.005591479496646561 54 53

# Djistrikas Algorithm Reference
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode

# Floyd Warshall Reference
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

G = nx.read_gml("../data/final_graph.gml")

# TODO: make this consider multiple different goal nodes, and terminate after finding
#       the first goal node (considering multiple building entrances)
def Djistrikas_Algorithm(u, v):

    # example case  testing
    start_node = u
    end_node = v
    
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
        
        # end after we have found the goal node
        # TODO: make this a list of goal nodes, depending on building
        if u == end_node:
            break


        # check all of the neighbors
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


# Floyd-Warshall Algorithm
# TODO: return path and distance (helper function)
# TODO: return correct given src node name and target node name
def Floyd_Warshall():

    size = len(G.nodes())
    nodes = list(G.nodes())

    # create dict of node labels and indices to go through container
    idx = {node: i for i, node in enumerate(nodes)}
    rev_idx = {i: node for node, i in idx.items()}

    # 130 x 130 DP
    dist = [[math.inf for _ in range(size)] for _ in range(size)]

    # Table of nodes to go through on shortest path 
    nxt = [[None] * size for _ in range(size)]

    # distance to self is 0 in the DP table
    for v in range(size):
        dist[v][v] = 0
        nxt[v][v] = nodes[v]

    # add edge weights to DP_Table
    for u, v, data in G.edges(data=True):
        i, j = idx[u], idx[v]
        w = data.get("distance", 1)            

        # as this is an undirected graph we need to fill both forward and backward directions
        if w < dist[i][j]:
            dist[i][j] = w
            nxt[i][j] = v

        if w < dist[j][i]:
            dist[j][i] = w
            nxt[j][i] = u

    # Floyd Warshall loop (O(n^3) time complexity)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    return dist, nxt, idx, rev_idx



# get table from Floyd_Algo and then reconstruct path for given two nodes you want
def Floyd_Answer(src, target, dist, nxt, idx):

    if src not in idx or target not in idx:
        print("node no exist in idx: 1st")
        return None, math.inf

    i, j = idx[src], idx[target]

    if nxt[i][j] is None or math.isinf(dist[i][j]):
        print("no path between the two: 2nd")
        return None, math.inf

    path = [src]
    u = src

    while u != target:
        u = nxt[idx[u]][j]

        if u is None:
            print("node is none: third")
            return None, math.inf

        path.append(u)

    return path, dist[i][j]


# function to calculate travel distance in minutes
# based on walking type, etc
def convert_to_time(travel_distance, travel_type):

    # TODO: provide sources for these speeds
    foot_travel = 3.6
    bike_travel = 18
    jog_speed = 7.5
    

    if travel_type == "walking":
        sec_time = travel_distance / foot_travel

    if travel_type == "biking":
        sec_time = travel_distance / bike_travel

    if travel_type == "jog":
        sec_time = travel_distance / jog_speed

    else:
        print("travel_type is not supported\nsupported types:\nwalking\nbiking\njog")

    time = sec_time
    
    if sec_time > 60:
        min_time = sec_time / 60
        time = min_time

    return time


src = '1'
target = 'Lovejoy_Front'


# algo showcase
print("Nodes: ", len(G.nodes()))
print("Edges: ", len(G.edges()))

path, distance = Djistrikas_Algorithm(src, target)
print(path, distance)

dist, nxt, idx, rev_idx = Floyd_Warshall()

# print(idx)
path, dist = Floyd_Answer(src, target, dist, nxt, idx)
print(path, dist)

print(convert_to_time(dist, 'walking'))
