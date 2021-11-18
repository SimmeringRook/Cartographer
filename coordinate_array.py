# Standard Python Libraries

# Third Party Libraries
import numpy as np

# Project Cartographer

class Coordinate_Array:

    def __init__(self, start = int(), stop = int(), resolution = float()):
        dimensionless_start_value = remove_dimensions(start, resolution)
        dimensionless_stop_value = remove_dimensions(stop, resolution)
        self.step_resolution = resolution
        self.domain = np.arange( 
                dimensionless_start_value,
                dimensionless_stop_value,
                (1 if (start < stop) else -1 )
            )
        self.size = np.shape(self.domain)[0]

def remove_dimensions(value_to_remove_dimensions_from, dimensions_to_remove):
    return int(value_to_remove_dimensions_from / dimensions_to_remove)

def add_dimensions(value_to_add_dimensions_to, dimensionful_variable):
    return np.multiply(value_to_add_dimensions_to, dimensionful_variable)
