# Overview

SIUE Campus-Router using Python, NetworkX, and Matplotlib.

# Methodology

I hand picked out nodes for each junction point in the university, and then added more nodes to try and ensure that there would be straight line distances. 
for each edge to simplify calculations and to make the graph more dense. The weight of the edges are calculated using haversine distance, which calculates the length
<br>
of an arc between the two nodes because Earth is a sphere and we needed arcs and not 2D Euclidean Points. Then I implemented Floyd-Warshall and Djistrikas Algorithm
to find the path of an arc (u,v). After that I added two functions to take a list of nodes that had building entrances, and run the two algorithms to account for 
<br>
building entrances. This is because buildings can have multiple entrances, meaning the algorithms need to account for N amount of arcs to a building instead of one.
<br>
An image of the path that is found with the algorithms is traced in img/matplot.png, here is an example:
<br>
[img_path](/img/matplot.png)
<br>
# Used Packages

- NetworkX
- Matplotlib
