import configuration_reader as cf_r
import coordinate_array
import spacetime.schwarzschild as schwarzschild

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

def main():
    
    coordinate_domains = cf_r.get_configuration_settings()
    if len(coordinate_domains) == 0:
        print("Error in loading runtime_configurations.yaml. Check to make sure the file is located in the same directory and has content.")
        return

    proper_distance = schwarzschild.get_bookkeeper_meter_stick_as_measured_from_shell(coordinate_domains["reduced circumference"].step_resolution)
    proper_time = schwarzschild.get_bookkeeper_lightclock_tick_as_measured_from_shell(coordinate_domains["time"].step_resolution)

    bk_stone_freefall_speed = schwarzschild.get_bookkeeper_speed_of_infalling_stone()
    shell_stone_freefall_speed = schwarzschild.get_shell_speed_of_infalling_stone()

    plotLabels = [
        ( f"Flat Space 'meter stick' at from Shell with dr={coordinate_domains['reduced circumference'].step_resolution} meters",
        'r-coordinate location of shell',
        "Equivalent measured distance at shell (dr_shell)" ),
        ( f"Observed in light clock tick Between Each Shell with dt={coordinate_domains['time'].step_resolution} meters",
            'r-coordinate location of shell',
        "Equivalent elapsed time at shell (dt_shell)" ),
        ( f"in-falling stone's observed speed according to Bookkeeper with dr={coordinate_domains['reduced circumference'].step_resolution} meters",
            'r-coordinate',
        "Speed at r-coordinate" ),
        ( f"in-falling stone's observed speed by Shell as it passes each Shell with dr={coordinate_domains['reduced circumference'].step_resolution} meters",
            'r-coordinate location of shell',
        "Speed of Stone at Shell (factors of c)" ),
    ]

    make_plot(
        horizontal_values= coordinate_array.add_dimensions(coordinate_domains["reduced circumference"].domain, coordinate_domains["reduced circumference"].step_resolution),
        vertical_values= [proper_distance, proper_time, bk_stone_freefall_speed, shell_stone_freefall_speed],
        plot_info= plotLabels
        )

if __name__ == '__main__':
    main()