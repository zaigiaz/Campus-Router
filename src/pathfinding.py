import networkx as nx 
import math
import sys
import heapq

# visualize graph file for nice figures
import visualize_graph as vz


# TODO: for today:
# DO Experiments 1 and 2
# Finish Presentation Slides


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


# runs Djistirkas multiple times to take into account multiple goal nodes.
# takes a list called building which has all the building entrances for given building
def Djistrika_Multiple_Answer(start_node, Building):

    pq = []

    for end_node in range(len(Building)):        
        path, dist = Djistrikas_Algorithm(start_node, Building[end_node])
    
        if path == None or dist == math.inf:
            print(f'cannot reach {end_node} from {start_node}')
            heapq.heappush(pq, (math.inf, None))
        
        heapq.heappush(pq, (dist, path))

    dist, path = heapq.heappop(pq)
    return (dist, path)
        
    
# Floyd-Warshall Algorithm
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



# TODO finish this function
# check multiple building entrances in Building List and then compute shortest path out of all.
def Floyd_check_multiple(src, Building):

    pq = []

    dist, nxt, idx, rev_idx = Floyd_Warshall()

    for node in Building:
        distance = dist[idx[node]]
        heapq.heappush(pq, (dist, node))

    # pop off priority queue and get node with shortest distance
    min_dist = heapq.heappop(pq)
    
    # name of our min distance target node
    target_node = min_dist[1]

    # format the final answer
    path, dist = Floyd_Answer(src, target_node, dist, nxt, idx)

    return path, dist
    

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

    elif travel_type == "biking":
        sec_time = travel_distance / bike_travel

    elif travel_type == "jog":
        sec_time = travel_distance / jog_speed

    else:
        print("travel_type is not supported\nsupported types:\nwalking\nbiking\njog")

    time = sec_time
    
    if sec_time > 60:
        min_time = sec_time / 60
        time = min_time

    return time


# main function for testing and other stuff
def main():
    src = '1'
    target = 'Lovejoy_Front'

    Building = ['Lovejoy_Front', '9', '32', 'Peck_Front']

    # algo showcase
    print("Nodes: ", len(G.nodes()))
    print("Edges: ", len(G.edges()))

    # single source to target path Djistrika Implementation
    path, distance = Djistrikas_Algorithm(src, target)
    print(path, distance)
    
    # call Djistrika multiple times to get answer
    ans = Djistrika_Multiple_Answer('Art_sideA', Building)
    print("shortest path out of all entrances", ans)

    # example call to get basic floyd warshall table
    dist, nxt, idx, rev_idx = Floyd_Warshall()

    # checks every node in Building against the table in Warshall to find shortest path to building
    dist, path = Floyd_check_multiple('1', Building)
    print(dist, path)

    vz.draw_graph(G)
    vz.highlight_edges(ans[1])

    # path, dist = Floyd_Answer(src, target, dist, nxt, idx)

    print(convert_to_time(ans[0], "walking"), "minute travel time")


if __name__  == "__main__": main()


