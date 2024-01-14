from abc import ABC, abstractmethod


class SolutionCommon(ABC):
    def __init__(self, user_input: str) -> None:
        self.lines = user_input.splitlines()

    @abstractmethod
    def solve(self) -> int:
        """Abstract method to solve the problem."""

    def end_digits(self, line: str) -> int:
        return int("".join([line[0], line[-1]]))

    def filter_digits(self, line: str):
        return "".join([char for char in line if char.isdigit()])


class Part1Solution(SolutionCommon):
    """Solution for 2023 Day 01 part 1"""

    def solve(self):
        line_digits = list(map(self.filter_digits, self.lines))
        first_and_last_digits = list(map(self.end_digits, line_digits))
        return sum(first_and_last_digits)


class Part2Solution(SolutionCommon):
    """Solution for 2023 Day 01 part 2"""

    def solve(self):
        with_word_numbers = list(map(self.replace_words, self.lines))
        line_digits = list(map(self.filter_digits, with_word_numbers))
        first_and_last_digits = list(map(self.end_digits, line_digits))
        return sum(first_and_last_digits)

    def replace_words(self, line: str) -> str:
        words = [
            ("one", "o1e"),
            ("two", "t2o"),
            ("three", "t3e"),
            ("four", "f4r"),
            ("five", "f5e"),
            ("six", "s6x"),
            ("seven", "s7n"),
            ("eight", "e8t"),
            ("nine", "n9e"),
        ]
        for word in words:
            line = line.replace(word[0], word[1])
        return line
