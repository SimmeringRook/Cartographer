import configuration_reader as cf_r
import spacetime.schwarzschild as schwarzschild

def main():
    
    coordinate_domains = cf_r.get_configuration_settings()
    if len(coordinate_domains) == 0:
        print("Error in loading runtime_configurations.yaml. Check to make sure the file is located in the same directory and has content.")
        return

    print(coordinate_domains)
    print(coordinate_domains["time"])

if __name__ == '__main__':
    main()