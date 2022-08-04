def solution(id_list, report, k):
    report_list = {}
    report_count = {}
    answer_dict = {}
    for n in id_list:
        report_list[n] = []
        report_count[n] = 0
        answer_dict[n] = 0
    for rep in report:
        a, b = rep.split()
        if b in report_list[a]:
            continue
        report_list[a].append(b)
        report_count[b] += 1
    for reported in [b for b in report_count if report_count[b] >= k]:
        for reportee in id_list:
            if reported in report_list[reportee]:
                answer_dict[reportee] += 1
    print(report_count) 
    answer = [0 for i in range(len(id_list))]  
    for i in range(len(id_list)):
        answer[i] = answer_dict[id_list[i]]
    return answer