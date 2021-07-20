from src.solution_template import Solver


class DayThree(Solver):

    filename = 'resources/input_day3.txt'

    moveset = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, 1),
        "v": (0, -1)
    }

    def solve_part1(self):
        with open(self.filename) as f:
            visited = [(0, 0)]

            while True:
                direction = f.read(1)
                if not direction:
                    break

                visited.append((visited[-1][0] + self.moveset[direction][0], visited[-1][1] + self.moveset[direction][1]))

            print("Solution for Day 3, Part 1 is: {}".format(len(set(visited))))

    def solve_part2(self):

        santa_visited = [(0, 0)]
        robot_santa_visited = [(0, 0)]

        with open(self.filename) as f:
            while True:
                data = f.read(2)
                if len(data) == 1:
                    santa_visited.append(
                        (santa_visited[-1][0] + self.moveset[data][0],
                         santa_visited[-1][1] + self.moveset[data][1]))
                    break
                if not data:
                    break

                [santa_direction, robot_santa_direction] = [c for c in data]

                santa_visited.append(
                    (santa_visited[-1][0] + self.moveset[santa_direction][0],
                     santa_visited[-1][1] + self.moveset[santa_direction][1]))
                robot_santa_visited.append(
                    (robot_santa_visited[-1][0] + self.moveset[robot_santa_direction][0],
                     robot_santa_visited[-1][1] + self.moveset[robot_santa_direction][1]))

        final_list = list(set(santa_visited) | set(robot_santa_visited))
        print("Solution for Day 3, Part 2 is: {}".format(len(final_list)))
