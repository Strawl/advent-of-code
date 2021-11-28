#from aocd.models import Puzzle


#def readwebsite(number):
#    puzzle = Puzzle("Calendar_2020", number)
#    return puzzle.input_data.split("\n")


def readfile(number):
    with open("Input/"+str(number)+".txt") as f:
        return list(map(lambda x : str(x).strip("\n"),f.readlines()))

