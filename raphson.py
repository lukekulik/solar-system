# Newton-Raphson method for orbit calculations using numpy arrays;
from numpy import linspace, abs, sqrt, sin, cos, arctan2, array, pi


def orbit(m0, e, a, inclination, ascension, n, acc=1.e-2):
    m = linspace(m0, 2 * pi + m0, n)
    ecc_anom = m
    ecc_anom_old = 0
    while acc < abs(ecc_anom - ecc_anom_old).max():  # Newton-Raphson solver for eccentric anomaly (E)
        ecc_anom_old = ecc_anom  # assigning previous value for accuracy comparison
        ecc_anom -= (ecc_anom - m - e * sin(ecc_anom)) / (1. - e * cos(ecc_anom))
        # function for E divided by its derivative w.r.t E

    theta = 2. * arctan2(sqrt(1. + e) * sin(ecc_anom / 2.),
                         sqrt(1. - e) * cos(ecc_anom / 2.))  # true anomaly

    r = a * (1 - e * cos(ecc_anom))  # radius

    theasc = theta - ascension

    # conversion to cartesian coordinates:

    x = r * (cos(ascension) * cos(theasc) - sin(ascension) * sin(theasc) * cos(inclination))

    z = r * (sin(ascension) * cos(theasc) + cos(ascension) * sin(theasc) * cos(inclination))

    y = r * (sin(theta - ascension) * sin(inclination))

    coord = array((x, y, z))

    return coord  # returning an array with the coordinates for one orbital period for a given celestial body
