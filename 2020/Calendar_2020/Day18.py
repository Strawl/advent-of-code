def find(i, expression):
    l = -1
    for o in range(i + 1, len(expression)):
        if o < len(expression) and expression[o].isnumeric():
            l = o
        else:
            break
    return l


def calculate_left_to_right(expression):
    while "(" in expression:
        x = expression.rfind("(")
        y = x + expression[x:].find(")")
        exp = expression[x + 1:y]
        expression = expression.replace("(" + str(exp) + ")", str(calculate_left_to_right(exp)))
    p = find(-1, expression)
    count = int(expression[0:p + 1])
    for i in range(p, len(expression)):
        if expression[i] == "+":
            if "+" in expression[i + 1:] or "*" in expression[i + 1:]:
                l = find(i, expression)
                count += int(expression[i + 1:l + 1])
                i = l
            else:
                count += int(expression[i + 1:])
        if expression[i] == "*":
            if "+" in expression[i + 1:] or "*" in expression[i + 1:]:
                l = find(i, expression)
                count *= int(expression[i + 1:l + 1])
                i = l
            else:
                count *= int(expression[i + 1:])
    return count


def calculate_add_first(expression):
    while "(" in expression:
        x = expression.rfind("(")
        y = x + expression[x:].find(")")
        exp = expression[x + 1:y]
        expression = expression.replace("(" + str(exp) + ")", str(calculate_add_first(exp)))
    while "+" in expression:
        i = expression.find("+")
        p = find(i, expression)
        l = len(expression) - find(len(expression)-i-1,expression[::-1]) -1
        expression = expression.replace(expression[l:p+1],str(int(expression[l:i]) + int(expression[i+1:p+1])))
    while "*" in expression:
        i = expression.find("*")
        p = find(i, expression)
        l = len(expression) - find(len(expression)-i-1,expression[::-1]) -1
        expression = expression.replace(expression[l:p+1],str(int(expression[l:i]) * int(expression[i+1:p+1])))
    return int(expression)


def task_1():
    with open("Input/18.txt") as f:
        math_expressions = [x.strip().replace(" ", "") for x in f.readlines()]
        return sum([int((calculate_left_to_right(x))) for x in math_expressions])


def task_2():
    with open("Input/18.txt") as f:
        math_expressions = [x.strip().replace(" ", "") for x in f.readlines()]
        return sum([int((calculate_add_first(x))) for x in math_expressions])
