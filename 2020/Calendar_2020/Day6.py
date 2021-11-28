def read_questions(z):
    with open("Input/6.txt") as f:
        return map(lambda x: str(x).replace("\n", z), f.read().split("\n\n"))


def task_1():
    return sum(map(lambda x: len(set(x)), read_questions("")))


# task_2 schön, performanter:

"""count = 0
    groups = read_questions(" ")
    for group in groups:
        for letter in set(group):
            if group.count(letter) == group.count(" ")+1:
                count += 1
    return count"""


# nicht so performant aber einzeiler
def task_2():
    return sum(map(lambda g: sum(map(lambda x: int(g.count(x) == g.count(" ") + 1), set(g))), read_questions(" ")))
