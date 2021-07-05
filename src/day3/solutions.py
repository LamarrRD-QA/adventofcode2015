from src.solution_template import Solver

FILENAME = 'resources/input_day3.txt'


class DayThree(Solver):
    MOVES = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, 1),
        "v": (0, -1)
    }

    def solve_part1(self):
        with open(FILENAME) as f:
            visited = [(0, 0)]

            while True:
                direction = f.read(1)
                if not direction:
                    break

                visited.append((visited[-1][0] + self.MOVES[direction][0], visited[-1][1] + self.MOVES[direction][1]))

            print("Solution for Day 3, Part 1 is: {}".format(len(set(visited))))

    def solve_part2(self):

        santa_visited = [(0, 0)]
        robot_santa_visited = [(0, 0)]

        with open(FILENAME) as f:
            while True:
                data = f.read(2)
                if len(data) == 1:
                    santa_visited.append(
                        (santa_visited[-1][0] + self.MOVES[data][0],
                         santa_visited[-1][1] + self.MOVES[data][1]))
                    break
                if not data:
                    break

                [santa_direction, robot_santa_direction] = [c for c in data]

                santa_visited.append(
                    (santa_visited[-1][0] + self.MOVES[santa_direction][0],
                     santa_visited[-1][1] + self.MOVES[santa_direction][1]))
                robot_santa_visited.append(
                    (robot_santa_visited[-1][0] + self.MOVES[robot_santa_direction][0],
                     robot_santa_visited[-1][1] + self.MOVES[robot_santa_direction][1]))

        final_list = list(set(santa_visited) | set(robot_santa_visited))
        print("Solution for Day 3, Part 2 is: {}".format(len(final_list)))
