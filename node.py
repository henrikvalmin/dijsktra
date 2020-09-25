class node:
    """
    Contains a single node in the network.
    The attribute neighbors is a dictionary of neighbor names
    as keys, the costs of the path as value. 
    """
    def __init__(self, name):
        self.neighbors = {}
        self.name = name

    def add(self, name, cost):
        self.neighbors[name] = cost