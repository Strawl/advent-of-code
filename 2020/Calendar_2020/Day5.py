from Calendar_2020.ReadFiles import readfile
import math


def search_seats(boarding_passes):
    seatRowMin = 0
    seatRowMax = 127
    seatColMin = 0
    seatColMax = 7
    for letter in boarding_passes:
        if letter == "F":
            seatRowMax -= math.ceil((seatRowMax - seatRowMin) / 2)
        if letter == "B":
            seatRowMin += math.ceil((seatRowMax - seatRowMin) / 2)
        if letter == "R":
            seatColMin += math.ceil((seatColMax - seatColMin) / 2)
        if letter == "L":
            seatColMax -= math.ceil((seatColMax - seatColMin) / 2)
    return seatRowMin * 8 + seatColMax


def task_1():
    seat_ids = list(map(search_seats, readfile(5)))
    return max(seat_ids)


def task_2():
    seat_ids = list(map(search_seats, readfile(5)))
    seat_ids.sort()
    for x in range(0, len(seat_ids)):
        if seat_ids[x + 1] - seat_ids[x] == 2:
            return seat_ids[x] + 1
