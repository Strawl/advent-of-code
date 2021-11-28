from anytree import AnyNode, RenderTree, ContStyle, Walker


def make_tree(rules, tree_object):
    line = ""
    """if tree_object.id == "8":
        make_tree.count_1 += 1
    elif tree_object.id == "11":
        make_tree.count_2 += 1"""
    if len(str(tree_object.id).split(" ")) != 1:
        line = tree_object.id
    else:
        line = rules[int(tree_object.id)]
    if "|" in line:
        for x in line.split(" | "):
            child = AnyNode(id=x, parent=tree_object, is_or=False)
            tree_object.is_or = True
            """if (tree_object.id == "8" and make_tree.count_1 > 10) or (
                    tree_object.id == "11" and make_tree.count_2 > 10):
                pass
            else:"""
            make_tree(rules, child)
    else:
        for x in line.split(" "):
            if "a" in x or "b" in x:
                child = AnyNode(id=x[1], parent=tree_object, is_or=False)
            else:
                child = AnyNode(id=x, parent=tree_object, is_or=False)
                """if (tree_object.id == "8" and make_tree.count_1 > 10) or (
                        tree_object.id == "11" and make_tree.count_2 > 10):
                    pass
                else:"""
                make_tree(rules, child)


make_tree.count_1 = 0
make_tree.count_2 = 0


def validate(value, tree, index=0):
    if index == len(value):
        print(index)
        return index
    temp_index = index
    w = Walker()
    if len(tree.children) == 0:
        if value[index] == tree.id:
            index += 1
    count = 0
    for child in tree.children:
        walk = w.walk(tree, child)
        if tree.is_or:
            check = validate(value, walk[2][0], temp_index)
            if check > index:
                index = check
        else:
            check = validate(value, walk[2][0], index)
            if check > index:
                count += 1
                index = check
    if tree.is_or:
        return index
    if len(tree.children) == 0 or count % len(tree.children) == 0:
        return index
    else:
        return temp_index


def task_1():
    with open("Input/19.txt") as f:
        data = [x.split("\n") for x in f.read().split("\n\n")]
        rules = {}
        for x in data[0]:
            split = x.split(": ")
            rules[int(split[0])] = split[1]
        root = AnyNode(id="0", parent=None, is_or=False)
        make_tree(rules, root)
        count = 0
        for x in data[1]:
            if validate(x, root) == len(x): count += 1
        print(len(data[1]))
        return count


def task_2():
    with open("Input/19.txt") as f:
        data = [x.split("\n") for x in f.read().split("\n\n")]
        rules = {}
        for x in data[0]:
            split = x.split(": ")
            rules[int(split[0])] = split[1]
        rules[8] = "42 | 42 8"
        rules[11] = "42 31 | 42 11 31"
        root = AnyNode(id="0", parent=None, is_or=False)
        make_tree(rules, root)
        print(RenderTree(root, ContStyle()))
        count = 0
        for x in data[1]:
            if validate(x, root) == len(x): count += 1
        print(len(data[1]))
        return count
