from src.solution_template import Solver

FILENAME = 'resources/input_day1.txt'


class DayOne(Solver):

    def solve_part1(self):
        with open(FILENAME) as f:
            building_floor = 0
            while True:
                c = f.read(1)
                if not c:
                    break
                elif c == '(':
                    building_floor += 1
                elif c == ')':
                    building_floor -= 1

            print("Solution for Day 1, Part 1 is: {}".format(building_floor))

    def solve_part2(self):
        with open(FILENAME) as f:
            building_floor = 0
            file_pos = 0
            while True:
                c = f.read(1)
                if not c:
                    break

                if building_floor == -1:
                    print("Solution for Day 1, Part 2 is: {}".format(file_pos))
                    break
                elif c == '(':
                    building_floor += 1
                elif c == ')':
                    building_floor -= 1

                file_pos += 1
