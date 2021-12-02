import sys
input = sys.stdin.readline

def solution(N, number):
    if N == number:
        return 1

    cache = [set() for _ in range(9)]
    # N, NN, NNN, NNNN ...
    for i in range(1, 9):
        cache[i].add(int(str(N) * i))

    for i in range(1, 9):
        for j in range(1, i):
            for k in cache[j]:
                for a in cache[i - j]:
                    cache[i].add(k + a)
                    cache[i].add(k - a)
                    cache[i].add(k * a)
                    if a != 0:
                        cache[i].add(k // a)
        if number in cache[i]:
            return i

    return -1
print(solution(5,12))