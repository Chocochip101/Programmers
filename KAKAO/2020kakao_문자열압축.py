import sys
input = sys.stdin.readline

def solution(s):
    answer = 987654321
    for i in range(1, len(s)//2 + 1):
        res = ''
        cnt = 1
        token = s[:i]
        for j in range(i, len(s), i):
            #중복 계산
            if token == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += token
                else:
                    res += str(cnt) + token
                token = s[j: j + i]
                cnt = 1
        if cnt == 1:
            res += token
        else:
            res += str(cnt) + token
        answer = min(answer, len(res))
    return answer


s = input().rstrip()
print(solution(s))