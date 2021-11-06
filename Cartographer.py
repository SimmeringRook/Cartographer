from EuclideanGeometry import EuclideanGeometry
from Latticework import Latticework
from SchwarzschildGeometry import SchwarzschildGeometry
from SpacetimeGeometry import SpacetimeGeometry

def main():
    gridsize = tuple((4,4,4,1))
    lattice = Latticework(gridsize)

    dx = tuple((2,0,0,0))
    dy = tuple((0,2,0,0))
    dt = tuple((0,0,0,4))

    euclideanPath = mark_out_path(dx, dy)
    minkowskiPath = mark_out_path(dx,dt)

    print("Euclidean:", euclideanPath, lattice._spacetime.Act_Metric_On(euclideanPath,euclideanPath))
    lattice._spacetime = SchwarzschildGeometry()
    print("Schwarzschild:", minkowskiPath, lattice._spacetime.Act_Metric_On(minkowskiPath,minkowskiPath))
    #print(lattice._nodes)

def mark_out_path(start, stop):
    return tuple(map(lambda i, j: i - j, start, stop))

if __name__ == '__main__':
    main()