# universal variable formulation, 3rd order differential equation solver for orbital prediction,
# implemented due to huge efficiency issues when using conventional methods (loops, recursion),
# algorithms based on Vectorized Analytic Two Body Propagator in MATLAB Copyright (c) 2012, Darin Koblick

from scipy.spatial.distance import cdist
from vis import *
from parameters import u, sun_radius
import numpy as np

u2 = np.sqrt(u)


def c2c3(psi):  # Stumpff functions definitions

    c2, c3 = 0, 0

    if np.any(psi > 1e-6):
        c2 = (1 - np.cos(np.sqrt(psi))) / psi
        c3 = (np.sqrt(psi) - np.sin(np.sqrt(psi))) / np.sqrt(psi ** 3)

    if np.any(psi < -1e-6):
        c2 = (1 - np.cosh(np.sqrt(-psi))) / psi
        c3 = (np.sinh(np.sqrt(-psi)) - np.sqrt(-psi)) / np.sqrt(-psi ** 3)

    if np.any(abs(psi) <= 1e-6):
        c2 = 0.5
        c3 = 1. / 6.

    return c2, c3


def position(r0, v0, t, trailer, tol=100):
    r0mag = mag(r0)  # magnitude of the distance from the Sun
    v0mag = mag(v0)  # magnitude of spacecraft velocity

    alpha = -(v0mag * v0mag) / u + 2. / r0mag  # constant term in differential equation

    # compute initial guess (x0) for Newton-Raphson solver:

    s0 = 0

    if alpha > 0.000001:  # elliptical orbits
        s0 = u2 * t * alpha

    if abs(alpha) < 0.000001:  # parabolic orbits
        h = cross(r0, v0)  # cross product of vectors r0 and v0
        hmag = mag(h)  # magnitude of the h vector
        p = hmag / u
        s = np.arctan(1 / (3. * np.sqrt(u / (p ** 3)) * t)) / 2.
        w = np.arctan(np.tan(s) ** (1 / 3.))
        s0 = np.sqrt(p) * 2. * np.tan(1 / (2. * w))

    if alpha < -0.000001:  # hyperbolic orbits
        a = 1. / alpha
        s0 = np.sign(t) * np.sqrt(-a) * np.log(-2. * u * alpha * t / (r0.dot(v0) + np.sign(t) *
                                                                      np.sqrt(-u * a) * (1 - r0mag * alpha)))

    # Newton-Raphson solver:

    err = np.inf
    dr0v0 = r0.dot(v0) / u2
    u2t = u2 * t
    i, s, c2, c3 = 0, 0, 0, 0

    while np.any(abs(err) > tol) and i < 25:
        s2 = s0 * s0  # s^2
        s3 = s2 * s0  # s^3
        psi = s2 * alpha  # alpha * s^2

        c2, c3 = c2c3(psi)  # Stumpff functions

        s0psic3 = s0 * (1.0 - psi * c3)
        s2c2 = s2 * c2

        r = s2c2 + dr0v0 * s0psic3 + r0mag * (1 - psi * c2)  # f'(s)

        s = s0 + (u2t - s3 * c3 - dr0v0 * s2c2 - r0mag * s0psic3) / r  # old value + f(s)/f'(s)

        err = s - s0  # convergence check
        s0 = s

        i += 1

    # identify non-converging array entries and remove them:

    del2 = np.where(abs(err) > tol)
    s, c2, c3, t = np.delete(s, del2), np.delete(c2, del2), np.delete(c3, del2), np.delete(t, del2)

    # calculate final coefficients:

    f = 1 - (s * s) * c2 / r0mag
    g = t - (s * s * s) * c3 / u2

    # calculate final path prediction:

    r2 = np.array(r0.astuple())  # convert vPython vectors to numpy arrays
    v2 = np.array(v0.astuple())

    path = r2 * f[:, None] + v2 * g[:, None]  # (changing shape to enable numpy broadcasting)

    dst = cdist(path, [[0, 0, 0]])  # compute distance of all points in the path from the origin

    # draw path:

    trailer.trail.color = color.green  # default color (green)

    if np.any(dst <= sun_radius):

        trailer.trail.color = color.red  # turn path RED, if collision detected
        trailer.trail.pos = path[0:np.argmax(dst <= sun_radius)]  # draw path only up to the Sun collision point

    else:
        trailer.trail.pos = path  # update full path

    return trailer
