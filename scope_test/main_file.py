import supporting_file as sf


GLOBAL_IN_MAINFILE_HEADER = "GLOBAL_IN_MAINFILE_HEADER"
GLOBAL_IN_MAINFILE = "GLOBAL_IN_MAINFILE"


def main():

    print(sf.__GLOBAL_IN_SUPPORTING)

    print(GLOBAL_IN_MAINFILE_HEADER)

    global GLOBAL_IN_MAINFILE
    GLOBAL_IN_MAINFILE += " assignemnt in main" 
    print(GLOBAL_IN_MAINFILE)

    print(sf.GLOBAL_IN_SUPPORTING_HEADER)
    print(sf.GLOBAL_IN_SUPPORTING)
    print(sf.get_supporting())
    print(sf.GLOBAL_IN_SUPPORTING)

    # print(_GLOBAL_IN_SUPPORTING)
    # print(get_hidden_supporting())
    # print(_GLOBAL_IN_SUPPORTING)

    


if __name__ == '__main__':
    main()