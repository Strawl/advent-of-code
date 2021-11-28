with open("Input/9.txt") as f:
    lines = list(map(int, f.readlines()))
    all_other = lines[25:]


def task_1():
    for i,val in enumerate(all_other):
        done = False
        for j in range(25):
            for l in range(25):
                if val == int(lines[i + j]) + int(lines[i + l]):
                    done = True
        if not done:
            return lines[i + 25]


def task_2():
    start_value = task_1()
    for i in range(0, len(all_other)):
        number = all_other[i]
        index = i
        while number < start_value:
            index += 1
            number += all_other[index]
            if number == start_value:
                return min(all_other[i:index + 1]) + max(all_other[i:index + 1])


