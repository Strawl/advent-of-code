from Calendar_2020.ReadFiles import readfile


def task_1():
    lines = list(map(int, readfile(1)))
    for x in lines:
        for y in lines:
            if x + y == 2020:
                return x * y * y


def task_2():
    lines = list(map(int, readfile(1)))
    for x in lines:
        for y in lines:
            for z in lines:
                if x + y + z == 2020:
                    return x * y * z
