import math
import networkx as nx

# haversine formula from https://en.wikipedia.org/wiki/Haversine_formula
# implementation here: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

G = nx.read_gml("../data/output_updated.gml")

def haversine_feet(lat1, lon1, lat2, lon2):
    R = 3959  # Earth's radius in miles
    
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c * 5280

# Add distances to edges
for u, v in G.edges():
    lat1, lon1 = G.nodes[u]['x'], G.nodes[u]['y']
    lat2, lon2 = G.nodes[v]['x'], G.nodes[v]['y']
    distance = haversine_feet(lat1, lon1, lat2, lon2)    
    G[u][v]['distance'] = distance


nx.write_gml(G, "../data/haversine.gml")
