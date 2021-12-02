import sys
input = sys.stdin.readline
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for dungeon in permutations(dungeons):
        now = k
        cnt = 0
        for minimum, use in dungeon:
            if minimum <= now:
                now -= use
            else: break
            cnt += 1
        answer = max(answer, cnt)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))