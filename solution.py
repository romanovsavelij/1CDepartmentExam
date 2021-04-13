class Solution:
    def __init__(self):
        self.n = 1

    def input(self):
        self.n = int(input())

    def solve(self):
        self.n += 1
        print(self)

    def __str__(self):
        return f"n: {self.n}"
