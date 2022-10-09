## Implementation of data structure for storing community information
import networkx as nx
import networkx.algorithms.community

class communities:

    # Constructor
    def __init__(self, input_graph):
        self.node_table = {} # dict for storing nodes w/ community id
        self.com_table = {} # dict for storing communities with list of member nodes

    def com_id(self, node):
        '''
        Given node u, quickly determine the id for the community containing u.
        node: Name of node as string
        '''
        return self.node_table[node]

    def node_set(self, id):
        '''
        Given community id, return list of nodes in that community.
        TODO: Potentially change return type
        id: Community id number as int
        '''
        return self.com_table[id]
