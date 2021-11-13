'''These are standard aliases for the packages; so I will opt to use standard notation
     for increased future readability'''
import numpy as np
import matplotlib.pyplot as plt

'''Physical constants'''
__c = 1                                 # meters per second
__BH_Mass = 2                           # kg
__G = 1                                 # meters^3 per (kg * second)

#M = (__G * __BH_Mass) / np.power(__c, 2)           # Mass of the Black Hole, as measured in meters

M = 500

'''Set Resolution Factors'''
__time_step_resolution  = 0.1 * __c       # meters            dt
__r_step_resolution     = 0.1           # meters            dr
__phi_step_resolution   = 1             # dimensionless     dphi
__theta_step_resolution = 1             # dimensionless     dtheta

''' --- Run time constants --- '''
__start_time    = (0 * __c)             # meters
__stop_time     = (10 * __c)            # meters
__time_iteration_direction = 1 if (__start_time < __stop_time) else -1

__start_r       = int(2 * M) + 1           # meters
__stop_r        = int(np.power(10, 2) * M)           # meters
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

def proper_time_at_shell(proper_time):
    for r in __r_domain :
        proper_time[ (r - __r_domain[0]) * __r_iteration_direction ] = np.sqrt(1 - (2*M)/(r*__r_step_resolution)) * __time_iteration_direction

'''
Make a series of plots including:
    - Limiting cases: BK, 2M Shell
    - Rain Drop (Stone frame, but only with radial motion, starts from rest) 
        / Stone's own frame
    - Shells: 3M, 5M, 20M (? -> far enough away to show trend towards BK)
'''
def make_plot(horizontal_values, vertical_values, plot_info, title = ''):

    if len(plot_info) > 1:

        fig, axs = plt.subplots(nrows = len(plot_info), sharex=True)
        for plotNumber in range(len(plot_info)):
            axs[plotNumber].plot(horizontal_values, vertical_values[plotNumber])
            axs[plotNumber].set_title(plot_info[plotNumber][0])
            axs[plotNumber].set_xlabel(plot_info[plotNumber][1])
            axs[plotNumber].set_ylabel(plot_info[plotNumber][2])

            # if (plotNumber > 0):
            #     ticks = generate_r_ticks(horizontalValues[plotNumber])
            #     axs[plotNumber].set_xticks(ticks[0])
            #     axs[plotNumber].set_xticklabels(ticks[1])

        plt.suptitle(title)

    else:
        fig, ax = plt.subplots()
        ax.plot(horizontal_values, vertical_values)
        ax.set_title(plot_info[0][0])
        ax.set_xlabel(plot_info[0][1])
        ax.set_ylabel(plot_info[0][2])

    plt.show()

def combine_plots(shared_axis, vertical_values, plot_info):
    fig, ax = plt.subplots()
    for plotNumber in range(len(vertical_values)):
        ax.plot(shared_axis, vertical_values[plotNumber])
    ax.set_title(plot_info[0])
    ax.set_xlabel(plot_info[1])
    ax.set_ylabel(plot_info[2])
    ax.set_ylim([0,5])
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

def main():
    proper_distance = np.zeros( np.shape(__r_domain) )
    proper_time = np.zeros( np.shape(__r_domain) ) #Tricky! Need to comment about this later!

    # If we invert these functions, we'll get "length contraction" and "time dilation", respectively
    # E.g., how much slower a clock is ticking and smaller a meter stick is, at shell `r` compared to at BK
    proper_distance_between_shells(proper_distance)
    proper_time_at_shell(proper_time)

    #give dimensions back:
    rcoord = give_dimensions_to_domain(__r_domain, __r_step_resolution)

    plotLabels = [
            ( 'Disagreement in meter stick length From Shell to Bookkeeper \n with dr=' + str(__r_step_resolution) + ' meters and M=' +str(M) + ' meters',
            'r-coordinate location of shell',
            'Proper Distance (length) of meter stick' ),
            ( 'Disagreement in light clock tick Between Each Shell \nwith dt=' + str(__time_step_resolution) + ' meters and M=' +str(M) + ' meters',
             'r-coordinate location of shell',
            'Proper (elapsed) Time of clock tick' )
        ]
#    make_plot(rcoord, [proper_distance, proper_time], plotLabels, "Comparison of measurements for Shell Observer to Flat Space")
    combine_plots(rcoord, [proper_distance, proper_time], plotLabels[0])


if __name__ == '__main__':
    main()