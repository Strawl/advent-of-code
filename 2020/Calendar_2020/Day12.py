import copy


def read():
    with open("Input/12.txt") as f:
        return [x.strip() for x in f.readlines()]


def task_1():
    values = [0] * 4
    index = 1
    for inst in read():
        if inst[0] == "F":
            values[index] += int(inst[1:])
        if inst[0] == "N": values[0] += int(inst[1:])
        if inst[0] == "E": values[1] += int(inst[1:])
        if inst[0] == "S": values[2] += int(inst[1:])
        if inst[0] == "W": values[3] += int(inst[1:])
        if inst[0] == "R":
            index += int(int(inst[1:]) / 90)
            if index >= len(values): index -= 4
        if inst[0] == "L":
            index -= int(int(inst[1:]) / 90)
            if index < 0: index += 4
    c = values[0] - values[2]
    if c < 0: c *= -1
    a = values[1] - values[3]
    if a < 0: a *= -1
    return c + a


def shift(key, array):
    return array[-key:] + array[:-key]


def task_2():
    waypoint = [1, 10, 0, 0]
    values = [0] * 4
    for inst in read():
        if inst[0] == "F":
            for i in range(len(values)):
                values[i] += int(inst[1:]) * waypoint[i]
        if inst[0] == "N": waypoint[0] += int(inst[1:])
        if inst[0] == "E": waypoint[1] += int(inst[1:])
        if inst[0] == "S": waypoint[2] += int(inst[1:])
        if inst[0] == "W": waypoint[3] += int(inst[1:])
        if inst[0] == "R":
            amount = int(int(inst[1:]) / 90)
            waypoint = copy.deepcopy(shift(amount, waypoint))
        if inst[0] == "L":
            amount = int(int(inst[1  :]) / 90)
            waypoint = copy.deepcopy(shift(4 - amount,waypoint))
    c = values[0] - values[2]
    if c < 0: c *= -1
    a = values[1] - values[3]
    if a < 0: a *= -1
    return c + a
