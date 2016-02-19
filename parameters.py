from numpy import arange
from vis import vector, box, color, curve, materials, sphere  # 3d objects classes
from planets import planet_list, saturn, uranus, ring_mat, ring2_mat, sun_mat, stars_mat, \
    death_star  # orbit data the planets
from moons import moon_list  # orbit data for the moons
from inceptor import moon_ini, planet_ini  # moons and planets constructor


# main simulation parameters:
running = True
ScaleUp = 2000  # scaling factor for planets and moons radii
t = 0  # time counter
dt = 1  # initial time step
n = 10000  # number of orbit coordinates generated (affects temporal accuracy - dt(real)=365.25*86400/n (in seconds))
f = 40  # vPython simulation rate in 1/f seconds, ensures constant timing on all computers
planets = []  # planets list
moons = []  # moons list
sw_lbl = False  # planet label switch 1
lbl_off = False  # planet label switch 2
obj_global, a_global, eps_global, name_global, radius_global = 0, 0, 0, 0, 0  # variables for label function calls

# spaceship simulation parameters:
ship_mode = False  # switch for turning on spaceship control
predraw = False  # switch that ensures that the spaceship path will be drawn when it is activated
u = 132712440018.1  # Sun gravitational parameter
am = 1.5e-6  # acceleration increment in km/s^2
n_pred = 800 + 1  # number of data points in the orbit prediction (affects speed of the simulation)
t_pred = 200000  # temporal shift of data points in the orbit prediction (in seconds)
times = arange(1, n_pred) * t_pred  # array with input for orbit predictor

# constructing spaceship and orbit predictor:
spaceship = sphere(radius=1000000, trail=curve(color=color.white), material=death_star, color=(0.5, 0.5, 0.5))
trailer = box(length=1, height=1, width=1, trail=curve())

# initial attitude of the spaceship (in km):
s0 = vector(3e+07, -2e+06, 2e+08)
v0 = vector(-17, 0, 14)
a0 = vector(0, 0, 0)

# initializing unique (one-off) bodies:
sun = sphere(radius=695500 * 40, color=color.yellow, material=materials.emissive)  # radius in km
sun2 = sphere(radius=695500 * 40, material=sun_mat, opacity=0.7)  # applying Sun spots
stars = sphere(radius=30066790000, material=stars_mat)  # constructing a stellar sphere

obj = sun  # declaring Sun as the object in the center of the scene
sun_radius = sun.radius # constant required by external modules

for planet in planet_list:  # constructing planets list
    planets.append(planet_ini(planet, n, ScaleUp))

for moon in moon_list:  # constructing moons list (has to be initialized after the planets)
    moons.append(moon_ini(moon, planets, n, ScaleUp))

star_radius=planets[-1][3]*0.25  # maximum range for the spaceship (semi major axis of the last planet)

# constructing rings of Saturn and Uranus:
saturn_ring = box(length=planets[5][0].radius + 180000 * ScaleUp, height=1,
                  width=planets[5][0].radius + 180000 * ScaleUp, material=ring_mat)
saturn_ring.rotate(angle=saturn['tilt'], axis=(0, 0, 1))  # tilt corresponding to planet tilt

uranus_ring = box(length=planets[6][0].radius + 70000 * ScaleUp, height=1,
                  width=planets[6][0].radius + 70000 * ScaleUp, material=ring2_mat)
uranus_ring.rotate(angle=uranus['tilt'], axis=(0, 0, 1))  # tilt corresponding to planet tilt