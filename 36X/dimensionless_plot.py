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
__time_step_resolution  = 0.1 * __c       # meters            dt
__r_step_resolution     = 0.1           # meters            dr
__phi_step_resolution   = 1             # dimensionless     dphi
__theta_step_resolution = 1             # dimensionless     dtheta

''' --- Run time constants --- '''
__start_time    = (0 * __c)             # meters
__stop_time     = (10 * __c)            # meters
__time_iteration_direction = 1 if (__start_time < __stop_time) else -1

__start_r       = int(2 * M) + 1           # meters
__stop_r        = int(np.power(10, 1) * M)           # meters
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

def bookkeeper_meter_stick_as_measured_from_shell(proper_distance):
    '''
    Bookkeepr: This is a meter stick
    Shell: Uh, you should get a refund, because that's 5 times longer than its supposed to be!
    '''
    for r in __r_domain :
        proper_distance[ (r - __r_domain[0]) * __r_iteration_direction ] = __r_step_resolution / np.sqrt(1 - (2*M)/(r*__r_step_resolution))

def bookkeeper_lightclock_tick_as_measured_from_shell(proper_time):
    '''
    Bookkeepr: That was one tick of my light clock
    Shell: Pretty sure you were sold a faulty clock, cause that wasn't even a full second!
            Also, why does the your voice sound weird? You should get that microphone checked...
    '''
    for r in __r_domain :
        proper_time[ (r - __r_domain[0]) * __r_iteration_direction ] = np.sqrt(1 - (2*M)/(r*__r_step_resolution)) * __time_step_resolution

def shell_meter_stick_as_measured_from_bookkeeper(proper_distance):
    for r in __r_domain :
        proper_distance[ (r - __r_domain[0]) * __r_iteration_direction ] =  np.sqrt(1 - (2*M)/(r*__r_step_resolution)) * __r_step_resolution

def shell_lightclock_tick_as_measured_from_bookkeeper(proper_time):
    for r in __r_domain :
        proper_time[ (r - __r_domain[0]) * __r_iteration_direction ] =  __time_step_resolution / np.sqrt(1 - (2*M)/(r*__r_step_resolution))

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
    bookkeeper_meter_stick_as_measured_from_shell(proper_distance)
    bookkeeper_lightclock_tick_as_measured_from_shell(proper_time)

    #give dimensions back:
    rcoord = give_dimensions_to_domain(__r_domain, __r_step_resolution)

    plotLabels = [
            ( "Flat Space 'meter stick' at from Shell \n with dr=" + str(__r_step_resolution) + " meters",
            'r-coordinate location of shell',
            "Equivalent measured distance at shell (dr_shell)" ),
            ( "Observed in light clock tick Between Each Shell \n with dt=" + str(__time_step_resolution) + " meters",
             'r-coordinate location of shell',
            "Equivalent elapsed time at shell (dt_shell)" )
        ]

    length_contraction_factor_at_shell = np.zeros( np.shape(__r_domain) )
    time_dilaton_factor_at_shell = np.zeros( np.shape(__r_domain) )

    bookkeeper_meter_stick_as_measured_from_shell(length_contraction_factor_at_shell)
    bookkeeper_lightclock_tick_as_measured_from_shell(time_dilaton_factor_at_shell)

    #remove dimensions to create figures of merit:

    length_contraction_factor_at_shell = length_contraction_factor_at_shell / __r_step_resolution
    time_dilaton_factor_at_shell = time_dilaton_factor_at_shell / __time_step_resolution

    make_plot(rcoord, [proper_distance, proper_time], plotLabels, "Disagreement in measurements for Shell Observer versus Flat Space \n M=" +str(M) + " meters")
    
    plotLabels = [
            ( "Flat Space 'meter stick' at from Shell \n with dr=" + str(__r_step_resolution) + " meters",
            'r-coordinate location of shell',
            "Length contraction factor (dr_shell / dr)" ),
            ( "Observed in light clock tick Between Each Shell \n with dt=" + str(__time_step_resolution) + " meters",
             'r-coordinate location of shell',
            "Time Dilaton factor (dt_shell / dt)" )
        ]

    make_plot(rcoord, [length_contraction_factor_at_shell, time_dilaton_factor_at_shell], plotLabels, "Graviational Effects on Shell Observer Measurements \n versus Flat Space with Black Hole Mass = " +str(M) + " meters")
    
    #combine_plots(rcoord, [proper_distance, proper_time], plotLabels[0])


if __name__ == '__main__':
    main()