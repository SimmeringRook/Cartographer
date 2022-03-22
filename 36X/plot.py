'''These are standard aliases for the packages; so I will opt to use standard notation for increased future readability'''
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

'''Physical constants'''
c = 1
M = 1
G = 1

'''Runtime constants'''
rad_const = np.power(1.5, (2/3.0)) * np.power(2*M, (1/3.0))
tau_final = 20.0
r_max = 40.0

'''Set Geometric scale factors'''
bookkeeper_timestep = 0.1
bookkeeper_rstep = 1

'''Arrays'''
tcoord = np.arange(0, int(tau_final/bookkeeper_timestep))
rcoord = np.arange( int(2*M), int( (r_max*M)/bookkeeper_rstep ) )

radial_position_at_time_t = np.zeros( np.shape(tcoord) )
v_effective = np.zeros( np.shape(rcoord) )
phi_position_at_rcoord = np.zeros( np.shape(rcoord) )

def shape_of_bound_orbit(rcoordinate, orbitalAngularMomentum, totalenergy_per_unitrestmass):
    return (orbitalAngularMomentum / np.power(rcoordinate, 2)) * 1 / np.power(( np.power(totalenergy_per_unitrestmass, 2) - (1 - (2*M)/rcoordinate) * (1 + np.power( (orbitalAngularMomentum / rcoordinate), 2) ) ), 0.5)

''' 
    - This should only be a straight line from the rain drop's view
    - Shell observers should see an increase up to their shell and then decrease to 0 at 2M
    - Bookkeeper should see an increase up to some r = ??M before decreasing to 0 at 2M
    - At some point, work on limiting case as Shell -> 2M, slope -> c
'''
def radial_position_at_propertime(tau):
    '''
    Using Equation 9.38 from Page 198 of Hartle:
        r(tau) = (3/2)^(2/3) * (2M)^(1/3) * (tau_final - tau)^(2/3)
    
    Since (3/2) and (2M) are constant values, we can save some efficency by calculating these at the start of the script and just reference the pre-calcualted value using `rad_const`
    '''
    return ( rad_const * np.power( (tau_final - tau), (2/3.0) ) )

def effective_potential(rcoordinate, orbitalAngularMomentum):
    return (- (G*M)/rcoordinate + np.power( (orbitalAngularMomentum / rcoordinate), 2) * 0.5 - ( (G*M)/np.power(c, 2) ) * (np.power(orbitalAngularMomentum, 2) / np.power(rcoordinate, 3)) ) * (1/ np.power(c, 2))

'''
Make a series of plots including:
    - Limiting cases: BK, 2M Shell
    - Rain Drop (Stone frame, but only with radial motion, starts from rest) / Stone's own frame
    - Shells: 3M, 5M, 20M (? -> far enough away to show trend towards BK)
'''
def make_plot(horizontalValues, verticalValues, plotInfo):
    fig, ax = plt.subplots()
    ax.plot(horizontalValues, verticalValues)
    ax.set_title(plotInfo[0])
    ax.set_xlabel(plotInfo[1])
    ax.set_ylabel(plotInfo[2])
    plt.show()

def get_proper_distance_for_shell(r, M, dr):
  return dr/sqrt(1-(2*M)/r)


def main():
    M = 5
    dr = 1

    r_coordinates = np.arange(2*M+dr, 15*M, dr)
    proper_distance = np.zeros(r_coordinates.shape)
    comparison = np.zeros(r_coordinates.shape)

    for r in r_coordinates:
        proper_distance[r-(2*M+dr)] = get_proper_distance_for_shell(r, M, dr)
        comparison[r-(2*M+dr)] = get_proper_distance_for_shell(r, M, dr)

    print(proper_distance[0])

    #plt.scatter(r_coordinates, proper_distance)
    plt.plot(r_coordinates, comparison)
    plt.title(f"Proper distance between shells separated by {dr=} meters \n and {M=} meters")
    plt.xlabel("r-coordinate")
    plt.ylabel("Physical distance between shells")
    plt.savefig(fname="CoreDesign_Plot.png")


if __name__ == '__main__':
    main()