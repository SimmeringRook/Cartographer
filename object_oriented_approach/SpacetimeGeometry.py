class SpacetimeGeometry:
    
    #__Metric = tuple((1,1,1,-1))

    def __init__(self, metric=tuple(((1-2*M/r),1,1,-1))):
        print("Creating Geometry with the metric:", metric)
        self.__metric = metric

    def get_Dimensionality(self):
        return len(self.__metric)

    def Act_Metric_On(self, pForm1, pForm2):
        metricResult = 0
        for i in range(len(self.__metric)):
            metricResult += pForm1[i] * self.__metric[i] * pForm2[i]
        return metricResult