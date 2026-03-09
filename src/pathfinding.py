import networkx as nx 
# from memory_profiler import profile
# import timeit
import math
import sys
import heapq

# visualize graph file for nice figures
import visualize_graph as vz
import buildings_list as bl

# TODO:
# DO Experiments 1 and 2
# Finish Presentation Slides and Paper

# Djistrikas Algorithnm Reference
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode

# Floyd Warshall Reference
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

G = nx.read_gml("../data/final_graph.gml")

# Djistrikas Algorithm
#      Input: u, v
#      where u is the start node and v is the goal node
# 
#      Output: path, distance
#      returns the path to given goal node and the total sum distance
#
# @profile
def djistrikas_algorithm(G, u, v):

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


# Djistrikas Algorithm with Multiple Nodes
# runs Djistrikas in a loop and inserts all the nodes in a priority queue
#
# Input: start_node, Building
#        Name of node and list of all building entrance nodes
# 
# Output: (dist, path) 
#         distance to smallest node, and path reconstructed to it
# @profile
def djistrika_multiple_nodes(start_node, Building):

    pq = []

    for end_node in range(len(Building)):        
        path, dist = djistrikas_algorithm(G, start_node, Building[end_node])
    
        if path == None or dist == math.inf:
            print(f'cannot reach {end_node} from {start_node}')
            heapq.heappush(pq, (math.inf, None))
        
        heapq.heappush(pq, (dist, path))

    path, dist = heapq.heappop(pq)
    return (dist, path)
        
    
# floyd-warshall algorithm
#
# Input: None
# 
# Output: matrix of distances from nodes i->j, table of prev nodes i->j
#         two dicts of indexed node names, both forward and reverse 
#
# @profile
def floyd_warshall(G):

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




# floyd_check_multiple
# 
# Takes the table from the Floyd Warshall Algorithm and checks all the nodes in it matching 
# Building list and returning the node with minimium distance in that list, calls Floyd_Answer() to format
# 
# Inputs: src, Building
#         start_node, and list of Building Entrance nodes
#
# Outputs: path, dist
#          Path to goal node, distance to it
#
# @profile
def floyd_check_multiple(src, Building):

    pq = []

    dist, nxt, idx, rev_idx = floyd_warshall(G)

    for node in Building:
        distance = dist[idx[src]][idx[node]]
        heapq.heappush(pq, (dist, node))

    # pop off priority queue and get node with shortest distance
    min_dist = heapq.heappop(pq)
    
    # name of our min distance target node
    target_node = min_dist[1]

    # format the final answer
    path, dist = floyd_answer(src, target_node, dist, nxt, idx)

    return path, dist
    

# floyd_answer
# 
# get table from Floyd_Algo and then reconstruct path for given two nodes you want
# 
# Inputs: src, target, dist, nxt, idx
#         source node, target node, list of distances, list of nodes, index of each node
#
# Outputs: path, dist[i][j]
#
def floyd_answer(src, target, dist, nxt, idx):

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


# convert_to_time
#
# takes distance traveled and divides by common measurements of average speed ft/s
# of various travel types like walking, biking, or jogging
# 
# inputs: travel distance, travel_type
#
# outputs: time taken to travel
# 
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


# algo_report
#
# Calls all the algorithms and generates a report and comparison between the two
# 
# Inputs: src, target, Buildings
# 
# Outputs: final report and comparison of algorithms presented
#
def algo_report(src, target, Buildings):

    node_list = []


    # algo showcase
    print("Nodes: ", len(G.nodes()))
    print("Edges: ", len(G.edges()))

    avg_degree = sum(dict(G.degree()).values()) / len(G.nodes())
    print("Degree: ", avg_degree)
    
    
    print("\n")

    # Single Answer (From u to v) 
    if Buildings == None and target:
        path, distance = djistrikas_algorithm(G, src, target)
        print(f'Path taken by djistrikas algorithm {path}\ndistance_traveled: {distance}\n\n')
        print(convert_to_time(distance, "walking"), "minute travel time")

        dist, nxt, idx, rev_idx = floyd_warshall(G)
        path, dist = floyd_answer(src, target, dist, nxt, idx)
    
        print("Floyd-Warshall")
        print(f'Distance: {dist}\nPath to goal node:\n{path}')
        print(convert_to_time(dist, "walking"), "minute travel time")

        node_list = path


    # multiple answers (Building List)
    elif Buildings and target == None:
        # call Djistrika multiple times to get answer
        ans = djistrika_multiple_nodes(src, Buildings)
        print("djistrika: shortest path out of all entrances", ans[1])
        print("djistrika: distance", ans[0])
        print(convert_to_time(ans[0], "walking"), "minute travel time\n")

        node_list = ans[1]

        print("Floyd-Warshall")
        dist, path = floyd_check_multiple(src, Buildings)
        print(f'Distance: {path}\nPath_to_goal_node: {dist}')
        print(convert_to_time(distance, "walking"), "minute travel time\n")

    else:
        print("something went wrong")
        sys.exit(1)

    
    print("\nDrawing Graph -----")
    vz.draw_graph(G)
    vz.highlight_edges(node_list)
    print("Finished!")



# example code
# Building = ['64', '62', 'Pallative Care', 'Peck_Back']
# algo_report('1', '4', None)
