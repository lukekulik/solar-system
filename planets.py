from vis import materials
from math import pi
from os import getcwd
from os.path import join


def mat_ini(name):  # function initializing textures
    name = join(join(getcwd(), "textures"), name)  # textures folder
    mat = materials.texture(data=materials.loadTGA(name), mapping="spherical")
    return mat

# textures for celestial bodies other than planets:
# textures from https://github.com/nddrylliog and http://3dmoddeling.blogspot.nl

sun_mat = mat_ini("sun3")  # sun spots material
stars_mat = mat_ini("starX")  # stellar sphere material
death_star = mat_ini("death_star")  # spaceship texture
ring_mat = materials.texture(data=materials.loadTGA(join(join(getcwd(), "textures"), "sat_ring")),
                             mapping="cubic")  # saturn rings material
ring2_mat = materials.texture(data=materials.loadTGA(join(join(getcwd(), "textures"), "uranus_ring")),
                              mapping="cubic")  # uranus rings material


# dictionaries with planet parameters (lengths in km, inclinations w.r.t. plane of the ecliptic, spin in rad/h):
# (it is enough to enter new celestial body parameters in this file for it to appear in the simulation)

mercury = {'a': 57909050.,
           'e': 0.205630,
           'inclination': 7 * pi / 180.,
           'right_ascension': 0.8436854966,
           'mean_anomaly': 3.0507657193,
           'radius': 2439.7,
           'tilt': 0.1 * pi / 180.,
           'spin': 2 * pi / 4222.6,
           'material': mat_ini("mercury"),
           'name': "Mercury"}

venus = {'a': 108208000.,
         'e': 0.0067,
         'inclination': 3.39 * pi / 180.,
         'right_ascension': 1.3381895772,
         'mean_anomaly': 0.8746717546,
         'radius': 6051.8,
         'tilt': 177 * pi / 180.,
         'spin': -2 * pi / 2802.,
         'material': mat_ini("venus"),
         'name': "Venus"}

earth = {'a': 149598261.,
         'e': 0.01671123,
         'inclination': 0.,
         'right_ascension': 0.,
         'mean_anomaly': 6.2398515744,
         'radius': 6378.,
         'tilt': 23 * pi / 180.,
         'spin': 2 * pi / 24.,
         'material': mat_ini("earth"),
         'name': "Earth"}

mars = {'a': 227939100.,
        'e': 0.093315,
        'inclination': 1.85 * pi / 180.,
        'right_ascension': 0.8676591934,
        'mean_anomaly': 0.3378329113,
        'radius': 3393.5,
        'tilt': 25 * pi / 180.,
        'spin': 2 * pi / 24.66,
        'material': mat_ini("mars"),
        'name': "Mars"}

jupiter = {'a': 778547200.,
           'e': 0.048775,
           'inclination': 1.31 * pi / 180.,
           'right_ascension': 1.7504400393,
           'mean_anomaly': 0.3284360586,
           'radius': 71400.,
           'tilt': 3 * pi / 180.,
           'spin': 2 * pi / 9.93,
           'material': mat_ini("jupiter"),
           'name': "Jupiter"}

saturn = {'a': 1433449370.,
          'e': 0.055723219,
          'inclination': 2.49 * pi / 180.,
          'right_ascension': 1.98,
          'mean_anomaly': 5.5911055356,
          'radius': 60000.,
          'tilt': 27 * pi / 180.,
          'spin': 2 * pi / 10.66,
          'material': mat_ini("saturn"),
          'name': "Saturn"}

uranus = {'a': 2876679082.,
          'e': 0.044405586,
          'inclination': 0.77 * pi / 180.,
          'right_ascension': 1.2908891856,
          'mean_anomaly': 2.4950479462,
          'radius': 25600.,
          'tilt': 98 * pi / 180.,
          'spin': -2 * pi / 17.24,
          'material': mat_ini("uranus"),
          'name': "Uranus"}

neptune = {'a': 4503443661.,
           'e': 0.011214269,
           'inclination': 1.77 * pi / 180.,
           'right_ascension': 2.3001058656,
           'mean_anomaly': 4.6734206826,
           'radius': 24300.,
           'tilt': 30 * pi / 180.,
           'spin': 2 * pi / 16.11,
           'material': mat_ini("neptune"),
           'name': "Neptune"}

#all of the planets have to be listed in the active planet list below:
planet_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
