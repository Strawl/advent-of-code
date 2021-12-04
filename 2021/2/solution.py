with open("input.txt","r") as f:
    data = [x.strip().split(" ") for x in f.readlines()]
    horizontal = depth= 0
    for x in data: 
        match x[0]:
            case "forward":
                horizontal += int(x[1])
            case "up":
                depth -= int(x[1]) 
            case "down":
                depth += int(x[1])
    print(horizontal * depth)
    aim = horizontal = depth = 0
    for x in data: 
        match x[0]:
            case "forward":
                horizontal += int(x[1])
                depth += aim * int(x[1])
            case "up":
                aim -= int(x[1]) 
            case "down":
                aim += int(x[1])
    print(horizontal * depth)



                
