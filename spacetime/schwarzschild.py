# Standard Python Libraries


# Third Party Libraries
import numpy as np

# Project Cartographer


def get_blackhole_mass_in_meters():
    global BLACKHOLE_MASS_IN_METERS
    if BLACKHOLE_MASS_IN_METERS is None:
        BLACKHOLE_MASS_IN_METERS = (GRAVITATIONAL_CONSTANT * BLACKHOLE_MASS_IN_KG) / np.power(SPEED_OF_LIGHT, 2) 

    return BLACKHOLE_MASS_IN_METERS

global SPEED_OF_LIGHT
SPEED_OF_LIGHT = None
global GRAVITATIONAL_CONSTANT
GRAVITATIONAL_CONSTANT = None

BLACKHOLE_MASS_IN_KG = None
global BLACKHOLE_MASS_IN_METERS
BLACKHOLE_MASS_IN_METERS = None

def _initialize(phyiscal_constants, spacetime_parameters):

    global SPEED_OF_LIGHT
    SPEED_OF_LIGHT = phyiscal_constants["speed_of_light"]
    global GRAVITATIONAL_CONSTANT
    GRAVITATIONAL_CONSTANT = phyiscal_constants["gravitational_constant"]

    global BLACKHOLE_MASS_IN_KG
    if "in_kg" in spacetime_parameters["mass"]:
        BLACKHOLE_MASS_IN_KG = spacetime_parameters["mass"]["in_kg"]
        
    global BLACKHOLE_MASS_IN_METERS
    if "in_meters" in spacetime_parameters["mass"]:
        BLACKHOLE_MASS_IN_METERS = spacetime_parameters["mass"]["in_meters"]
