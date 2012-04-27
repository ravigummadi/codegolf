__author__ = 'gummadi'

def convert_to_edge_matrix(sample_array, edge_matrix):
    print '%d' % sample_array[0][0]
    for i, v in enumerate(sample_array):
        for j in range(len(v)):
            set_edges(edge_matrix, sample_array, i, j)
    return

def set_edges(edge_matrix, sample_array, i, j):
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
    new = []
    for i in range (0, length):
        for j in range (0, length):
            new.append(0)
        edge_matrix.append(new)
        new = []
    return

sample_array = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,1]
];
edge_matrix = [];
init_edge_matrix(edge_matrix, 12);
convert_to_edge_matrix(sample_array, edge_matrix);
print edge_matrix







