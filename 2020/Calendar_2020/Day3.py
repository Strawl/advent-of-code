from Calendar_2020.ReadFiles import readfile


def task_1(xSpeed, YSpeed):
    lines = readfile(3)
    count = 0
    xCor = 0
    for x in range(YSpeed, len(lines), YSpeed):
        # One way is to add lines to the already existing ones -> very inefficient
        #   while (xCor + 3) >= len(lines[x])+1:
        #        lines[x] = lines[x].replace("\n","")
        #        lines[x] += lines[x].replace("\n", "")
        # Better way:
        xCor += xSpeed
        if xCor >= len(lines[x]): xCor -= len(lines[x])
        if lines[x][xCor] == '#': count += 1
    return count


def task_2():
    return task_1(1, 1) * task_1(3, 1) * task_1(5, 1) * task_1(7, 1) * task_1(1, 2)
