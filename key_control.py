from vis import scene, label, vector, norm, cross
#from pygame.mixer import music
from parameters import planets, n, am
from wx import Exit

lbl = label(text="    Simulation is paused. \n Press any key to continue.", visible=False, box=False)

# key_check function translates user keyboard into commands for the program:


def key_check(ship_mode, s, v, a, dt, sw_lbl, lbl_off, predraw, earthpos, t, ship):
    if scene.kb.keys:  # check if there are any keys pressed in the queue

        key = scene.kb.getkey()  # retrieve the pressed key

        # change simulation speed: (steps are small on purpose; user has to press and hold for smooth transition)
        if key == 'q' and 1 <= dt < 125:
            dt += 2
        elif key == 'q' and dt <= 0.95:
            dt += 0.05
        elif key == 'a' and dt > 1:
            dt -= 2
        elif key == 'a' and 0.2 < dt <= 1:
            dt -= 0.05

        elif key == 'esc':
            Exit()  # exit the program

        elif key == 'p':
            lbl.visible = True  # show pause label
            lbl.pos = scene.center  # center the label on the screen
            scene.kb.getkey()  # wait for key input
            lbl.visible = False  # hide pause label

        elif key == 'x':
            if scene.stereo == 'nostereo':
                scene.stereo = 'redcyan'  # turn on 3D rendering mode (red-cyan)
            elif scene.stereo == 'redcyan':
                scene.stereo = 'crosseyed'  # turn on 3D rendering mode (cross-eyed)
            else:
                scene.stereo = 'nostereo'  # turn off 3D rendering mode

        elif key == 'l':
            sw_lbl = not sw_lbl  # planet/spaceship label switch
            lbl_off = not lbl_off

        elif key == 's':
            #if ship_mode:
 #               music.fadeout(2500) # fade out music when quitting spaceship mode
#            else:
#                music.play(-1)   # turn on music when entering spaceship mode

            ship_mode = not ship_mode  # spaceship mode switch
            a = vector(0, 0, 0)  # reset acceleration
            sw_lbl = True  # turn on spaceship label

        # spaceship thrusters control:

        elif key == 'up':
            #a += vector(0, 0, am)  # old cartesian steering
            a += am*norm(v)  # accelerate into the direction of motion
        elif key == 'down':
            a -= am*norm(v)  # accelerate against the direction of motion
        elif key == 'left':
            a -= am*cross(norm(v),cross(norm(v),norm(s)))   # accelerate to the left of the velocity

        elif key == 'right':
            a += am*cross(norm(v),cross(norm(v),norm(s)))  # accelerate to the right of the velocity
        elif key == 'd':
            a += am*cross(norm(v),norm(s))  # accelerate to the 'top' of the velocity
        elif key == 'c':
            a -= am*cross(norm(v),norm(s))   # accelerate to the 'bottom' of the velocity
        elif key == '0':
            a = vector(0, 0, 0)  # reset acceleration

        # pre-programmed spaceship positions/scenarios:

        elif key == '1':  # Earth-Sun Lagrange point 3 (L3 - 'counter-Earth')
            s = -earthpos
            v0 = (planets[2][1][:, (int(-t + 1)) % n] - planets[2][1][:, (int(-t)) % n]) / (365.25 * 86400 / n)
            v = vector(v0[0], v0[1], v0[2])
            a = vector(0, 0, 0)
            predraw = False
            ship.trail.append(pos=s, retain=1)

        elif key == '2':  # polar orbit around the Sun
            s = vector(3e+07, -2e+06, 2e+08)
            v = vector(0, 24, 0)
            a = vector(0, 0, 0)
            predraw = False
            ship.trail.append(pos=s, retain=1)

        elif key == '3':  # orbit of the probe Helios 2  (fastest man-made object to date - 0.02% speed of light)
            s = vector(43e6, 0, 0)  # perihelion
            v = vector(0, 0, 70.22)
            a = vector(0, 0, 0)
            predraw = False
            ship.trail.append(pos=s, retain=1)

        elif key == '4':  # Halley's comet (derived using specific orbital energy, 162.3 deg inclination)
            s = vector(87813952, 0, 0)  # perihelion
            v = vector(0, 16.7, 52)
            a = vector(0, 0, 0)
            predraw = False
            ship.trail.append(pos=s, retain=1)

    return ship_mode, s, v, a, dt, sw_lbl, lbl_off, predraw, ship


def mouse_check(obj, sw_lbl, lbl_off, ship_mode):
    if scene.mouse.clicked and not ship_mode:  # check if there are any clicks in the queue

        scene.mouse.getclick()  # retrieve the click
        obj_old = obj
        obj = scene.mouse.pick  # clicked object becomes main object

        try:
            r = obj.radius
        except AttributeError:
            obj = obj_old  # if the clicked object is not a sphere (e.g. Saturn's rings), go back to old_obj
        else:
            if r > 30000000000:  # if the clicked object is a very large sphere (celestial), go back to old_obj
                obj = obj_old

        if obj != obj_old and not lbl_off:  # if different planet was clicked, switch planet label ON
            sw_lbl = True

    scene.center = obj.pos  # center scene on the main object

    return obj, sw_lbl
