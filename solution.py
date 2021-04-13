class Solution:
    def __init__(self, n: int):
        self.n = n

    def solve(self):
        self.n += 1

    def input(self):
        self.n = int(input())

    def __str__(self):
        return f"n: {self.n}"
