# Standard Python Libraries
import os

# Third Party Libraries
import yaml

# Project Cartographer
import spacetime.schwarzschild as schwarzschild
import coordinate_array

__configuration_file_path = os.path.dirname(__file__) + "\\runtime_configurations.yaml"

def get_configuration_settings():
    """Read in the run time parameters

    Returns:
        [Coordinate_Array]: [A dictionary of Coordinate_Array]
    """
    coordinate_domains = { }
    try:
        with open(__configuration_file_path) as config_file:
            data = yaml.load(config_file, Loader=yaml.SafeLoader)
            
            if len(data["coordinate_domains"]) < 1 :
                raise RuntimeError('No coordinate domains specified inside runtime_configurations.yaml.')
            
            for dimension in data["coordinate_domains"]:
                if (dimension["dimension"] == "reduced circumference"):
                    schwarzschild._initialize(data["physical_constants"], data["spacetime_parameters"], dimension)
                coordinate_domains.update({
                dimension["dimension"]: coordinate_array.Coordinate_Array(
                        start = dimension["start"],
                        stop = dimension["stop"],
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
    except RuntimeError('') as err:
        print("Error in loading runtime_configurations.yaml. Check to make sure the file is located in the same directory and has content.")
    return coordinate_domains
