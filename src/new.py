import networkx as nx
import osmnx as osm
from shapely.geometry import Point

# G = osm.graph_from_xml("../img/pruned.osm")
# osm.save_graphml(G, "pruned.graphml")
# print("saved pruned.graphml")


G = ox.load_graphml("pruned_with_lengths.graphml")
# replace with your entrance source; example CSV columns: id,lat,lon
entr = pd.read_csv("entrances.csv")
for _,r in entr.iterrows():
    nid = f"entr_{int(r.id)}"
    G.add_node(nid, y=r.lat, x=r.lon, entrance=True)
    # snap to nearest graph node
    nearest = ox.distance.nearest_nodes(G, X=r.lon, Y=r.lat)
    dist = ox.distance.great_circle_vec(r.lat, r.lon, G.nodes[nearest]['y'], G.nodes[nearest]['x'])
    # connect both ways
    G.add_edge(nid, nearest, length=dist)
    G.add_edge(nearest, nid, length=dist)
ox.save_graphml(G, "pruned_with_entrances.graphml")
print("saved pruned_with_entrances.graphml")
