import sys
from itertools import permutations
import math

def isPrime(num):
    if(num <= 1): return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    prime_candidates = []
    answer = []
    for i in range(1, len(numbers) + 1):
        prime_candidates += [''.join(k) for k in permutations(numbers, i)]

    prime_candidates = [int(n) for n in prime_candidates]
    for i in prime_candidates:
        if(isPrime(i)):
            answer.append(i)

    return len(set(answer))

print(solution('011'))