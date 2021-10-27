from SpacetimeGeometry import SpacetimeGeometry


class EuclideanGeometry(SpacetimeGeometry):
    
    __2DEuclidean = tuple((1,1))

    def __init__(self, dimesionality=2):
        euclideanMetric = tuple((tuple((1,1)), tuple((1,1,1))))
        super().__init__(euclideanMetric[dimesionality-2])