'''These are standard aliases for the packages; so I will opt to use standard notation for increased future readability'''
import numpy as np
import matplotlib.pyplot as plt

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

def shape_of_bound_orbit():
    pass

def radial_position_at_propertime(tau):
    '''
    Using Equation 9.38 from Page 198 of Hartle:
        r(tau) = (3/2)^(2/3) * (2M)^(1/3) * (tau_final - tau)^(2/3)
    
    Since (3/2) and (2M) are constant values, we can save some efficency by calculating these at the start of the script and just reference the pre-calcualted value using `rad_const`
    '''
    return ( rad_const * np.power( (tau_final - tau), (2/3.0) ) )

def effective_potential(rcoordinate, orbitalAngularMomentum):
    return (- (G*M)/rcoordinate + np.power( (orbitalAngularMomentum / rcoordinate), 2) * 0.5 - ( (G*M)/np.power(c, 2) ) * (np.power(orbitalAngularMomentum, 2) / np.power(rcoordinate, 3)) ) * (1/ np.power(c, 2))

def make_plot(horizontalValues, verticalValues):
    fig, ax = plt.subplots()
    ax.plot(horizontalValues, verticalValues)
    plt.show()

def main():
    
    # for tau in tcoord:
    #     radial_position_at_time_t[tau - tcoord[0]] = radial_position_at_propertime(tau * bookkeeper_timestep)
    # make_plot(radial_position_at_time_t, tcoord)

    for r in rcoord:
        v_effective[r - rcoord[0]] = effective_potential(r, 5)
    #rescale the rcoordinates to be factors of M
    scaled_rcoord = np.multiply(rcoord, (bookkeeper_rstep/M) )
    make_plot(scaled_rcoord, v_effective)

if __name__ == '__main__':
    main()