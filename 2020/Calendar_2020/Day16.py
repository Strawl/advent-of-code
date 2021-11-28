def match(numbers, value):
    n = numbers.split(" ")
    if (int(n[0]) <= value <= int(n[1])) or (int(n[2]) <= value <= int(n[3])):
        return True
    return False


def task_1():
    with open("Input/16.txt") as f:
        data = [[lines.strip() for lines in x.split("\n")] for x in f.read().split("\n\n")]
        keys = [d.split(": ")[0] for d in data[0]]
        values = [(d.split(": ")[1].replace(" or ", " ")).replace("-", " ") for d in data[0]]
        specifications_dictionary = dict(zip(keys, values))
        false_values = []
        for other_tickets in data[2]:
            for specs in other_tickets.split(","):
                one_spec_is_false = False
                for l in specifications_dictionary.values():
                    if match(l, int(specs)):
                        one_spec_is_false = True
                        break
                if not one_spec_is_false: false_values.append(int(specs))
        return sum(false_values)


def task_2():
    with open("Input/16.txt") as f:
        data = [[lines.strip() for lines in x.split("\n")] for x in f.read().split("\n\n")]
        keys = [d.split(": ")[0] for d in data[0]]
        values = [(d.split(": ")[1].replace(" or ", " ")).replace("-", " ") for d in data[0]]
        specifications_dictionary = dict(zip(keys, values))
        bad_tickets = []
        for other_ticket in data[2]:
            for field in other_ticket.split(","):
                legit = False
                for specification in specifications_dictionary.values():
                    if match(specification, int(field)):
                        legit = True
                if not legit:
                    bad_tickets.append(other_ticket)
                    break
        [data[2].remove(b) for b in bad_tickets]
        good_tickets = data[2].copy()
        order = {}
        neigh = [x.split(",") for x in good_tickets]
        for x in specifications_dictionary.keys():
            indexes = []
            for i in range(0, 20):
                field_is_good_for_this_specs = True
                for l in neigh:
                    if not match(specifications_dictionary[x], int(l[i])):
                        field_is_good_for_this_specs = False
                if field_is_good_for_this_specs:
                    indexes.append(i)
            order[x] = indexes
        correct_order = {}
        while len(order) != 0:
            for x in order.keys():
                if len(order[x]) == 1:
                    correct_order[x] = order[x][0]
                    for l in order.keys():
                        if correct_order[x] in order[l]:
                            order[l].remove(correct_order[x])
                    order.pop(x)
                    break
        count = 1
        for pos in correct_order.keys():
            if pos.startswith("departure"):
                count *= int(data[1][0].split(",")[correct_order[pos]])
        return count
