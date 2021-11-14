# Standard Python Libraries


# Third Party Libraries
import numpy as np

# Project Cartographer


SPEED_OF_LIGHT = 1                                 # meters per second
BLACKHOLE_MASS_IN_KG = 2                           # kg
GRAVITATIONAL_CONSTANT = 1                                 # meters^3 per (kg * second)

global BLACKHOLE_MASS_IN_METERS
BLACKHOLE_MASS_IN_METERS = None

def get_blackhole_mass_in_meters():
    global BLACKHOLE_MASS_IN_METERS
    if BLACKHOLE_MASS_IN_METERS is None:
        BLACKHOLE_MASS_IN_METERS = (GRAVITATIONAL_CONSTANT * BLACKHOLE_MASS_IN_KG) / np.power(SPEED_OF_LIGHT, 2) 

    return BLACKHOLE_MASS_IN_METERS

def __build_coordinate_arrays(self, stuff):
    pass

def _remove_dimensions(value, dimension):
    return int( value / dimension)

def _add_dimensions(value, dimension):
    return (value * dimension)


def _initialize(phyiscal_constants):
    global SPEED_OF_LIGHT
    SPEED_OF_LIGHT = phyiscal_constants["speed_of_light"]
    global SPEED_OF_LIGHT
    SPEED_OF_LIGHT = phyiscal_constants["speed_of_light"]
    global SPEED_OF_LIGHT
    SPEED_OF_LIGHT = phyiscal_constants["speed_of_light"]