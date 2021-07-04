import sys

from more_itertools import partition
from build_solvers import SOLVERS


def get_valid_args(arg):
    if ':' in arg:
        [lhs_arg, rhs_arg] = arg.split(':', 1)
        try:
            lhs_arg = int(lhs_arg)
            rhs_arg = int(rhs_arg)
        except ValueError:
            return False
        if 1 <= lhs_arg <= 25 and 0 <= rhs_arg <= 2:
            return True
    else:
        try:
            day = int(arg)
        except ValueError:
            return False
        if 1 <= day <= 25:
            return True


def change_to_funcs(pair):
    k, v = pair
    silly = SOLVERS[k - 1]()

    func = None
    if v == 0:
        func = silly.solve_all
    elif v == 1:
        func = silly.solve_part1
    elif v == 2:
        func = silly.solve_part2
    return func


def determine_runner():
    temp_list = filter(get_valid_args, sys.argv[1:])
    singles, pairs = partition(lambda token: ':' in token, temp_list)

    runner = dict(x.split(':') for x in pairs)
    runner = {int(k): int(v) for k, v in runner.items()}
    for x in singles:
        runner[int(x)] = 0

    callers = list(map(change_to_funcs, runner.items()))
    for m in callers:
        m()


if __name__ == '__main__':
    determine_runner()
