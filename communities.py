## Implementation of data structure for storing community information
import networkx as nx
import networkx.algorithms.community
from math import comb

class communities:

    # Constructor
    def __init__(self, input_graph):
        '''
        input_graph: networkx graph to manipulate
        '''
        self.node_table = {} # dict for storing all nodes w/ community id
        self.com_table = {0: []} # dict for storing communities with list of member nodes
        self.graph = input_graph

        # Iterate through all nodes, add all to single community
        for node in self.graph.nodes():
            self.node_table[node] = 0
            self.com_table[0].append(node)

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

    def modularity(self, gamma):
        '''
        Function for calculating modularity. Uses Leiden definition of modularity.
        gamma: resolution parameter (>0)
        '''
        if not gamma>0:
            raise Exception("Gamma must be greater than 0")

        m = self.graph.number_of_edges() # m = Total number of edges in graph

        com_sum = 0 # Initialize sum for formula
        for n_list in self.com_table.values():
            ec = self.graph.subgraph(n_list).number_of_edges() # Edges in community
            Kc = sum([self.graph.degree[n] for n in n_list]) # Total degree of community
            com_sum = com_sum + (ec - gamma*((Kc**2)/(2*m))) # Update sum

        return com_sum / (2*m)


        ''' Pseudocode
        sum = 0 # Initialize sum
        # Double for-loop to look at every possible pair of nodes
        for each node u in graph:
            for each node v in graph:
                # Only evaluate sum when delta = 1 (u,v in same community)
                if com_id(u) == com_id(v):
                    delta = 1


        if com_id(u) == com_id(v):
            delta = 1
        '''

    def mod_change(self):
        '''
        Function for calculating change in modularity when node moved from one
        community to another. D
        '''

        pass

    def CPM(self, gamma):
        '''
        Function for calculating CPM value.
        com: id of community to calculate modularity
        gamma: resolution parameter
        '''
        if not gamma>0:
            raise Exception("Gamma must be greater than 0")

        sum = 0 # Initialize sum
        for n_list in self.com_table.values():
            ec = self.graph.subgraph(n_list).number_of_edges() # Edges in community
            nc = len(n_list) # Number of nodes in this community
            sum = sum + (ec - gamma*comb(nc, 2))

        return sum

    def CPM_change(self):
        '''
        Function for calculating change in CPM value when node is moved from one
        community to another.
        '''
        pass

    def moveNode(self, node):
        '''
        Function for performing actual node move. Moves node from its current community
        to another community specified
        '''
        pass
