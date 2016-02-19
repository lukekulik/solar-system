from vis import materials
from math import pi
from os import getcwd
from os.path import join


moon_mat = materials.texture(data=materials.loadTGA(join(join(getcwd(), "textures"), "moon")),
                             mapping="spherical")  # moon material - same for all of them

ScaleMoon = 300  # scaling factor for semi major axes of some moons

# moons have arbitrary scale factors applied to semi major axis and radius to make them properly visible

# dictionaries with moon parameters (lengths in km, inclinations w.r.t. plane of the ecliptic, spin in rad/h, \
# planet numbers from 0, tidal lock - 0/1, only including moons with radius > 500km,):

luna = {'a': 384399 * 50.,
        'e': 0.0549,
        'inclination': (-23.4 + 5.145) * pi / 180.,
        'right_ascension': -pi / 2.,
        'mean_anomaly': 0.,
        'radius': 1737.1,
        'tilt': 0.02691995838,
        'spin': 2 * pi / 708.7341666667,
        'material': moon_mat,
        'period': 27.321,
        'planet_name': "Earth",
        'planet_num': 2,
        'tidal_lock': 1}

phobos = {'a': 9376 * 1000,
          'e': 0.0151,
          'inclination': 0,
          'right_ascension': -pi / 2,
          'mean_anomaly': 0.,
          'radius': 11.2667 * 10,
          'tilt': 0.,
          'spin': 0,
          'material': moon_mat,
          'period': 0.31891023,
          'planet_name': "Mars",
          'planet_num': 3,
          'tidal_lock': 1}

deimos = {'a': 23463.2 * 650.,
          'e': 0.00033,
          'inclination': 0,
          'right_ascension': -pi / 2,
          'mean_anomaly': 0.,
          'radius': 10. * 10,
          'tilt': 0.,
          'spin': 0,
          'material': moon_mat,
          'period': 1.263,
          'planet_name': "Mars",
          'planet_num': 3,
          'tidal_lock': 1}

callisto = {'a': 1882700 * ScaleMoon / 2,
            'e': 0.0074,
            'inclination': 0.003351032164,
            'right_ascension': 0.,
            'mean_anomaly': 0.,
            'radius': 2410.3,
            'tilt': 0.,
            'spin': 0,
            'material': moon_mat,
            'period': 16.689,
            'planet_name': "Jupiter",
            'planet_num': 4,
            'tidal_lock': 1}

europa = {'a': 670900 * ScaleMoon,
          'e': 0.009,
          'inclination': 0.008203047484,
          'right_ascension': 0.,
          'mean_anomaly': 0.,
          'radius': 1560.8,
          'tilt': 0.,
          'spin': 0,
          'material': moon_mat,
          'period': 12.689,
          'planet_name': "Jupiter",
          'planet_num': 4,
          'tidal_lock': 1}

ganymede = {'a': 1070400 * ScaleMoon,
            'e': 0.0013,
            'inclination': 0.003490658504,
            'right_ascension': 0.,
            'mean_anomaly': 0.,
            'radius': 2634.1,
            'tilt': 0.,
            'spin': 0,
            'material': moon_mat,
            'period': 10.689,
            'planet_name': "Jupiter",
            'planet_num': 4,
            'tidal_lock': 1}

io = {'a': 421800 * ScaleMoon * 1.5,
      'e': 0.0041,
      'inclination': 0.03857177647,
      'right_ascension': 0.,
      'mean_anomaly': 0.,
      'radius': 1821.6,
      'tilt': 0.,
      'spin': 0,
      'material': moon_mat,
      'period': 6.689,
      'planet_name': "Jupiter",
      'planet_num': 4,
      'tidal_lock': 1}

dione = {'a': 377396 * 3 * ScaleMoon,
         'e': 0.0022,
         'inclination': 0,
         'right_ascension': -pi / 2.,
         'mean_anomaly': 0.,
         'radius': 561.4 * 3,
         'tilt': 0.,
         'spin': 0,
         'material': moon_mat,
         'period': 7.689,
         'planet_name': "Saturn",
         'planet_num': 5,
         'tidal_lock': 1}

enceladus = {'a': 237948 * 3 * ScaleMoon,
             'e': 0.0047,
             'inclination': 0,
             'right_ascension': -pi / 2.,
             'mean_anomaly': 0.,
             'radius': 252.1 * 3,
             'tilt': 0.,
             'spin': 0,
             'material': moon_mat,
             'period': 16.689,
             'planet_name': "Saturn",
             'planet_num': 5,
             'tidal_lock': 1}

tethys = {'a': 294619 * 3 * ScaleMoon,
          'e': 0.,
          'inclination': 0,
          'right_ascension': -pi / 2.,
          'mean_anomaly': 0.,
          'radius': 531.1 * 3,
          'tilt': 0.,
          'spin': 0,
          'material': moon_mat,
          'period': 1.689,
          'planet_name': "Saturn",
          'planet_num': 5,
          'tidal_lock': 1}

titan = {'a': 1221870 * ScaleMoon,
         'e': 0.0288,
         'inclination': 0,
         'right_ascension': -pi / 2.,
         'mean_anomaly': 0.,
         'radius': 2576.,
         'tilt': 0.,
         'spin': 0,
         'material': moon_mat,
         'period': 61.689,
         'planet_name': "Saturn",
         'planet_num': 5,
         'tidal_lock': 1}

ariel = {'a': 191020 * ScaleMoon,
         'e': 0.0012,
         'inclination': 0,
         'right_ascension': -pi / 2.,
         'mean_anomaly': 0.,
         'radius': 578.9,
         'tilt': 0.,
         'spin': 0,
         'material': moon_mat,
         'period': 16.689,
         'planet_name': "Uranus",
         'planet_num': 6,
         'tidal_lock': 1}

oberon = {'a': 583520 * ScaleMoon,
          'e': 0.0014,
          'inclination': 0.,
          'right_ascension': -pi / 2.,
          'mean_anomaly': 0.,
          'radius': 761.4,
          'tilt': 0.,
          'spin': 0,
          'material': moon_mat,
          'period': 6.689,
          'planet_name': "Uranus",
          'planet_num': 6,
          'tidal_lock': 1}

titania = {'a': 435910 * ScaleMoon,
           'e': 0.0011,
           'inclination': 0,
           'right_ascension': -pi / 2.,
           'mean_anomaly': 0.,
           'radius': 788.4,
           'tilt': 0.,
           'spin': 0,
           'material': moon_mat,
           'period': 1.689,
           'planet_name': "Uranus",
           'planet_num': 6,
           'tidal_lock': 1}

umbriel = {'a': 266000 * ScaleMoon,
           'e': 0.0039,
           'inclination': 0,
           'right_ascension': -pi / 2.,
           'mean_anomaly': 0.,
           'radius': 584.7,
           'tilt': 0.,
           'spin': 0,
           'material': moon_mat,
           'period': 24.689,
           'planet_name': "Uranus",
           'planet_num': 6,
           'tidal_lock': 1}

triton = {'a': 354759 * ScaleMoon,
          'e': 0.,
          'inclination': 0.,
          'right_ascension': -pi / 2.,
          'mean_anomaly': 0.,
          'radius': 1353.4,
          'tilt': 0.,
          'spin': 0,
          'material': moon_mat,
          'period': 16.689,
          'planet_name': "Neptune",
          'planet_num': 7,
          'tidal_lock': 1}

# all of the displayed moons have to be listed in the active moons list below:

moon_list = [luna, phobos, deimos, callisto, europa, ganymede, io, dione, enceladus, tethys, titan, ariel, oberon,
             titania, umbriel, triton]