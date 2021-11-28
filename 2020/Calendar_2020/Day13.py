import math


def task_1():
    with open("Input/13.txt") as f:
        input_data = [x.strip().replace("x", "").split(",") for x in f.readlines()]
        busses = [line for line in input_data[1] if line.strip() != '']
        arrival_time = int(input_data[0][0])
        earliest_time = [math.ceil(arrival_time / int(bus)) * int(bus) for bus in busses]
        best_bus = min(earliest_time)
        return (best_bus - arrival_time) * int(busses[earliest_time.index(best_bus)])


def task_2():
    with open("Input/13.txt") as f:
        input_data = [x.strip().replace("x", "").split(",") for x in f.readlines()]
        busses = [int(line) for line in input_data[1] if line.strip() != '']
        sub_tim = [input_data[1].index(line) for line in input_data[1] if line.strip() != '']
        x1 = 0
        x2 = 0
        tru_that = False
        increase = max(busses)
        offset = sub_tim[busses.index(increase)]
        index = max(busses)
        # index = busses[0]
        # amount = busses[0]
        while True:
            index += increase
            x = index - offset
            if x % busses[0] == 0:
                if (x + sub_tim[1]) % busses[1] == 0:
                    if (x + sub_tim[8]) % busses[8] == 0:
                        if (x + sub_tim[3]) % busses[3] == 0:
                            if (x + sub_tim[4]) % busses[4] == 0:
                                if x1 == 0:
                                    x1 = x
                                elif x2 == 0:
                                    x2 = x
                                if (x + sub_tim[5]) % busses[5] == 0:
                                    if (x + sub_tim[6]) % busses[6] == 0:
                                        if (x + sub_tim[7]) % busses[7] == 0:
                                            return x
            # Getting the difference so my program finds the solution faster
            if x2 != 0 and not tru_that:
                increase = x2 - x1
                tru_that = True
