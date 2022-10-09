## Code for Louvain algorithm
import networkx as nx

def moveNodes(g, p):
    '''
    Phase 1 of Louvain algorithm. For every node u and every neighbor v of u,
    evaluate change in q when u removed from its community and added to v's community.
    Ends with u moved to the neighhboring community for which q change is largest.
    g: networkx graph
    p: partition (community)
    '''
    pass

def Louvain(g, p):
    '''
    Repeatedly perform moveNodes function until quality no longer improves.
    Stops when relative change in quality between two consecutive iterations falls
    below threshold 10^-3.
    g: networkx graph
    p: partition (community)
    '''
    pass