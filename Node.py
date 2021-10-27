class Node:

    # Future planning: at some point, we might want each node to be able to tell us where it lies in the overall structure of the multi-dimensional array containing these "grid points". Instead of polluting the class with an attribute for each coordinate (read: index of element in array), we can do this with a tuple (think vector). The Node should never assume any behaviour of the spacetime or geometry, so by default, we will initialize with a single dimensional tuple.
    __latticeCoordinates = tuple((0,))

    def __init__(self, positionInLatticework):
        self.__latticeCoordinates = positionInLatticework
        print("Node created with lattice coordinates:", self.__latticeCoordinates)