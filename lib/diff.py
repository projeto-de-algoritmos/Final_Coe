"""
    Longest common subsequence module
    Créditos para Alex Dzyoba
"""
from typing import List

class Diff:
    def lcslen(self, x: str, y: str) -> List:
        lookup = [[0]* (len(y) + 1)] * (len(x) + 1)

        for i, xi in enumerate(x):
            for j, yj in enumerate(y):
                if xi == yj:
                    lookup[i][j] = 1 + lookup[i-1][j-1]
                else:
                    lookup[i][j] = max(lookup[i][j-1], lookup[i-1][j])
        return lookup

    def backtrack(self, lookup: List, x: str, y: str, i: int, j: int):
        if i == -1 or j == -1:
            return ""
        elif x[i] == y[j]:
            return self.backtrack(lookup, x, y, i-1, j-1) + x[i]
        elif lookup[i][j-1] >= lookup[i-1][j]:
            return self.backtrack(lookup, x, y, i, j-1)
        elif lookup[i][j-1] < lookup[i-1][j]:
            return self.backtrack(lookup, x, y, i-1, j)

    def lcs(self, x: str, y: str):
        lookup = self.lcslen(x, y)
        return self.backtrack(lookup, x, y, len(x)-1, len(y)-1)