import sys
input = sys.stdin.readline
key_pad = {
    0: [3, 1],
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    '*': [3, 0],
    '#': [3, 2],
}
def dist(a: list, b: list):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def solution(numbers, hand):
    left_hand = key_pad['*']
    right_hand = key_pad['#']
    answer = ''
    for now in numbers:
        if now == 1 or now == 4 or now == 7:
            left_hand = key_pad[now]
            answer += 'L'
        elif now == 3 or now == 6 or now == 9:
            right_hand = key_pad[now]
            answer += 'R'
        else:
            if dist(left_hand, key_pad[now]) > dist(right_hand, key_pad[now]):
                right_hand = key_pad[now]
                answer += 'R'
            elif dist(left_hand, key_pad[now]) < dist(right_hand, key_pad[now]):
                left_hand = key_pad[now]
                answer += 'L'
            else:
                if hand == 'right':
                    right_hand = key_pad[now]
                    answer += 'R'
                else:
                    left_hand = key_pad[now]
                    answer += 'L'

    return answer
