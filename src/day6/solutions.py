import numpy
import numpy as np
import re

from src.solution_template import Solver


class DaySix(Solver):
    filename = 'resources/input_day6.txt'
    dimensions = (1_000, 1_000)

    def solve_part1(self):
        light_grid = np.zeros(self.dimensions, dtype=bool)

        with open(self.filename) as f:
            for line in f:
                result_one, result_two = re.findall(r'\d+,\d+', line)
                x1, y1 = [int(i) for i in result_one.split(',')]
                x2, y2 = [1 + int(i) for i in result_two.split(',')]

                if line.startswith('turn on'):
                    light_grid[y1:y2, x1:x2] = True
                elif line.startswith('turn off'):
                    light_grid[y1:y2, x1:x2] = False
                elif line.startswith('toggle'):
                    light_grid[y1:y2, x1:x2] = ~light_grid[y1:y2, x1:x2]

        print("Solution for Day 6, Part 1 is: {}".format(np.count_nonzero(light_grid)))

    def solve_part2(self):
        light_grid = np.zeros(self.dimensions, dtype=int)

        with open(self.filename) as f:
            for line in f:
                result_one, result_two = re.findall(r'\d+,\d+', line)
                x1, y1 = [int(i) for i in result_one.split(',')]
                x2, y2 = [1 + int(i) for i in result_two.split(',')]
                subgrid = light_grid[y1:y2, x1:x2]

                if line.startswith('turn on'):
                    subgrid += 1
                elif line.startswith('turn off'):
                    nonzero_pos = subgrid.nonzero()
                    subgrid[nonzero_pos] -= 1
                elif line.startswith('toggle'):
                    subgrid += 2

        print("Solution for Day 6, Part 2 is: {}".format(light_grid.sum()))
