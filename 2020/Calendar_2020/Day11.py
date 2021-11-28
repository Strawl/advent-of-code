import copy


def read():
    with open("Input/11.txt") as f:
        return [x.strip() for x in f.readlines()]


def task_1():
    before = read()
    after = read()
    amount = -1
    while True:
        for row_index, rows in enumerate(before):
            for seat_index, seat_place in enumerate(rows):
                if seat_place == ".":
                    pass
                elif seat_place == "L":
                    count = 0
                    if seat_index - 1 == -1 or (before[row_index][seat_index - 1] != "#"): count += 1
                    if seat_index + 1 == len(rows) or before[row_index][seat_index + 1] != "#": count += 1
                    if row_index - 1 == -1 or before[row_index - 1][seat_index] != "#": count += 1
                    if row_index + 1 == len(before) or before[row_index + 1][seat_index] != "#": count += 1
                    if seat_index - 1 == -1 or row_index - 1 == -1 or before[row_index - 1][
                        seat_index - 1] != "#": count += 1
                    if seat_index + 1 == len(rows) or row_index - 1 == -1 or before[row_index - 1][
                        seat_index + 1] != "#": count += 1
                    if seat_index + 1 == len(rows) or row_index + 1 == len(before) or before[row_index + 1][
                        seat_index + 1] != "#": count += 1
                    if seat_index - 1 == -1 or row_index + 1 == len(before) or before[row_index + 1][
                        seat_index - 1] != "#": count += 1
                    if count == 8:
                        new = list(after[row_index])
                        new[seat_index] = '#'
                        after[row_index] = ''.join(new)
                elif seat_place == "#":
                    count = 0
                    if seat_index - 1 != -1 and (before[row_index][seat_index - 1] == "#"): count += 1
                    if seat_index + 1 != len(rows) and before[row_index][seat_index + 1] == "#": count += 1
                    if row_index - 1 != -1 and before[row_index - 1][seat_index] == "#": count += 1
                    if row_index + 1 != len(before) and before[row_index + 1][seat_index] == "#": count += 1
                    if seat_index - 1 != -1 and row_index - 1 != -1 and before[row_index - 1][
                        seat_index - 1] == "#": count += 1
                    if seat_index + 1 != len(rows) and row_index - 1 != -1 and before[row_index - 1][
                        seat_index + 1] == "#": count += 1
                    if seat_index + 1 != len(rows) and row_index + 1 != len(before) and before[row_index + 1][
                        seat_index + 1] == "#": count += 1
                    if seat_index - 1 != -1 and row_index + 1 != len(before) and before[row_index + 1][
                        seat_index - 1] == "#": count += 1
                    if count >= 4:
                        new = list(after[row_index])
                        new[seat_index] = 'L'
                        after[row_index] = ''.join(new)
        c = sum([x.count("#") for x in before])
        if amount == c: return c
        amount = c
        before = copy.deepcopy(after)
    return count


def look(x_position, y_position, x_speed, y_speed, input_lis):
    try:
        if x_position+x_speed >= 0 and y_position+y_speed >= 0:
            if input_lis[y_position + y_speed][x_position + x_speed] == ".":
                lookedChar = look(x_position + x_speed, y_position + y_speed, x_speed, y_speed, input_lis)
            else:
                return input_lis[y_position + y_speed][x_position + x_speed]
            return lookedChar
        else: return '.'
    except:
        return "."


def task_2():
    before = read()
    after = read()
    amount = -1
    while True:
        for row_index, rows in enumerate(before):
            for seat_index, seat_place in enumerate(rows):
                if seat_place == ".":
                    pass
                elif seat_place == "L":
                    count = 0
                    if look(seat_index, row_index, -1, -1, before) != '#': count += 1
                    if look(seat_index, row_index, -1, 0, before) != '#': count += 1
                    if look(seat_index, row_index, -1, 1, before) != '#': count += 1
                    if look(seat_index, row_index, 0, 1, before) != '#': count += 1
                    if look(seat_index, row_index, 1, 1, before) != '#': count += 1
                    if look(seat_index, row_index, 1, 0, before) != '#': count += 1
                    if look(seat_index, row_index, 1, -1, before) != '#': count += 1
                    if look(seat_index, row_index, 0, -1, before) != '#': count += 1
                    if count == 8:
                        new = list(after[row_index])
                        new[seat_index] = '#'
                        after[row_index] = ''.join(new)
                elif seat_place == "#":
                    count = 0
                    if look(seat_index, row_index, -1, -1, before) == '#': count += 1
                    if look(seat_index, row_index, -1, 0, before) == '#': count += 1
                    if look(seat_index, row_index, -1, 1, before) == '#': count += 1
                    if look(seat_index, row_index, 0, 1, before) == '#': count += 1
                    if look(seat_index, row_index, 1, 1, before) == '#': count += 1
                    if look(seat_index, row_index, 1, 0, before) == '#': count += 1
                    if look(seat_index, row_index, 1, -1, before) == '#': count += 1
                    if look(seat_index, row_index, 0, -1, before) == '#': count += 1
                    if count >= 5:
                        new = list(after[row_index])
                        new[seat_index] = 'L'
                        after[row_index] = ''.join(new)
        c = sum([x.count("#") for x in after])
        if amount == c: return c
        amount = c
        before = copy.deepcopy(after)
