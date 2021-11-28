def translate(value, mask):
    binaryString = bin(value)
    stringArray = ["0"] * (len(mask) - len(binaryString) + 2) + list(binaryString[2:])
    for i, x in enumerate(mask):
        if x != "X":
            stringArray[i] = x
    return int("".join(stringArray), 2)


def translate_with_floating_bits(value, mask):
    binaryString = bin(value)
    stringArray = ["0"] * (len(mask) - len(binaryString) + 2) + list(binaryString[2:])
    for i, x in enumerate(mask):
        if x == "1":
            stringArray[i] = x
        if x == "X":
            stringArray[i] = x
    floating_array = [stringArray.copy() for x in range(2 ** mask.count("X"))]
    for index, float_option in enumerate(floating_array):
        bin_index = bin(index)[2:]
        bin_array = ["0"] * (mask.count("X") - len(bin_index)) + list(bin_index)
        i = 0
        for in_x in range(len(float_option)):
            if float_option[in_x] == "X":
                float_option[in_x] = bin_array[i]
                i += 1
        floating_array[index] = int("".join(float_option), 2)

    return floating_array


def task_1():
    with open("Input/14.txt") as f:
        input_data = [x.strip().split(" = ") for x in f.readlines()]
        current_mask = ""
        mem = {}
        for data_line in input_data:
            if data_line[0] == "mask":
                current_mask = data_line[1]
            elif data_line[0].startswith("mem"):
                index = data_line[0][4:-1]
                mem[index] = translate(int(data_line[1]), current_mask)
        return sum(mem.values())


def task_2():
    with open("Input/14.txt") as f:
        input_data = [x.strip().split(" = ") for x in f.readlines()]
        current_mask = ""
        mem = {}
        for data_line in input_data:
            if data_line[0] == "mask":
                current_mask = data_line[1]
            elif data_line[0].startswith("mem"):
                index = data_line[0][4:-1]
                index_list = translate_with_floating_bits(int(index), current_mask)
                for i in index_list:
                    mem[i] = int(data_line[1])
        return sum(mem.values())
