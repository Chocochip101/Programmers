def solution(citations):
    # 16 5 3 1 0
    citations.sort(reverse=True)
    for h in range(len(citations)):
        if h > citations[h]:
            return h
    return len(citations)
print(solution([3, 0, 6, 1, 5]))

