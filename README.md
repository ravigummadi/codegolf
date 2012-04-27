Cooling Data Centers
========

Here is the algorithm of the approach:
* Convert the matrix to a undirected graph
* The total number of nodes will be equal to the number of data centers (including everything)
* There is an edge between two nodes, if only they are allowed to be wired i.e up, below or on either sides.
* Now do a BFS (breadth first search) on the graph and get the list of parents
* Use the parent child relationship to find all the paths between A and B. 
* If there are any paths which equal to the total number of data centers owned by us, its a valid path.