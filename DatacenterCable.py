__author__ = 'gummadi'
from GraphOperations import GraphOperations

def convert_to_edge_matrix(sample_array, edge_matrix):
    """
    Takes an array of data centers and converts it to
    adjacency matrix
    """
    print '%d' % sample_array[0][0]
    for i, v in enumerate(sample_array):
        for j in range(len(v)):
            set_edges(edge_matrix, sample_array, i, j)
    return

def set_edges(edge_matrix, sample_array, i, j):
    """
    Given an edge_matrix and the input array, sets the edges
    based on the given set of rules
    """
    width = len(sample_array[0])
    height = len(sample_array);
    vertex_num = width * i + j
    if i-1 >=0:
        up_vertex = width * (i-1) + j
        if sample_array[i][j] == sample_array[i-1][j] == 0:
            edge_matrix[vertex_num][up_vertex] = 1
            edge_matrix[up_vertex][vertex_num] = 1
    if i+1 < height:
        down_vertex = width * (i+1) + j
        if sample_array[i][j] == sample_array[i+1][j] == 0:
            edge_matrix[vertex_num][down_vertex] = 1
            edge_matrix[down_vertex][vertex_num] = 1
    if j-1 >= 0:
        left_vertex = width * i + (j-1)
        if sample_array[i][j] == sample_array[i][j-1] == 0:
            edge_matrix[vertex_num][left_vertex] = 1
            edge_matrix[left_vertex][vertex_num] = 1
    if j+1 < width:
        right_vertex = width * i + (j+1)
        if sample_array[i][j] == sample_array[i][j+1] == 0:
            edge_matrix[vertex_num][right_vertex] = 1
            edge_matrix[right_vertex][vertex_num] = 1
    return

def init_edge_matrix(edge_matrix, length):
    """
    Initializes the edge matrix. Initializing a multi-dimensional
    array in python is a pain.
    """
    new = []
    for i in range (0, length):
        for j in range (0, length):
            new.append(0)
        edge_matrix.append(new)
        new = []
    return

def convert_to_adjacency_list(edge_matrix):
    """
    Converts the edge matrix to adjacency list representation
    """
    adjacency_list = []
    new = []
    for row in edge_matrix:
        for i,v in enumerate(row):
            if v == 1:
                new.append(i)
        adjacency_list.append(new)
        new = []
    return adjacency_list


## ---------------------------------------------------
# Main script starts here
## ---------------------------------------------------

sample_array = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,1]
];
edge_matrix = [];
matrix_len = len(sample_array[0])*len(sample_array);
init_edge_matrix(edge_matrix, matrix_len);
convert_to_edge_matrix(sample_array, edge_matrix);
adjacency_list = convert_to_adjacency_list(edge_matrix);
graph_ops = GraphOperations(adjacency_list);
#graph_ops.bfs(0);
#graph_ops.dfs(0,10);
print graph_ops.find_all_paths(0,10);

print edge_matrix
print adjacency_list;







