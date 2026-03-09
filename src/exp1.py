import networkx as nx
import pathfinding as pf
import buildings_list as bl
import random

# explores our graph and measures the percentage of buildings crossed on a random path

G = nx.read_gml("../data/final_graph.gml")
nodes = list(G.nodes())

in_morris = 0
out_morris = 0
total_paths = 0

for n in range(10000):
    node1, node2 = random.sample(nodes, 2)
    ans = pf.djistrikas_algorithm(node1, node2)

    if ans is None:
        continue
    
    total_paths += 1

    morris_count = sum(1 for node in ans[0] if node in bl.Art)
    in_morris += morris_count
    out_morris += len(ans[0]) - morris_count

print(f"Total paths analyzed: {total_paths}")
print(f"Morris Center nodes visited: {in_morris}")
print(f"Non-Morris nodes visited: {out_morris}")
print(f"% Morris nodes: {100*in_morris/(in_morris+out_morris):.1f}%")
