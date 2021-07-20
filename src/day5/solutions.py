import itertools

from more_itertools import windowed, pairwise

from src.solution_template import Solver


def is_nice_string(test_string):
    vowels = 'aeiou'
    disallowed_substrings = ['ab', 'cd', 'pq', 'xy']

    condition1 = len(list(filter(lambda c: c in vowels, test_string))) >= 3
    condition2 = any(test_string[i] == test_string[i + 1] for i in range(len(test_string) - 1))
    condition3 = all(s not in test_string for s in disallowed_substrings)
    return condition1 and condition2 and condition3


def is_nice_string_2(test_string):
    enumerated_pairs = {k: v for k, v in enumerate(pairwise(test_string))}
    sorted_enumerated_pairs = sorted(enumerated_pairs.items(), key=lambda item: item[1])
    pairs_locations = {k: list(map(lambda group: group[0], g))
                       for k, g in itertools.groupby(sorted_enumerated_pairs, key=lambda item: item[1])}

    condition1 = False

    for x in pairs_locations.values():
        if len(x) >= 2:
            for c in itertools.combinations(x, 2):
                if abs(c[0] - c[1]) != 1:
                    condition1 = True

    condition2 = any(lhs == rhs for lhs, _, rhs in windowed(test_string, 3))

    return condition1 and condition2


class DayFive(Solver):
    FILENAME = 'resources/input_day5.txt'

    def solve_part1(self):
        count = 0
        with open(self.FILENAME) as f:
            for line in f:
                if is_nice_string(line.rstrip()):
                    count += 1

        print("Solution for Day 5, Part 1 is: {}".format(count))

    def solve_part2(self):
        count = 0
        with open(self.FILENAME) as f:
            for line in f:
                if is_nice_string_2(line.rstrip()):
                    count += 1

        print("Solution for Day 5, Part 2 is: {}".format(count))
