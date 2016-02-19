from vis import rate, vector  # importing vPython module
# from pygame.mixer import music, init  # importing PyGame music module
from graphics import camera  # importing vPython with predefined settings
from key_control import key_check, mouse_check  # importing keyboard and mouse control module
from spaceship import ship  # importing variable orbit simulator
from uvf import position  # importing orbit predictor from variable orbit simulator
from info import lbl, lbl_ship, popup  # importing planet label generator
from update import planet_update, moon_update  # importing position-updating functions
from parameters import running, f, spaceship, times, sun, saturn_ring, uranus_ring, dt, planets, moons, n, \
    ship_mode, sw_lbl, lbl_off, s0, v0, a0, predraw, trailer, obj, t
# importing variables, lists, planets and moons

# init()  # initializing PyGame music mixer module
# music.load("danube.mp3")  # loading The Blue Danube Waltz by Johann Strauss

s, v, a = vector(s0.astuple()), vector(v0.astuple()), vector(a0.astuple())

while running:
    rate(f)  # ensures a steady rate of simulation on all computers

    # checking keyboard input:
    ship_mode, s, v, a, dt, sw_lbl, lbl_off, predraw, spaceship = key_check(ship_mode, s, v, a, dt, sw_lbl, lbl_off,
                                                                            predraw, planets[2][0].pos, t, spaceship)

    # spaceship coordinates update:
    s, v, a, predraw = ship(s, v, a, dt * 365.25 * 86400 / n, spaceship, predraw)

    if ship_mode:

        obj = spaceship # set spaceship as the main object

        if sw_lbl:
            popup = lbl_ship(popup, spaceship, s, v, a)  # spaceship data label update
        else:
            popup.visible = False  # hiding spaceship label if it was switched off by the user

        if (a.mag != 0) or not predraw:
            trailer = position(s, v, times, trailer)  # orbital path prediction update
            predraw = True

    elif obj == spaceship:  # switching back to heliocentric model if spaceship not active
        obj = sun

    else:
        trailer.trail.pos = []  # clear orbit prediction trail
        spaceship.trail.pos = []    # clear spaceship trail
        predraw = False # set predraw orbit prediction switch to false

    for planet in planets:  # planets coordinates update
        planet_update(planet, t, dt, n)
    for moon in moons:  # moons coordinates update
        moon_update(moon, t, dt, n)

    saturn_ring.pos = planets[5][0].pos  # saturn's rings coordinates update
    uranus_ring.pos = planets[6][0].pos  # uranus rings coordinates update

    obj, sw_lbl = mouse_check(obj, sw_lbl, lbl_off, ship_mode)  # checking mouse input

    if sw_lbl and not ship_mode:
        popup, sw_lbl = lbl(popup, obj, sw_lbl, dt)  # planet label update
    elif popup.visible and not ship_mode:
        popup.visible = False  # hiding planet label if it was switched off by the user

    if t < 6000:
        camera()  # initial camera movement

    t += dt

    if t >= 1e20:  # orbital reset, to prevent the counter from going to infinity
        t = 0
        for planet in planets:  # removing the trail of all the planets
            planet[0].trail.append(pos=planet[1][:, 0], retain=0)
