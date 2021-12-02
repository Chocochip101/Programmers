def solution(genres, plays):
    songs_dict = {}
    sum_dict = {}
    for i in range(len(genres)):
        if genres[i] in songs_dict.keys():
            songs_dict[genres[i]].append((plays[i], i))
            sum_dict[genres[i]] += plays[i]
        else:
            songs_dict.setdefault(genres[i], [(plays[i], i)])
            sum_dict.setdefault(genres[i], plays[i])
    sum_list = sorted(sum_dict.items(), key=lambda x:x[1], reverse=True)
    answer = []
    for g, _ in sum_list:
        songs_dict[g].sort(reverse=True, key=lambda x: (int(x[0]), int(x[1])))
        for i in range(len(songs_dict[g])):
            if i == 2: break
            answer.append(songs_dict[g][i][1])
    return answer
