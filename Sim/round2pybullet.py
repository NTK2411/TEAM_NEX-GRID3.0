import pybullet as p
import pybullet_data
import cv2
import numpy as np
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-15)
p.loadURDF('rsc/plane.urdf',[0,0,-0.1], useFixedBase=1)
p.configureDebugVisualizer(p.COV_ENABLE_WIREFRAME, 0)
p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0)

arena_size = 14
cover_plates = [None] * (arena_size ** 2)
def load_arena():
    """
    Function to load the arena
    """
    # arena = np.random.randint(low = 0, high = 6, size=(9, 9))
    # Arena reference
    # 0 -> black base
    # 1 -> light green base
    # 2 -> blue base
    # 3 -> red base
    # 4 -> purple base
    # 5 -> yellow base
    # 6 -> white base
    # 7 -> dark green base
    arena = np.array([
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 5, 5, 6, 6, 5, 5, 6, 6, 5, 5, 6, 6],
        [6, 6, 5, 5, 6, 6, 5, 5, 6, 6, 5, 5, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 5, 5, 6, 6, 5, 5, 6, 6, 5, 5, 6, 6],
        [6, 6, 5, 5, 6, 6, 5, 5, 6, 6, 5, 5, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 5, 5, 6, 6, 5, 5, 6, 6, 5, 5, 6, 6],
        [6, 6, 5, 5, 6, 6, 5, 5, 6, 6, 5, 5, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    ])

    base_plate_dict = {
        1: 'rsc/base plate/base plate green.urdf',
        2: 'rsc/base plate/base plate cyan.urdf',
        3: 'rsc/base plate/base plate red.urdf',
        4: 'rsc/base plate/base plate purple.urdf',
        5: 'rsc/base plate/base plate yellow.urdf',
        6: 'rsc/base plate/base plate white.urdf',
        7: 'rsc/base plate/base plate darkgreen.urdf',
        # 1: 'rsc/base plate/base plate blue.urdf',
    }

    def get_base_plate_position(i, j):
        return [(arena_size / 2 - 0.5)-i*1,(arena_size / 2 - 0.5)-j*1,0]

    for i in range(arena_size):
        for j in range(arena_size):
            if arena[i, j] == 0:
                continue
            p.loadURDF(base_plate_dict[arena[i, j]], get_base_plate_position(i, j), p.getQuaternionFromEuler([0, 0, 0]), useFixedBase=1)
    for i in (-1,0,1):
        for j in (-1,0,1):
            p.loadURDF('rsc/boundary.urdf',[4*i,4*j,-0.1], useFixedBase=1)
    print("Namaste")
load_arena()

p.stepSimulation()
time.sleep(10)