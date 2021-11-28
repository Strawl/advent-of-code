def task_1():
    with open("Input/10.txt") as f:
        lines = list(map(int, f.readlines()))
        lines.sort()
        count = 0
        count2 = 0
        for i in range(0, len(lines) - 1):
            difference = lines[i + 1] - lines[i]
            if difference == 1:
                count += 1
            if difference == 3:
                count2 += 1
        return (count + 1) * (count2 + 1)


def task_2():
    with open("Input/10.txt") as f:
        lines = list(map(int, f.readlines()))
        lines.append(0)
        lines.append(max(lines) + 3)
        lines.sort()
        needed = [0]
        for index_i, i in enumerate(lines):
            if index_i + 1 < len(lines):
                if lines[index_i + 1] - lines[index_i] == 3:
                    if index_i not in needed:
                        needed.append(index_i)
                    if index_i + 1 not in needed:
                        needed.append(index_i + 1)

        count = 1
        for i in range(len(needed) - 1):
            if lines[needed[i + 1]] - lines[needed[i]] > 3: count *= ((2 ** 3) - 1)
            if lines[needed[i + 1]] - lines[needed[i]+1] == 2: count *= 2**2
            if lines[needed[i + 1]] - lines[needed[i]+1] == 1: count *= 2

        return count
