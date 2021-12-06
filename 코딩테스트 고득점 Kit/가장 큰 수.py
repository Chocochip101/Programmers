from itertools import permutations
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True,key=lambda x: x * 3)

    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))

