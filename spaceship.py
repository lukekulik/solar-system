from vis import vector, mag, mag2, norm
from parameters import u, sun_radius, star_radius, s0, v0, a0


def ship(s, v, a, dt, spaceship, predraw):
    dst = vector(0, 0, 0) - s  # computing spaceship - Sun distance vector
    gravity_acc = (u / (mag2(dst))) * norm(dst)  # computing gravity force

    v += (gravity_acc + a) * dt  # numerical integration of velocity
    s += v * dt  # numerical integration of position

    spaceship.pos = s  # assigning new position to the spaceship
    spaceship.trail.append(pos=s, retain=2000)  # appending spaceship trail with new position

    # recovers the spaceship to the initial position in case of crashing into the Sun or going out of range:

    if star_radius <= mag(s) or mag(s) <= sun_radius:
        spaceship.pos = s0
        spaceship.trail.pos = []    # clear the trail
        s, v, a = vector(s0.astuple()), vector(v0.astuple()), vector(a0.astuple())  # assign initial values
        predraw = False  # redraw the orbital prediction

    return s, v, a, predraw
