from Calendar_2020.ReadFiles import readfile
import re


def read_passwords():
    with open("Input/4.txt") as f:
        return map(lambda x: str(x).replace("\n", " "), f.read().split("\n\n"))


def check(dataset):
    count = 0
    for d in dataset:
        if d[0] == "byr":
            if 1920 <= int(d[1]) <= 2002: count += 1
        elif d[0] == "iyr":
            if 2010 <= int(d[1]) <= 2020: count += 1
        elif d[0] == "eyr":
            if 2020 <= int(d[1]) <= 2030: count += 1
        elif d[0] == "hgt":
            value = int(re.sub("cm|in", "", d[1]))
            if str(d[1]).endswith("cm") and 150 <= value <= 193:
                count += 1
            elif str(d[1]).endswith("in") and 59 <= value <= 76:
                count += 1
        elif d[0] == "hcl":
            if (len(d[1]) == 7) and re.sub("[#0-9a-f]", "", d[1]) == "": count += 1
        elif d[0] == "ecl":
            if re.sub("amb|blu|brn|gry|grn|hzl|oth", "", d[1]) == "": count += 1
        elif d[0] == "pid":
            if len(d[1]) == 9 and d[1].isnumeric(): count += 1
    return count == 7


def contain_check(s):
    if "byr" in s and "iyr" in s and "eyr" in s and "hgt" in s and "hcl" in s and "ecl" in s and "pid" in s:
        return True


def task_1():
    passwords = read_passwords()
    counter = 0
    for s in passwords:
        if contain_check(s):
            counter += 1
    return counter


def task_2():
    passwords = read_passwords()
    counter = 0
    for s in passwords:
        if contain_check(s):
            dataset = list(map(lambda st: st.split(":"), s.split()))
            if check(dataset): counter += 1
    return counter
