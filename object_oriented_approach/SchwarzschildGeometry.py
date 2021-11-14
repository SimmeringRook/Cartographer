from SpacetimeGeometry import SpacetimeGeometry
from math import math

class SchwarzschildGeometry(SpacetimeGeometry):

    __Metric = tuple(( tuple((1,)), tuple((1,-1)), tuple((1,1,-1)) ))

    def __init__(self, dimesionality=2):
        super().__init__(SchwarzschildGeometry.__Metric[len(SchwarzschildGeometry.__Metric) - dimesionality])

    def Act_Metric_On(self, pForm1, pForm2):
        metricResult = 0
        for i in range(len(self.__metric)):
            metricResult += pForm1[i] * (self.__metric[i] * self.get_Physical_Scale_Factor(1)) * pForm2[i]
        return metricResult

    def get_Physical_Scale_Factor(coordinate_location, dimension=0):
        return 1/(math.pow(coordinate_location, 2))