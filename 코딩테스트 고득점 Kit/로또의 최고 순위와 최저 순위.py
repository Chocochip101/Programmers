def CntToRank(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    elif cnt <= 1:
        return 6

def solution(lottos, win_nums):
    cnt = 0
    zeros = 0
    for num in lottos:
        if num == 0:
            zeros += 1
        else:
            if num in win_nums:
                cnt += 1

    answer = [CntToRank(zeros + cnt), CntToRank(cnt)]
    return answer


print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))