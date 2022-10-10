## Tests for various methods
import networkx as nx
from reading import read_txt
from communities import communities
import unittest

class tests(unittest.TestCase):

    def setUp(self):
        self.g = nx.Graph() # Create empty undirected graph
        read_txt(self.g, "sample.txt") # Read sample.txt, add to graph
        self.P = communities(self.g) # Create single community for graph

    def test_modularity(self):
        print(self.P.modularity(1))
        print(self.P.modularity(10))
        with self.assertRaises(Exception):
            print(self.P.modularity(-1))

    def test_CPM(self):
        print(self.P.CPM(1))
        print(self.P.CPM(10))
        with self.assertRaises(Exception):
            print(self.P.CPM(-1))

unittest.main()