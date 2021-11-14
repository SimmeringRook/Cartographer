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

def get_bookkeeper_meter_stick_as_measured_from_shell(r_coord):
    '''
    Bookkeeper: This is a meter stick
    Shell: Uh, you should get a refund, because that's 5 times longer than its supposed to be!
    '''
    M = get_blackhole_mass_in_meters()
    proper_distance = np.zeros (np.shape(r_coord.domain) )
    for r in r_coord.domain:
        proper_distance[ (r - r_coord.domain[0]) * r_coord.iteration_direction ] = r_coord.step_resolution / np.sqrt(1 - (2*M)/(r*r_coord.step_resolution))
    return proper_distance

def get_bookkeeper_lightclock_tick_as_measured_from_shell(r_coord, dt):
    '''
    Bookkeeper: That was one tick of my light clock
    Shell: Pretty sure you were sold a faulty clock, cause that wasn't even a full second!
            Also, why does the your voice sound weird? You should get that microphone checked...
    '''
    M = get_blackhole_mass_in_meters()
    proper_time = np.zeros (np.shape(r_coord.domain) )
    for r in r_coord.domain:
        proper_time[ (r - r_coord.domain[0]) * r_coord.iteration_direction ] = np.sqrt(1 - (2*M)/(r*r_coord.step_resolution)) * dt
    return proper_time