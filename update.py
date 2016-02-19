from numpy import sin, cos, arccos
from vis import *


def planet_update(planetlist, t, dt, n):  # function updating the position of planets

    # assign a position from coordinates list - entire row based on time elapsed from the start of the
    # last period (%n), scaled w.r.t. Earth's period:

    planetlist[0].pos = (planetlist[1][:, (int(-t / planetlist[2])) % n])

    # append planet trail with the recent position; number of points retained is proportional to semi-major axis:

    planetlist[0].trail.append(pos=planetlist[0].pos, retain=int(1.5e-9 * planetlist[3] ** 1.55 / dt))

    # rotate a planet by the increment corresponding to the time elapsed, around its tilted axis:

    planetlist[0].rotate(angle=planetlist[5] * dt, axis=(-sin(planetlist[4]), cos(planetlist[4]), 0))

    return 0


def moon_update(moonlist, t, dt, n):  # function updating the position of moons

    # assign a position from coordinates list - entire row based on time elapsed from the start of the
    # last period (%n), scaled w.r.t. Earth's period added to associated planet position at given time:

    moonlist[0].pos = moonlist[1][:, (int(-t / moonlist[3])) % n] + moonlist[2][:, (int(-t / moonlist[4])) % n]
    # first term - associated planet position, second term - moon position

    # tidal locking mechanism (calculates the change in the direction of the velocity vector and
    # rotates the moon accordingly):

    # moon velocity at time t w.r.t. its planet: (based on the change in position)
    vel_vect0 = vector(
        moonlist[2][:, (int(-(t + dt) / moonlist[4])) % n] - moonlist[2][:, (int(-(t) / moonlist[4])) % n])

    # moon velocity at time t+1 w.r.t. its planet: (based on the change in position)
    vel_vect1 = vector(
        moonlist[2][:, (int(-(t + 2 * dt) / moonlist[4])) % n] - moonlist[2][:, (int(-(t + dt) / moonlist[4])) % n])

    v0n, v1n = norm(vel_vect0), norm(vel_vect1)  # normalize velocity vectors
    cx = v0n.dot(v1n)  # take dot product of velocity vectors
    d1 = arccos(cx)  # angle in radians between two moon velocity vectors

    # planet velocity at time t w.r.t. Sun: (based on the change in position)
    vel_vect2 = vector(
        moonlist[1][:, (int(-(t + dt) / moonlist[3])) % n] - moonlist[1][:, (int(-(t) / moonlist[3])) % n])

    # planet velocity at time t+1 w.r.t. Sun: (based on the change in position)
    vel_vect3 = vector(
        moonlist[1][:, (int(-(t + 2 * dt) / moonlist[3])) % n] - moonlist[1][:, (int(-(t + dt) / moonlist[3])) % n])

    v2n, v3n = norm(vel_vect2), norm(vel_vect3)  # normalize velocity vectors
    cx2 = v2n.dot(v3n)  # take dot product of velocity vectors
    d2 = arccos(cx2)  # angle in radians between two planet velocity vectors

    if d2 > 1:  # protection against d2 becoming a large number if planet velocity does not change in given time step
        d2 = 0

    # rotate a moon by the increment corresponding to the time elapsed, around its tilted axis:
    moonlist[0].rotate(angle=(d1 - d2) * moonlist[7], axis=(-sin(moonlist[5]), cos(moonlist[5]), 0))

    return 0
