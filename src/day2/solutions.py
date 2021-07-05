import math

from src.solution_template import Solver

FILENAME = 'resources/input_day2.txt'


class DayTwo(Solver):
    def solve_part1(self):
        total = 0
        with open(FILENAME) as f:
            for line in f:
                dimensions = [int(i) for i in line.split('x')]
                dimensions.sort()
                surface_area = 2 * ((dimensions[0] * dimensions[1]) + (dimensions[0] * dimensions[2]) + (
                        dimensions[1] * dimensions[2]))
                total += surface_area + (dimensions[0] * dimensions[1])

        print("Solution for Day 2, Part 1 is: {}".format(total))

    def solve_part2(self):
        total = 0
        with open(FILENAME) as f:
            for line in f:
                dimensions = [int(i) for i in line.split('x')]
                dimensions.sort()
                ribbon_length = 2 * (dimensions[0] + dimensions[1])
                total += ribbon_length + math.prod(dimensions)

        print("Solution for Day 2, Part 1 is: {}".format(total))
