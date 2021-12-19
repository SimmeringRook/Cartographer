import configuration_reader as cf_r
import coordinate_array
import spacetime.schwarzschild as schwarzschild
import numpy as np

def make_plot(horizontal_values, vertical_values, plot_info, title = ''):

    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(nrows = len(plot_info), sharex=True)

    for plotNumber in range(len(plot_info)):
        axs[plotNumber].plot(horizontal_values, vertical_values[plotNumber])
        axs[plotNumber].set_title(plot_info[plotNumber][0])
        axs[plotNumber].set_xlabel(plot_info[plotNumber][1])
        axs[plotNumber].set_ylabel(plot_info[plotNumber][2])

    plt.suptitle("Disagreement in measurements for Shell Observer versus Flat Space M=" +str(schwarzschild.get_blackhole_mass_in_meters()) + " meters")
    plt.show()

def make_plot_speed(horizontal_values, vertical_values, plot_info, title = '', colors = list()):

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    for i in range(len(vertical_values)):
        if i > 1:
            ax.plot(horizontal_values, vertical_values[i], color=colors[i-2])
        else:
            ax.plot(horizontal_values, vertical_values[i], label=plot_info[0][i])
    ax.set_xlabel(plot_info[1])
    ax.set_ylabel(plot_info[2])

    plt.legend()
    plt.suptitle(f"Speed of In-Falling Stone as measured from different observers \nM={schwarzschild.get_blackhole_mass_in_meters()} meters, dr={title} meters")
    plt.show()

def main():
    
    coordinate_domains = cf_r.get_configuration_settings()

    # proper_distance = schwarzschild.get_bookkeeper_meter_stick_as_measured_from_shell(coordinate_domains["reduced circumference"].step_resolution)
    # proper_time = schwarzschild.get_bookkeeper_lightclock_tick_as_measured_from_shell(coordinate_domains["time"].step_resolution)

    bk_stone_freefall_speed = schwarzschild.get_bookkeeper_speed_of_infalling_stone()
    shell_stone_freefall_speed = schwarzschild.get_shell_speed_of_infalling_stone()
    
    dr_bookkeeper = coordinate_domains["reduced circumference"].step_resolution
    M = schwarzschild.get_blackhole_mass_in_meters()
    five_M = (5*M)/dr_bookkeeper

    # print(np.shape(np.arange(coordinate_domains["reduced circumference"].domain[0], five_M, (M/dr_bookkeeper))))

    shells = [ ]
    fiveM_speed = np.zeros(np.shape(coordinate_domains["reduced circumference"].domain))
    initial_wavelength = 1/(740 * np.power(10, 6))
    print(np.shape(shell_stone_freefall_speed), np.shape(coordinate_domains["reduced circumference"].domain))
    for r_coord in coordinate_domains["reduced circumference"].domain:
        fiveM_speed[r_coord - int((2*M + 1)/dr_bookkeeper)] = schwarzschild.tevian_speed_at_shell(initial_wavelength, r_coord, five_M)
    shells.append(schwarzschild.tevian_speed_at_shell)
    # for shell_coord in np.arange(coordinate_domains["reduced circumference"].domain[0], five_M, (M/dr_bookkeeper)):
    #     shells.append(schwarzschild.get_speed_measurements_from_specified_shell(shell_coord))

    # below_2M = np.arange(coordinate_domains["reduced circumference"].domain[0]-99, (2*M)/dr_bookkeeper, -0.1)

    # print(
    #     coordinate_domains["reduced circumference"].domain[0],
    #     (2*M)/dr_bookkeeper,
    #     np.shape(below_2M),
    #     len(shells)
    #     )
    # for shell_coord in below_2M:
    #     shells.append(schwarzschild.get_speed_measurements_from_specified_shell(shell_coord))

    # print(schwarzschild.get_speed_measurements_from_specified_shell(coordinate_domains["reduced circumference"].domain[0], dr_bookkeeper)[0])
    # print(schwarzschild.get_shell_speed_of_infalling_stone()[0])
    # unstable_rcoord = (3*schwarzschild.get_blackhole_mass_in_meters())/dr_bookkeeper
    # unstable_shell_freefall_speed = schwarzschild.get_speed_measurements_from_specified_shell(unstable_rcoord, dr_bookkeeper)

    colors = [ ]
    for c in np.linspace(0, 0.8, num=len(shells)):
        colors.append(str(c))

    # print(len(shells))
    # fiveM_rcoord = (5*schwarzschild.get_blackhole_mass_in_meters())/dr_bookkeeper
    # fiveM_shell_freefall_speed = schwarzschild.get_speed_measurements_from_specified_shell(fiveM_rcoord, dr_bookkeeper)

    # plotLabels = [
    #     ( f"Flat Space 'meter stick' at from Shell with dr={coordinate_domains['reduced circumference'].step_resolution} meters",
    #     'r-coordinate location of shell',
    #     "Equivalent measured distance at shell (dr_shell)" ),
    #     ( f"Observed in light clock tick Between Each Shell with dt={coordinate_domains['time'].step_resolution} meters",
    #         'r-coordinate location of shell',
    #     "Equivalent elapsed time at shell (dt_shell)" ),
    #     ( f"in-falling stone's observed speed according to Bookkeeper with dr={coordinate_domains['reduced circumference'].step_resolution} meters",
    #         'r-coordinate',
    #     "Speed at r-coordinate" ),
    #     ( f"in-falling stone's observed speed by Shell as it passes each Shell with dr={coordinate_domains['reduced circumference'].step_resolution} meters",
    #         'r-coordinate location of shell',
    #     "Speed of Stone at Shell (factors of c)" ),
    # ]

    # make_plot(
    #     horizontal_values= coordinate_array.add_dimensions(coordinate_domains["reduced circumference"].domain, coordinate_domains["reduced circumference"].step_resolution),
    #     vertical_values= [proper_distance, proper_time, bk_stone_freefall_speed, shell_stone_freefall_speed],
    #     plot_info= plotLabels
    #     )

    plotLabels = [
        ("Bookkeeper", "Shell = 2M", "Shell = 3M", "Shell = 5M"),
        "r-coordinate/M",
        "Speed (mutliple of c)"
    ]

    r_coord_as_multiples_of_M = np.true_divide(coordinate_array.add_dimensions(coordinate_domains["reduced circumference"].domain, coordinate_domains["reduced circumference"].step_resolution), schwarzschild.get_blackhole_mass_in_meters())

    make_plot_speed(
        horizontal_values=r_coord_as_multiples_of_M, 
        vertical_values=[bk_stone_freefall_speed, shell_stone_freefall_speed] + shells, 
        plot_info=plotLabels, 
        title=str(dr_bookkeeper), 
        colors=colors
        )

if __name__ == '__main__':
    main()