with open("input.txt", "r") as f: 
    data = [[[int(z)for z in y.split(",")] for y in x.strip().split(" -> ") ] for x in f.readlines()]
    all_points = []
    seen = []
    for pos in data:
        pos.sort()
        if pos[0][0] == pos[1][0] or pos[0][1] == pos[1][1]:
            xory = int(pos[0][0] == pos[1][0])
            for i in range(pos[0][xory],pos[1][xory]+1):
                xy = [0,0]
                xy[xory] = i
                xy[int(not xory)] = pos[0][int(not xory)]
                if xy in all_points and xy not in seen:
                    seen.append(xy)
                all_points.append(xy)
        else:
            y = pos[0][1]
            direction = int(pos[0][1] <= pos[1][1]) 
            if direction == 0: direction = -1
            for x in range(pos[0][0], pos[1][0]+1):
                xy = [x,y]
                if xy in all_points and xy not in seen:
                    seen.append(xy)
                all_points.append(xy)
                y += direction  

    print(len(seen))