## Methods for reading input files and creating graph objects
import networkx as networkx

def read_txt(g, fname):
    '''
    Reads the specified edges text file and adds all edges to the specified graph.
    g: Graph to which edges will be added
    fname: Input file to read
    '''
    f = open(fname, "r")
    firstline = f.readline() # Read first line
    assert(firstline[:5] == "#tail") # Check that correct table is being read

    for line in f:
        arr = line.split()

        g.add_edge(arr[1], arr[0]) # Add edge from two nodes (undirected)

    # End of loop

    f.close()