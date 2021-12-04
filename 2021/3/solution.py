import numpy as np
with open("input.txt","r") as f:
    data = [list(map(int, x)) for x in f.read().split("\n")]
    data = np.array(data)
    column_sums = data.sum(axis=0)
    rows, columns = data.shape
    final_binary = ""
    for x in column_sums:
        final_binary += str(int(x >= rows/2))
    print(int(final_binary,2) * (int(final_binary,2) ^ 0b111111111111) )
    data_oxygen = data_scrubber= np.copy(data)
    i = 0
    while data_oxygen.shape[0] != 1:
        column_sums = data_oxygen.sum(axis=0)
        most_occuring = int(column_sums[i] >= data_oxygen.shape[0]-column_sums[i])
        data_oxygen = np.delete(data_oxygen, np.where(data_oxygen[:,i] != most_occuring), axis=0)
        i += 1
    i = 0
    while data_scrubber.shape[0] != 1:
        column_sums = data_scrubber.sum(axis=0)
        least_occuring = int(column_sums[i] < data_scrubber.shape[0]-column_sums[i])
        data_scrubber = np.delete(data_scrubber, np.where(data_scrubber[:,i] != least_occuring), axis=0)
        i += 1
    print((data_oxygen.dot(1 << np.arange(data_oxygen.shape[-1] -1, -1, -1 )) * data_scrubber.dot(1 << np.arange(data_scrubber.shape[-1] -1, -1, -1 )))[0])