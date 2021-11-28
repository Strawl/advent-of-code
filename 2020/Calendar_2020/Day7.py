import re


def read(z):
    with open("Input/7.txt") as f:
        bag_rules = list(map(lambda x: str(x).split(" contain "), f.read().split("\n")))
        for x in bag_rules:
            x[0] = x[0].replace(" ", "")[:-1]
            x[1] = re.sub(z, "", str(x[1].replace(" ", ""))).split(",")
            for l in range(0, len(x[1])):
                if x[1][l].endswith("bags"): x[1][l] = x[1][l][:-1]
        return bag_rules


counted = []


def task_1(search_word, bag_rules=read("[0-9.]")):
    count = 0
    for bags in bag_rules:
        for bag in bags[1]:
            if search_word in bag:
                if bags[0] not in counted:
                    counted.append(bags[0])
                    count += 1 + task_1(bags[0])
    return count


def task_2(search_word, bag_rules=read("[.]")):
    count = 0
    for bags in bag_rules:
        if search_word in bags[0]:
            for bag in bags[1]:
                if "nootherbag" in bag:
                    return 0
                count += int(bag[:1]) + int(bag[:1]) * task_2(bag[1:])
    return count
