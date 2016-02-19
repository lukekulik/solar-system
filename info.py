from vis import label, mag, mag2
from planets import planet_list
from parameters import u, n, f, obj_global, a_global, eps_global, name_global, radius_global

# planet/spaceship label definition:
popup = label(visible=False, box=False, xoffset=-50, yoffset=50, font='sans', opacity=0.4)


def lbl(popup, obj, sw_lbl, dt):
    # global variables for comparison between function calls
    global obj_global, a_global, eps_global, name_global, radius_global

    err = 1e20  # large number for error comparison in the for loop below

    r0mag = mag(obj.pos)  # computing the instantaneous distance from the Sun

    if r0mag == 0:  # turning off the planet label if the clicked object is centered at the origin (i.e. Sun, stars)
        sw_lbl = not sw_lbl
        return popup, sw_lbl

    if obj_global != obj:  # execute only if new object was chosen

        # looking through the planet list searching for the closest value for semi major axis for the selected object:

        for planet in planet_list:
            if (abs(planet['a'] - r0mag)) < err:
                err = (abs(planet['a'] - r0mag))  # assign new closest value

                a_global = planet['a']  # assign semi-major axis
                name_global = planet['name']  # assign planet name
                radius_global = planet['radius']  # assign planet radius
                eps_global = -u / (2 * a_global)  # compute specific orbital energy

        obj_global = obj  # assign new object as already labeled

    v0mag = (2 * (eps_global + u / r0mag)) ** 0.5  # velocity calculation using specific orbital energy

    popup.pos = obj.pos  # update label position to overlap with planet position

    # update label text with new data:
    popup.text = str(name_global) + \
                 "\nRadius: " + str(radius_global) + " km" + \
                 "\nDistance from the Sun: " + str(int(round(r0mag))) + " km (" + str(
        round(r0mag / 149598261, 2)) + " AU)" + \
                 "\nOrbital Velocity: " + str(round(v0mag, 2)) + " km/s" + \
                 "\nTime scale: 1 s =  " + str(round(f * dt * 365.25 * 86400 / (3600. * n), 3)) + "hrs"

    popup.visible = True

    return popup, sw_lbl


def lbl_ship(popup, obj, s, v, a):
    # get magnitudes of distance from the Sun, velocity and acceleration:
    r0mag = mag(s)
    v0mag = mag(v)
    a0mag = mag(a) * 1e6  # converted from km/s^2 to m/s^2

    eps = mag2(v) / 2 - u / r0mag  # compute specific orbital energy

    popup.pos = obj.pos  # update label position to overlap with spaceship position

    # update label text with new data:
    popup.text = "Spaceship!" + \
                 "\nAcceleration: " + str(a) + \
                 "\nSpecific orbital energy: " + str(eps) + " MJ/kg" + \
                 "\nDistance from the Sun: " + str(int(round(r0mag))) + " km (" + str(
        round(r0mag / 149598261, 2)) + " AU)" + \
                 "\nEngine Acceleration: " + str(round(a0mag, 2)) + " m/s^2" + \
                 "\nOrbital Velocity: " + str(round(v0mag, 2)) + " km/s"

    popup.visible = True

    return popup