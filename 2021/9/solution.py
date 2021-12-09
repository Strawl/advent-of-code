import numpy

def basin_lookup(index):
    x = ndarray[index]
    basin_array = [index]
    if ndarray.shape[1] != index[1] + 1 and ndarray[index[0], index[1]+1] > x and ndarray[index[0], index[1]+1] != 9:
        basin_array = basin_array + basin_lookup((index[0], index[1] + 1))
    if ndarray.shape[0] != index[0] + 1 and ndarray[index[0] + 1, index[1]] > x and ndarray[index[0] + 1, index[1]] != 9:
        basin_array = basin_array + basin_lookup((index[0] + 1, index[1]))
    if -1 != index[1] - 1 and ndarray[index[0], index[1] - 1 ] > x and ndarray[index[0], index[1] - 1 ] != 9:
        basin_array = basin_array + basin_lookup((index[0], index[1] - 1))
    if -1 != index[0] - 1 and ndarray[index[0] - 1, index[1]] > x and ndarray[index[0] - 1, index[1]] != 9:
        basin_array = basin_array + basin_lookup((index[0] - 1, index[1]))
    return basin_array

ndarray = numpy.genfromtxt('input.txt', delimiter=1, dtype=int)
count = 0
shape = ndarray.shape
basin_sizes = []
for index, x in numpy.ndenumerate(ndarray):
    if ndarray.shape[1] == index[1] + 1 or ndarray[index[0], index[1]+1] > x:
        if ndarray.shape[0] == index[0] + 1 or ndarray[index[0] + 1, index[1]] > x:
            if -1 == index[1] - 1  or ndarray[index[0], index[1] - 1 ] > x:
                if -1 == index[0] - 1  or ndarray[index[0] -1, index[1]] > x:
                    basin_sizes.append(len(set(basin_lookup(index))))
                    count += 1 + x
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
print(count)

