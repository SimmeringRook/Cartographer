class SpacetimeGeometry:
    
    __Metric = tuple((1,1,1,-1))

    def __init__(self, metric=tuple((1,1,1,-1))):
        self.__Metric = metric

    def get_Dimensionality(self):
        return len(self.__Metric)

    def get_LineElement_Of(self,drVector):
        return self.Act_Metric_On(drVector)

    def Act_Metric_On(pForm1, pForm2):
        metricResult = 0
        return metricResult