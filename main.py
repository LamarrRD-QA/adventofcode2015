import sys
from more_itertools import partition


def validate_list(elem):
    if ':' in elem:
        [lhs_str, rhs_str] = elem.split(':', 1)
        try:
            lhs = int(lhs_str)
            rhs = int(rhs_str)
        except ValueError:
            return False
        if 1 <= lhs <= 25 and 0 <= rhs <= 2:
            return True
    else:
        try:
            day = int(elem)
        except ValueError:
            return False
        if 1 <= day <= 25:
            return True


def determine_runner():
    temp_list = filter(validate_list, sys.argv[1:])
    singles, pairs = partition(lambda token: ':' in token, temp_list)

    runner = dict(x.split(':') for x in pairs)
    runner = {int(k): int(v) for k, v in runner.items()}
    for x in singles:
        runner[int(x)] = 0
    print(runner)


if __name__ == '__main__':
    determine_runner()
