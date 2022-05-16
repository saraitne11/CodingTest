# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    pri = deque(priorities)
    idx = deque([i for i in range(len(priorities))])
    answer = 0

    while True:
        c_pri = pri.popleft()
        c_idx = idx.popleft()
        if list(filter(lambda x: x > c_pri, pri)):
            pri.append(c_pri)
            idx.append(c_idx)
        else:
            answer += 1
            if c_idx == location:
                break

    return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
