from Calendar_2020.ReadFiles import readfile


def task_1():
    lines = readfile(2)
    count = 0
    for x in lines:
        ranges, policyChar, password = x.split()
        split = ranges.split("-")
        if int(split[0]) <= password.count(policyChar[0]) <= int(split[1]):
            count += 1
    return count


def task_2():
    lines = readfile(2)
    count = 0
    for x in lines:
        ranges, policyChar, password = x.split()
        split = ranges.split("-")
        if (password[int(split[0]) - 1] == policyChar[0]) ^ (password[int(split[1]) - 1] == policyChar[0]):
            count += 1
    return count
