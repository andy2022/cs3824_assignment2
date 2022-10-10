## Code for Louvain algorithm
import networkx as nx
from random import shuffle

def moveNodes(G, P, H, H_change):
    '''
    Phase 1 of Louvain algorithm. For every node u and every neighbor v of u,
    evaluate change in q when u removed from its community and added to v's community.
    Ends with u moved to the neighhboring community for which q change is largest.
    G: networkx graph
    P: partition as communities object
    H: modularity or CPM as function handle
    H_change: change in H as function handle
    '''
    # Calculate H for current partition - kickstart loop by setting H(P) > H
    Hp = H(P)
    H_old = Hp-1

    while Hp > H_old:
        H_old = Hp # Save current value of H
        # For each node in node_table (gets access to partitions)
        for v in shuffle(P.node_table.keys()):

            pass

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