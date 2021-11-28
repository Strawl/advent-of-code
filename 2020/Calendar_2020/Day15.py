def task_1_2(iteration_count):
    # This code is using list, takes way to long to process not recommended
    """numbers = [12,20,0,6,1,17,7]
    print(numbers)
    for i in range(7, iteration_count):
        if numbers.count(numbers[i-1]) == 1: numbers.append(0)
        else: numbers.append(numbers[::-1][1:].index(numbers[len(numbers)-1])+1)
    return numbers[iteration_count-1]"""

    # Using Dictionaries is the wae to go
    numbers = {12: 0, 20: 1, 0: 2, 6: 3, 1: 4, 17: 5, 7: 6}
    lastNumber = 7
    for i in range(7, iteration_count):
        if numbers[lastNumber] == i - 1:
            lastNumber = 0
        else:
            x = numbers[lastNumber]
            numbers[lastNumber] = i - 1
            lastNumber = i - 1 - x
            if lastNumber not in numbers:
                numbers[lastNumber] = i
    return lastNumber
