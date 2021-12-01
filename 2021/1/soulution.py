# My take on the first day: 
with open("input.txt","r") as f:
    data = [int(x.strip()) for x in f.readlines()]
    inc_sum = 0
    for i in range(0,len(data)-1):
        if data[i+1] > data[i]:
            inc_sum += 1
    print(inc_sum)
    sum_inc_sum = 0
    for i in range(1,len(data)-2):
        if sum(data[i:i+3]) > sum(data[i-1:i+2]):
            sum_inc_sum += 1
    print(sum_inc_sum)

# Optimizing it into real one liners (very ugly):
data = [int(x.strip()) for x in open("input.txt","r").readlines()]
print(sum(data[i+1] > data[i] for i in range(0,len(data)-1)))
print(sum(sum(data[i:i+3]) > sum(data[i-1:i+2]) for i in range(1,len(data)-2)))

# Most elegant one-liner solution I found online:
n = [int(x.strip()) for x in open("input.txt","r").readlines()]
print(sum(a < b for a, b in zip(n, n[1:])))
print(sum(a < b for a, b in zip(n, n[3:])))
