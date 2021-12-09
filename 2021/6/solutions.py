import functools
with open("input.txt","r") as f:
    data = [int(x) for x in f.read().strip().split(",")]

@functools.lru_cache(maxsize=None)
def iterate(days,iteration):
    if iteration-days <= 0: return 0
    count = int((iteration-days-1) / 7 ) + 1
    for x in range(days,iteration+1, 7):
        count += iterate(6,iteration-x-3)  
    return count

def calculate_number_of_fish(iteration):
    count_dict = {}
    for x in set(data):
        count_dict[x] = iterate(x,iteration)
    g_count = 0
    for k, v in count_dict.items():
        g_count += data.count(k) * v
    print(g_count+len(data))

calculate_number_of_fish(80)
calculate_number_of_fish(256)
    
