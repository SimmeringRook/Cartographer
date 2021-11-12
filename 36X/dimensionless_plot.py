'''These are standard aliases for the packages; so I will opt to use standard notation
     for increased future readability'''
import numpy as np
import matplotlib.pyplot as plt

'''Physical constants'''
__c = 1                                 # meters per second
__BH_Mass = 2                           # kg
__G = 1                                 # meters^3 per (kg * second)

#M = (__G * __BH_Mass) / np.power(__c, 2)           # Mass of the Black Hole, as measured in meters

M = 5000

'''Set Resolution Factors'''
__time_step_resolution  = 1 * __c     # meters
__r_step_resolution     = 0.1             # meters
__phi_step_resolution   = 1             # dimensionless
__theta_step_resolution = 1             # dimensionless

''' --- Run time constants --- '''
__start_time    = (0 * __c)             # meters
__stop_time     = (10 * __c)            # meters
__time_iteration_direction = 1 if (__start_time < __stop_time) else -1

__start_r       = 10500#int(2 * M)            # meters
__stop_r        = 50001#int(20 * M)           # meters
__r_iteration_direction = 1 if (__start_r < __stop_r) else -1

__start_phi     = 0                     # dimensionless
__stop_phi      = 2*np.pi               # dimensionless
__phi_iteration_direction = 1 if (__start_phi < __stop_phi) else -1

__start_theta   = 0                     # dimensionless
__stop_theta    = np.pi                 # dimensionless
__theta_iteration_direction = 1 if (__start_theta < __stop_theta) else -1

'''Coordinate Arrays'''
__time_domain   = np.arange( 
                    int(__start_time  / __time_step_resolution), 
                    int(__stop_time / __time_step_resolution), 
                    __time_iteration_direction
                    )
__r_domain      = np.arange( 
                    int(__start_r     / __r_step_resolution), 
                    int(__stop_r / __r_step_resolution), 
                    __r_iteration_direction
                    )
__phi_domain    = np.arange( 
                    int(__start_phi   / __phi_step_resolution), 
                    int(__stop_phi / __phi_step_resolution), 
                    __phi_iteration_direction
                    )
__theta_domain  = np.arange( 
                    int(__start_theta / __theta_step_resolution), 
                    int(__stop_theta / __theta_step_resolution),
                    __theta_iteration_direction
                    )

def proper_distance_between_shells(proper_distance):
    for r in __r_domain :
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
        proper_distance[ (r - __r_domain[0]) * __r_iteration_direction ] = __r_iteration_direction / np.sqrt(1 - (2*M)/(r*__r_step_resolution))

def proper_time_between_shells(proper_time):
    for r in __r_domain :
        proper_time[ (r - __r_domain[0]) * __r_iteration_direction ] = np.sqrt(1 - (2*M)/(r*__r_step_resolution)) * __time_iteration_direction

'''
Make a series of plots including:
    - Limiting cases: BK, 2M Shell
    - Rain Drop (Stone frame, but only with radial motion, starts from rest) 
        / Stone's own frame
    - Shells: 3M, 5M, 20M (? -> far enough away to show trend towards BK)
'''
def make_plot(horizontalValues, verticalValues, plotInfo, title = ''):

    if len(plotInfo) > 1:

        fig, axs = plt.subplots(1, 2)
        for plotNumber in range(len(plotInfo)):
            axs[plotNumber].plot(horizontalValues[plotNumber], verticalValues[plotNumber])
            axs[plotNumber].set_title(plotInfo[plotNumber][0])
            axs[plotNumber].set_xlabel(plotInfo[plotNumber][1])
            axs[plotNumber].set_ylabel(plotInfo[plotNumber][2])

            # if (plotNumber > 0):
            #     ticks = generate_r_ticks(horizontalValues[plotNumber])
            #     axs[plotNumber].set_xticks(ticks[0])
            #     axs[plotNumber].set_xticklabels(ticks[1])

        plt.suptitle(title)

    else:
        fig, ax = plt.subplots()
        ax.plot(horizontalValues, verticalValues)
        ax.set_title(plotInfo[0][0])
        ax.set_xlabel(plotInfo[0][1])
        ax.set_ylabel(plotInfo[0][2])

    plt.show()

# def generate_r_ticks(domain):
#     ticks = {}
#     for tick in domain:
#         multiple_of_M = int(tick / M)
#         if not(multiple_of_M in ticks.keys()):
#             ticks.update({multiple_of_M: str(multiple_of_M ) + "M"})
#     return (list(ticks.keys()), list(ticks.values()))

def give_dimensions_to_domain(domain_of_coordinate, resolution_factor):
    coordinate_array = (domain_of_coordinate * resolution_factor)
    return coordinate_array

def Example1():
    proper_distance = np.zeros( np.shape(__r_domain) )
    proper_distance_between_shells(proper_distance)

    #give dimensions back:
    rcoord = give_dimensions_to_domain(__r_domain, __r_step_resolution)

    plotLabels = ( 'Disagreement in meter stick length Between Each Shell with dr=' + str(__r_step_resolution) + ' meters', 'r-coordinate location of shell', 'Proper Distance (length) of meter stick' )
    make_plot(rcoord, proper_distance, (plotLabels, ))

def Example2():
    proper_time = np.zeros( np.shape(__r_domain) ) #Tricky! Need to comment about this later!
    proper_distance_between_shells(proper_time)

    #give dimensions back:
    rcoord = give_dimensions_to_domain(__r_domain, __r_step_resolution)

    plotLabels = ( 'Disagreement in light clock tick Between Each Shell with dt=' + str(__time_step_resolution) + ' meters', 'r-coordinate location of shell', 'Proper (elapsed) Time of clock tick' )
    make_plot(rcoord, proper_time, (plotLabels, ))

def main():

    Example1()
    Example2()


if __name__ == '__main__':
    main()