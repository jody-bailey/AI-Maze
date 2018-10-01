# Jody Bailey
# 09/21/2018
# Intro to Algorithms
# This class is used to create my Nodes for the tree.

# NodeMixin from anytree is used just for keeping track of
# the parent node and help with the path
from anytree import NodeMixin


class Node(NodeMixin):

    # Variables for my Nodes
    location = ''
    data = ''
    traveledPath = []

    # Constructor
    def __init__(self, location, data, path, parent=None):
        super(Node, self).__init__()
        self.location = location
        self.data = data
        self.traveledPath = path
        self.parent = parent
