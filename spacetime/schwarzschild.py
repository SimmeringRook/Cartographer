# Standard Python Libraries

# Third Party Libraries
import numpy as np

# Project Cartographer

def get_blackhole_mass_in_meters():
    global BLACKHOLE_MASS_IN_METERS
    if BLACKHOLE_MASS_IN_METERS is None:
        BLACKHOLE_MASS_IN_METERS = (GRAVITATIONAL_CONSTANT * BLACKHOLE_MASS_IN_KG) / np.power(SPEED_OF_LIGHT, 2) 
    return BLACKHOLE_MASS_IN_METERS

def get_curvature_factor():
    global CURVATURE_FACTORS, ALMOST_CURVATURE_FACTOR
    if CURVATURE_FACTORS is None:
        M = get_blackhole_mass_in_meters()
        ALMOST_CURVATURE_FACTOR = np.reciprocal(np.true_divide(np.multiply(r_coord_local.domain, r_coord_local.step_resolution), 2*M))
        CURVATURE_FACTORS = np.sqrt(np.ones(np.shape(r_coord_local.domain)) - ALMOST_CURVATURE_FACTOR)
    return CURVATURE_FACTORS

global SPEED_OF_LIGHT
SPEED_OF_LIGHT = None
global GRAVITATIONAL_CONSTANT
GRAVITATIONAL_CONSTANT = None

BLACKHOLE_MASS_IN_KG = None
global BLACKHOLE_MASS_IN_METERS
BLACKHOLE_MASS_IN_METERS = None

r_coord_local = None
CURVATURE_FACTORS = None
global ALMOST_CURVATURE_FACTOR
ALMOST_CURVATURE_FACTOR = None

def _initialize(phyiscal_constants, spacetime_parameters, r_circumference_parameters):

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
    
    import coordinate_array

    global r_coord_local
    r_coord_local = coordinate_array.Coordinate_Array(
                            start = r_circumference_parameters["start"],
                            stop = r_circumference_parameters["stop"],
                            resolution = r_circumference_parameters["step"]
        )
    get_curvature_factor()

def get_bookkeeper_meter_stick_as_measured_from_shell(dr):
    '''
    Bookkeeper: This is a meter stick
    Shell: Uh, you should get a refund, because that's 5 times longer than its supposed to be!
    '''
    return np.multiply(np.reciprocal(get_curvature_factor()), dr)

def get_bookkeeper_lightclock_tick_as_measured_from_shell(dt):
    '''
    Bookkeeper: That was one tick of my light clock
    Shell: Pretty sure you were sold a faulty clock, cause that wasn't even a full second!
            Also, why does the your voice sound weird? You should get that microphone checked...
    '''
    return np.multiply(get_curvature_factor(), dt)

def get_bookkeeper_speed_of_infalling_stone():
    '''
    Bookkeeper coordinates for stone free falling from infinity
    '''
    return np.multiply(
            np.ones(np.shape(ALMOST_CURVATURE_FACTOR)) - ALMOST_CURVATURE_FACTOR,
            - np.sqrt(ALMOST_CURVATURE_FACTOR)
        )
    
def get_shell_speed_of_infalling_stone():
    return (- np.sqrt(ALMOST_CURVATURE_FACTOR))