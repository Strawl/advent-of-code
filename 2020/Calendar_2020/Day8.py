def read_commands():
    with open("Input/8.txt") as f:
        return [x.split(" ") for x in f.read().split("\n")]


def run(changeIndex=-1):
    usedIndexes = list()
    commands = read_commands()
    index = 0
    accumulator = 0
    if changeIndex != -1:
        if commands[changeIndex][0] == "jmp":
            commands[changeIndex][0] = "nop"
        elif commands[changeIndex][0] == "nop":
            commands[changeIndex][0] = "jmp"
    while index not in usedIndexes:
        usedIndexes.append(index)
        if index == 682:
            return [usedIndexes, accumulator, True, [index, commands[index]]]
        if commands[index][0] == "acc":
            accumulator += int(commands[index][1])
            index += 1
        elif commands[index][0] == "jmp":
            index += int(commands[index][1])
        elif commands[index][0] == "nop":
            index += 1
    return [usedIndexes, accumulator, False, [index, commands[index]]]


def task_1():
    return run()[1]


def task_2():
    x = read_commands()
    for index, l in enumerate(x):
        if run(index)[2]:
            return run(index)[1]
