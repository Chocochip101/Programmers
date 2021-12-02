def solution(answers):
    math = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    cnt = [0] * 3
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == math[i][j % len(math[i])]:
                cnt[i] += 1
    max_cnt = max(cnt)
    answer = []
    for i in range(3):
        if max_cnt == cnt[i]:
            answer.append(i+1)
    return answer