import math
def part_one(filename):
    with open(filename, "r") as file:
        data = sum(([math.floor(int(x.replace("\n", ""))/3) - 2 for x in file.readlines()]))
        return data

def calculate_fuel(fuel):
    fuel_sum = fuel
    fuel = math.floor(fuel / 3) - 2 
    while fuel >= 0:
        fuel_sum += fuel 
        fuel = math.floor(fuel / 3) - 2 
    return fuel_sum

def part_two(filename):
    with open(filename, "r") as file:
        data = sum([calculate_fuel(x) for x in [math.floor(int(x.replace("\n", ""))/3) - 2 for x in file.readlines()]])
        return data
    
    

print(part_one("input.txt"))
print(part_two("input.txt"))
