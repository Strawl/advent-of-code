with open("input.txt","r") as f:
    data = [int(x.strip()) for x in f.readlines()]
    prev = data[0]
    inc_sum = 0
    for x in data[1:]:
        if x > prev:
            inc_sum += 1
        prev = x
    print(inc_sum)
    prev_sum = sum(data[0:3])
    sum_inc_sum = 0
    for i in range(1,len(data)-2):
        cur_sum = sum(data[i:i+3]) 
        if cur_sum > prev_sum:
            sum_inc_sum += 1
        prev_sum = cur_sum
    print(sum_inc_sum)

        
        



