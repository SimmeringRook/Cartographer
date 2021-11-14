# Standard Python Libraries

# Third Party Libraries
import numpy as np

# Project Cartographer
import configuration as config
import coordinate_array

'''Since the starting value of __r_domain isn't necessarilly 0, we need to subtract the difference to access
the first index in the array.
E.g., 
    We want the r-coordinate domain of our calculations to be within [2M, 40M] with a resolution of 0.1.
    __r_domain will have the values in an array of size (stop - start)/resolution;
    So, during the first iteration of this loop, `r` will have the value of (2M / 0.1) = 20M.
    We want to use `r` to also index the proper_distance array, as they are of the same length, so:
    (r - __r_domain[0]) = 0

Next problem: we've set the step direction for the domains to dynamically respond to different orders.
E.g.,
    (r - __r_domain[0]) = 0 still works for the first iteration of the loop,
    but since r = __r_domain[1], where __r_domain[1] is now less than __r_domain[0],
    this will throw an error as "-1" is not a valid index.
    We can resolve this by multiplying by the __r_iteration_direction to correct to a positive index
    and the loop will iterrate correctly iregardless if our intervals look like: [2M, 40M] or [40M, 2M]
'''

def proper_distance_between_shells(proper_distance, r_domain):
    iteration_direction = coordinate_array.get_iteration_direction(r_domain)
    for r in r_domain :
        index_value = (r - r_domain[0]) * iteration_direction
        proper_distance[ index_value ] = (
            __r_step_resolution / np.sqrt(1 - (2*M)/(r*__r_step_resolution))
        )

def proper_time_at_shell(proper_time, r_domain):
    iteration_direction = coordinate_array.get_iteration_direction(r_domain)
    for r in r_domain :
        index_value = (r - r_domain[0]) * iteration_direction
        proper_time[ index_value ] = np.sqrt(1 - (2*config.get_blackhole_mass_in_meters())/(r*__r_step_resolution)) * __time_step_resolution