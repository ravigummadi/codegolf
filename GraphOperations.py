__author__ = 'gummadi'
from collections import deque

class GraphOperations:

    def __init__(self, adjacency_list):
        i = 0
        self.adjacency_list = adjacency_list
        self.processed = list(range(len(adjacency_list)))
        self.discovered = list(range(len(adjacency_list)))
        self.parent = list(range(len(adjacency_list)))
        for i in range(len(adjacency_list)):
            self.processed[i] = self.discovered[i]= False
            self.parent[i] = -1
        return

    def bfs(self, start):
        q = deque()
        v = 0
        y = 0
        q.append(0)
        self.discovered[start] = True
        while len(q) != 0:
            v = q.popleft()
            self.process_vertex_early(v)
            self.processed[v] = True
            p = self.adjacency_list[v]
            for ad_v in self.adjacency_list[v]:
                if not self.processed[ad_v]:
                    self.process_edge(v, ad_v)
                if not self.discovered[ad_v]:
                    q.append(ad_v)
                    self.discovered[ad_v] = True
                    self.parent[ad_v] = v
            self.process_vertex_late(v)
        print self.parent
        return


    def process_vertex_late(self,v):
        print 'Processed Vertex Late: %d' % v
        return

    def process_vertex_early(self,v):
        print 'Processed Vertex Early: %d' % v
        return

    def process_edge(self,v,ad_v):
        print 'Processed Edge: %d,%d' %(v, ad_v)
        return