import hashlib
import itertools

from src.solution_template import Solver


class DayFour(Solver):
    filename = 'resources/input_day4.txt'

    def solve_part1(self):
        f = open(self.filename)
        data = f.read().rstrip()
        f.close()

        for num in itertools.count(start=1):
            temp = "{}{}".format(data, num).encode('utf-8')
            m = hashlib.md5(temp)
            if m.hexdigest().startswith('00000'):
                print("Solution for Day 4, Part 1 is: {}".format(num))
                break

    def solve_part2(self):
        f = open(self.filename)
        data = f.read().rstrip()
        f.close()

        for num in itertools.count(start=1):
            temp = "{}{}".format(data, num).encode('utf-8')
            m = hashlib.md5(temp)
            if m.hexdigest().startswith('000000'):
                print("Solution for Day 4, Part 2 is: {}".format(num))
                break
