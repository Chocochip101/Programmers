def solution(id_list, report, k):
    # 사용자가 신고한 타사용자들
    report_list = {}
    # 신고 당한 횟수
    report_count = {}
    # Dict에서 리스트 정답으로 변환을 위한 딕셔너리
    answer_dict = {}
    
    # 초기화
    for n in id_list:
        report_list[n] = []
        report_count[n] = 0
        answer_dict[n] = 0
    
    for rep in report:
        a, b = rep.split()
        # 이미 신고한 전적이 있으면 continue
        if b in report_list[a]:
            continue
        # 신고한 적이 없으면 append & count
        report_list[a].append(b)
        report_count[b] += 1
    # k번 이상 신고 당한 사용자 
    for reported in [b for b in report_count if report_count[b] >= k]:
        for reportee in id_list:
            if reported in report_list[reportee]:
                answer_dict[reportee] += 1

    answer = [0 for _ in range(len(id_list))]  
    # List로 변환
    for i in range(len(id_list)):
        answer[i] = answer_dict[id_list[i]]
    return answer