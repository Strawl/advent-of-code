import threading

from Calendar_2020 import Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14, \
    Day15, Day16, Day17, Day18, Day19, Day20
import time
import sys

t1 = time.time()
print("*****Advent of Code****+")
print("Day 1 Task 1")
print(Day1.task_1())
print("\nDay 1 Task 2")
print(Day1.task_2())
print("\nDay 2 Task 1")
print(Day2.task_1())
print("\nDay 2 Task 2")
print(Day2.task_2())
print("\nDay 3 Task 1")
print(Day3.task_1(3, 1))
print("\nDay 3 Task 2")
print(Day3.task_2())
print("\nDay 4 Task 1")
print(Day4.task_1())
print("\nDay 4 Task 2")
print(Day4.task_2())
print("\nDay 5 Task 1")
print(Day5.task_1())
print("\nDay 5 Task 2")
print(Day5.task_2())
print("\nDay 6 Task 1")
print(Day6.task_1())
print("\nDay 6 Task 2")
print(Day6.task_2())
print("\nDay 7 Task 1")
print(Day7.task_1("shinygoldbag"))
print("\nDay 7 Task 2")
print(Day7.task_2("shinygoldbag"))
print("\nDay 8 Task 1")
print(Day8.task_1())
print("\nDay 8 Task 2")
print(Day8.task_2())
print("\nDay 9 Task 1")
print(Day9.task_1())
print("\nDay 9 Task 2")
print(Day9.task_2())
print("\nDay 10 Task 1")
print(Day10.task_1())
print("\nDay 10 Task 2")
print(Day10.task_2())
print("\nDay 11 Task 1")
print(Day11.task_1())
print("\nDay 11 Task 2")
print(Day11.task_2())
print("\nDay 12 Task 1")
print(Day12.task_1())
print("\nDay 12 Task 2")
print(Day12.task_2())
print("\nDay 13 Task 1")
print(Day13.task_1())
print("\nDay 13 Task 2")
print(Day13.task_2())
print("\nDay 14 Task 1")
print(Day14.task_1())
print("\nDay 14 Task 2")
print(Day14.task_2())
print("\nDay 15 Task 1")
print(Day15.task_1_2(2020))
print("\nDay 15 Task 2")
print(Day15.task_1_2(30000000))
print("\nDay 16 Task 1")
print(Day16.task_1())
print("\nDay 16 Task 2")
print(Day16.task_2())
print("\nDay 17 Task 1")
print(Day17.task_1())
print("\nDay 17 Task 2")
print(Day17.task_2())
print("\nDay 18 Task 1")
print(Day18.task_1())
print("\nDay 18 Task 2")
print(Day18.task_2())
print("\nDay 19 Task 1")
print(Day19.task_1())
# print("\nDay 19 Task 2")
# print("---Construction Site---")
# print(Day19.task_2())
# print("\nDay 20 Task 1")
# print(Day20.task_1())

print()
print(f"All of these Tasks took {time.time() - t1} time")
