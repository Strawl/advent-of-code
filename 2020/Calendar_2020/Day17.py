import numpy as np


def increase_size(space):
    space = np.append(space, np.zeros((space.shape[0], 2, space.shape[2])), axis=1).copy()
    space = np.append(space, np.zeros((2, space.shape[1], space.shape[2])), axis=0).copy()
    space = np.append(space, np.zeros((space.shape[0], space.shape[1], 2)), axis=2).copy()
    # This works aswell but the above is more elegant
    """space.resize((space.shape[0] + 2, space.shape[1], space.shape[2]), refcheck=False)
    z = np.zeros((space.shape[0], space.shape[1], 2))
    space = np.concatenate((space, z), axis=2).copy()"""
    return np.roll(space, [1, 1, 1], axis=(0, 1, 2)).copy()


def increase_size_4d(space):
    space = np.append(space, np.zeros((space.shape[0], space.shape[1], 2, space.shape[3])), axis=2).copy()
    space = np.append(space, np.zeros((space.shape[0], 2, space.shape[2], space.shape[3])), axis=1).copy()
    space = np.append(space, np.zeros((space.shape[0], space.shape[1], space.shape[2],2)), axis=3).copy()
    space = np.append(space, np.zeros((2, space.shape[1], space.shape[2], space.shape[3])), axis=0).copy()
    return np.roll(space, [1, 1, 1, 1], axis=(0, 1, 2, 3)).copy()


def check_surrounding(space, x, y, z):
    return np.sum(
        space[x if x == 0 else x - 1:x + 2, y if y == 0 else y - 1:y + 2, z if z == 0 else z - 1:z + 2].copy())


def check_surrounding_4d(space, x, y, z, w):
    return np.sum(space[x if x == 0 else x - 1:x + 2, y if y == 0 else y - 1:y + 2, z if z == 0 else z - 1:z + 2,
                  w if w == 0 else w - 1:w + 2].copy())


def task_1():
    with open("Input/17.txt") as f:
        space = np.zeros((1, 8, 8))
        for i, l in enumerate(f.readlines()):
            for j, p in enumerate(list(l.strip())):
                if p == "#":
                    space[0, i, j] = 1
        for i in range(0, 6):
            space = increase_size(space)
            temp_space = space.copy()
            for idx, x in np.ndenumerate(space):
                if x == 1:
                    amount = check_surrounding(space, idx[0], idx[1], idx[2]) - 1
                    if amount != 2 and amount != 3:
                        temp_space[idx[0], idx[1], idx[2]] = 0
                else:
                    if check_surrounding(space, idx[0], idx[1], idx[2]) == 3:
                        temp_space[idx[0], idx[1], idx[2]] = 1
            space = temp_space.copy()
        return np.sum(space)


def task_2():
    with open("Input/17.txt") as f:
        space = np.zeros((1, 1, 8, 8))
        for i, l in enumerate(f.readlines()):
            for j, p in enumerate(list(l.strip())):
                if p == "#":
                    space[0, 0, i, j] = 1
        for i in range(0, 6):
            space = increase_size_4d(space)
            temp_space = space.copy()
            for idx, x in np.ndenumerate(space):
                if x == 1:
                    amount = check_surrounding_4d(space, idx[0], idx[1], idx[2], idx[3]) - 1
                    if amount != 2 and amount != 3:
                        temp_space[idx[0], idx[1], idx[2], idx[3]] = 0
                else:
                    if check_surrounding_4d(space, idx[0], idx[1], idx[2], idx[3]) == 3:
                        temp_space[idx[0], idx[1], idx[2], idx[3]] = 1
            space = temp_space.copy()
        return np.sum(space)
