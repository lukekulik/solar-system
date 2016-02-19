from vis import scene, local_light, color, vector


# scene parameters and settings:

scene.x, scene.y = 250, 80  # centering the window (optimized for SXGA displays)
scene.width, scene.height = 800, 600
scene.title = "Solar System"
scene.lights = []
scene.ambient = 0.4  # turning off default lights and turning on some ambient light and the Sun
scene.forward = (2, -1, -2)
lamp = local_light(pos=(0, 0, 0), color=color.white)  # setting the scene
scene.autoscale = False
scene.scale = (0.000000001, 0.000000001, 0.000000001)
scene.fov = 0.8  # field of view

scene_old = vector(scene.forward.astuple())


def camera():  # initial camera movement
    global scene_old

    if scene_old==scene.forward:    # stop when user rotates -> scene.forward changes
        scene.forward = (scene.forward[0] + 6 / 3000., scene.forward[1] - 4 / 5000., scene.forward[2])
        scene_old=vector(scene.forward.astuple())

    # scene.scale = (scene.scale[0] + 6 * 2e-13, scene.scale[1] + 6 * 2e-13, scene.scale[2] + 6 * 2e-13)

    return 0
