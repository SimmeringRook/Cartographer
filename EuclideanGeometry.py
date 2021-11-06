from SpacetimeGeometry import SpacetimeGeometry


class EuclideanGeometry(SpacetimeGeometry):

    __Metric = tuple(( tuple((1,)), tuple((1,1)), tuple((1,1,1)) ))

    def __init__(self, dimesionality=2):
        super().__init__(EuclideanGeometry.__Metric[len(EuclideanGeometry.__Metric) - dimesionality])
