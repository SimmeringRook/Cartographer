#import numpy

from EuclideanGeometry import EuclideanGeometry
from Node import Node


class Latticework:

    def __init__(self, gridShape = tuple((4,4)), spacetime = EuclideanGeometry(2)):
        self._spacetime = spacetime
        #self._nodes = numpy.empty(gridShape, dtype=object)
        #self.__populate_Lattice()

    # def __populate_Lattice(self):
    #     # numpy.shape() returns a tuple describe the dimensions of the numpy array
    #     # We can asked for the 
    #     numberOfDimensions = len(numpy.shape(self._nodes))
    #     print("Number of Dimensions:", numberOfDimensions)

    #     for dimension in range(numberOfDimensions):
    #         print("Length of Dimension:", numpy.shape(self._nodes)[dimension])

    #     for x in range(numpy.shape(self._nodes)[numberOfDimensions - numberOfDimensions]):
    #         for y in range(numpy.shape(self._nodes)[numberOfDimensions - numberOfDimensions + 1]):
    #             if (numberOfDimensions - numberOfDimensions + 2) < numberOfDimensions:
    #                 for z in range(numpy.shape(self._nodes)[numberOfDimensions - numberOfDimensions + 2]):
    #                     if (numberOfDimensions - numberOfDimensions + 3) < numberOfDimensions:
    #                         for t in range(numpy.shape(self._nodes)[numberOfDimensions - numberOfDimensions + 3]):
    #                             self._nodes[x,y,z,t] = Node(tuple((x,y,z,t)))
    #                     else:
    #                         self._nodes[x,y,z] = Node(tuple((x,y,z)))
    #             else:
    #                 self._nodes[x,y] = Node(tuple((x,y)))
    
    # def __Create_Latticework(self, gridLength, numberOfDimensions):
        
    #     emptyGridDimension = []
    #     for dimension in range(numberOfDimensions):
    #         for g in range(gridLength[dimension]):
    #             emptyGridDimension.append(" ")
        
    #     for dimension in range(numberOfDimensions):
    #         currentGridDimension = []
    #         for g in range(gridLength[dimension]):
    #             currentGridDimension[dimension].append(emptyGridDimension.copy())


    #     for g in range(gridLength[0]):
    #         newNode = Node(tuple((dimension, g)))
    #         currentGridDimension.append(newNode)
    #         self._nodes.append(currentGridDimension)

    # Example: 4x3
    # need a list for the 4 x values
    # then need to make 3 lists for the y values
    # fill each y value list with copies of the x values list

