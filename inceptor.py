from planets import earth
from vis import sphere, curve, color  # vPython tools
from raphson import orbit  # orbital calculator


def planet_ini(planetdata, n, scale_up):  # retrieves data from planet dictionary and creates a planet

    a = planetdata['a']  # semi-major axis
    tilt = planetdata['tilt']
    timescale = (a / earth['a']) ** 1.5  # rotation period w.r.t. Earth
    spin = 365.25 * 24 * planetdata['spin'] / n  # rotation rate

    celestial = sphere(radius=planetdata['radius'] * scale_up, material=planetdata['material'],
                       trail=curve(color=color.white))  # create an object using vPython class 'sphere'
    celestial.rotate(angle=tilt, axis=(0, 0, 1))  # tilt the planet

    coord = orbit(planetdata['mean_anomaly'], planetdata['e'], a, planetdata['inclination'],
                  planetdata['right_ascension'], n)  # create orbit coordinates list for the planet

    return [celestial, coord, timescale, a, tilt, spin]  # return a list with entries used in simulation


def moon_ini(moondata, planets, n, scale_up):  # retrieves data from moon dictionary and creates a moon

    tilt = moondata['tilt']
    moonscale = moondata['period'] / 365.25  # rotation period w.r.t Earth
    spin = 365 * 24 * moondata['spin'] / n  # rotation rate
    lock = moondata['tidal_lock']

    celestial = sphere(radius=moondata['radius'] * scale_up,
                       material=moondata['material'])  # create an object using vPython class 'sphere'

    mooncoord = orbit(moondata['mean_anomaly'], moondata['e'], moondata['a'],
                      planets[moondata['planet_num']][4] + moondata['inclination'],
                      moondata['right_ascension'], n)  # create orbit coordinates list for the moon

    planetcoord = planets[moondata['planet_num']][1]  # retrieve associated planet data
    planetscale = planets[moondata['planet_num']][2]  # retrieve associated planet rotation period w.r.t Earth

    return [celestial, planetcoord, mooncoord, planetscale, moonscale, tilt,
            spin, lock]  # return a list with entries used in simulation