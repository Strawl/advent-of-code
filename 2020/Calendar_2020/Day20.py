import math
import numpy as np


def check_squares(tile, tile2):
    if np.array_equal(tile[-1], tile2[0]):
        return 1
    if np.array_equal(tile[0], tile2[-1]):
        return -1
    return 0

    """print(tile)
    print()
    print(np.rot90(tile,1,(0,1))) #rotateleft
    print()
    print(np.flip(tile,0)) # Y Achse
    print()
    print(np.flip(tile, 1)) # X Achse"""


def task_1():
    with open("Input/20.txt") as f:
        data = [x.split(":\n") for x in f.read().split("\n\n")]
        data = [[x.split("\n") for x in y] for y in data]
        for t in data:
            t[0] = int(t[0][0].split(" ")[1])
        [[print(x) for x in y] for y in data]
        length = len(data) ** 0.5
        current_grid = np.zeros((int(length), int(length)))
        space = np.zeros((int(length), int(length), 10, 10))
        for i, d in enumerate(data):
            current_grid[int(math.floor(i / length)), int(i % length)] = d[0]
            for idx, x in enumerate(d[1]):
                for idy, y in enumerate(x):
                    if y == "#":
                        space[int(math.floor(i / length)), int(i % length), idx, idy] = 1
        check_squares(space, 0, 0, 1, 0)
