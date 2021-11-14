# Standard Python Libraries

# Third Party Libraries
import numpy as np

# Project Cartographer

def create_new_domain(start = int(), stop = int(), resolution = float()):
    dimensionless_start_value = remove_dimensions(start, resolution)
    dimensionless_stop_value = remove_dimensions(stop, resolution)
    _new_domain = np.arange( 
            dimensionless_start_value,
            dimensionless_stop_value,
            get_iteration_direction(
                    dimensionless_start_value,
                    dimensionless_stop_value
                )
        ) 
    return _new_domain

def remove_dimensions(value_to_remove_dimensions_from, dimensions_to_remove):
    return int(value_to_remove_dimensions_from / dimensions_to_remove)

def add_dimensions(value_to_add_dimensions_to, dimensionful_variable):
    return (value_to_add_dimensions_to * dimensionful_variable)

def get_iteration_direction(coordinate_array):
    return (1 if (coordinate_array[0] < coordinate_array[1]) else -1 )

def get_iteration_direction(start, stop):
    return (1 if (start < stop) else -1 )
