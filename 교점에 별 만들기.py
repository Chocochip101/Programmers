import sys
import math
input = sys.stdin.readline
from itertools import combinations


def solution(line):
    min_x = float('inf')
    min_y = float('inf')
    max_x = -float('inf')
    max_y = -float('inf')
    star_coord = set()
    for line1, line2 in combinations(line, 2):
        A, B, E = line1
        C, D, F = line2
        if A * D == B * C:
            continue
        if (B * F - E * D) % (A * D - B * C) == 0 and (E * C - A * F) % (A * D - B * C) == 0:
            x = (B * F - E * D) // (A * D - B * C)
            y = (E * C - A * F) // (A * D - B * C)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

            star_coord.add((x, y))

    answer = []
    for y in range(max_y, min_y - 1, -1):
        s = []
        for x in range(min_x, max_x + 1):
            if (x, y) in star_coord:
                s.append('*')
            else:
                s.append(".")
        answer.append("".join(s))
    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))