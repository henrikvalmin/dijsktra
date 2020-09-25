import pandas as pd
from tabulate import tabulate
from node import node
from dijkstra import dijsktra as d

def connect(node1, node2, cost):
    """Creates a connection between two nodes
    with a specified cost."""
    node1.add(node2.name, cost)
    node2.add(node1.name, cost)

def initialize_nodes():
    """Initializes the nodes and their connections."""

    # Below is an example (P.3 in chapter 5 from Computer Networking - 
    # a top down approach by Kuruse & Ross).

    x = node('x')
    y = node('y')
    z = node('z')
    w = node('w')
    u = node('u')
    v = node('v')
    t = node('t')

    initial_nodes = [x, y, z, w, u, v, t]
    initial_nodes.sort(key=lambda x: x.name)

    connect(x, z, 8)
    connect(x, y, 6)
    connect(x, v, 3)
    connect(x, w, 6)

    connect(y, z, 12)
    connect(y, t, 7)
    connect(y, v, 8)

    connect(v, w, 4)
    connect(v, u, 3)
    connect(v, t, 4)

    connect(u, w, 3)
    connect(u, t, 2)
    return initial_nodes

def main():
    nodes = initialize_nodes()
    table = d.dijsktra_solve(nodes, nodes[4]) # alphabetic index of node
    print('\n', tabulate(table, headers='keys', tablefmt='psql'), '\n', sep='')


if __name__ == "__main__":
    main()