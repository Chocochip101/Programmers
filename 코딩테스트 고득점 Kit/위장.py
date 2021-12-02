def solution(clothes):
    cloth_dict = {}
    for c, a in clothes:
        if a in cloth_dict.keys():
            cloth_dict[a].append(c)
        else:
            cloth_dict.setdefault(a, [c])
    answer = 1
    for a in cloth_dict:
        answer *= len(cloth_dict[a]) + 1
    return answer - 1

print(solution([["crowmask", "face"]]))