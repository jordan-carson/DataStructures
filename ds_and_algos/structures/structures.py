# class Stack


class Node:
    def __init__(self, value):
        self.edges = list()
        self.value = value


class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self, nodes=list(), edges=list()):
        self.nodes = nodes
        self.edges = edges