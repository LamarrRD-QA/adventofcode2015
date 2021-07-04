from abc import ABC, abstractmethod


class Solver(ABC):

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass

    def solve_all(self):
        self.solve_part1()
        self.solve_part2()
