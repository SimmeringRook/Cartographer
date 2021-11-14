# Standard Python Libraries
import os

# Third Party Libraries
import yaml

# Project Cartographer
import spacetime.schwarzschild as schwarzschild
import coordinate_array

__configuration_file_path = os.path.dirname(__file__) + "\\runtime_configurations.yaml"

def get_configuration_settings():
    coordinate_domains = { }
    try:
        with open(__configuration_file_path) as config_file:
            data = yaml.load(config_file, Loader=yaml.SafeLoader)
            schwarzschild._initialize(data["physical_constants"], data["spacetime_parameters"])
            for dimension in data["coordinate_domains"]:
                coordinate_domains.update({
                    dimension["dimension"]: coordinate_array.Coordinate_Array(
                            start = dimension["start"] * schwarzschild.get_blackhole_mass_in_meters() + 1, #TODO NEED TO FIX THIS; we've hardcoded scale factors!
                            stop = dimension["stop"] * schwarzschild.get_blackhole_mass_in_meters(),
                            resolution = dimension["step"]
                        )
                })

    except yaml.YAMLError as exc:
        print ("Error while parsing YAML file:")
        if hasattr(exc, 'problem_mark'):
            if exc.context != None:
                print ('  parser says\n' + str(exc.problem_mark) + '\n  ' +
                    str(exc.problem) + ' ' + str(exc.context) +
                    '\nPlease correct data and retry.')
            else:
                print ('  parser says\n' + str(exc.problem_mark) + '\n  ' +
                    str(exc.problem) + '\nPlease correct data and retry.')
        else:
            print ("Something went wrong while parsing yaml file")

    return coordinate_domains
