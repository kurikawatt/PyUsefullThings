#coding: utf-8

class Graph:

    def __init__(self, adjacency:list[list[bool]]=[]):
        
        self.__edges = dict()
        self.__node_label = dict()

        if adjacency:
            for i, node in enumerate(adjacency):
                self.__edges[i] = {}
                self.__node_label[i] = str(i) 
                for j, connected in enumerate(node):
                    if connected:
                        self.__edges[i][j] = True
                    else:
                        self.__edges[i][j] = False