from collections import deque
def cnt(s1, s2):
    res = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            res += 1
    return res

def solution(begin, target, words):
    if target not in words:
        return 0
    word_dict = {}
    for s in words:
        word_dict.setdefault(s, 0)
    word_dict.setdefault(begin, 0)
    q = deque()
    q.append(begin)
    while q:
        now = q.pop()
        if now == target:
            return word_dict[target]
        for word in words:
            if word_dict[word] == 0 and cnt(word, now) == 1:
                word_dict[word] = word_dict[now] + 1
                q.append(word)
    return 0

print(solution("hit",  "cog",["hot", "dot", "dog", "lot", "log", "cog"]	))