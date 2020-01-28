# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     trucks = deque(truck_weights)
#     n_trucks = len(truck_weights)
#     passing_sec = [0 for _ in truck_weights]
#     passed = []
#     passing = []
#
#     i = 0
#     j = -1
#     while len(passed) < n_trucks:
#         if len(trucks) > 0 and sum(passing) + trucks[0] <= weight:
#             passing.append(trucks.popleft())
#             j += 1
#
#         passing_sec[:j+1] = map(lambda x: x+1, passing_sec[:j+1])
#
#         if passing_sec[i] == bridge_length:
#             passed.append(passing[0])
#             passing = passing[1:]
#             i += 1
#
#     return passing_sec[0] + 1


def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    n_trucks = len(truck_weights)
    passing_sec = [0 for _ in truck_weights]
    passed = []
    passing = []

    i = 0
    j = -1
    current_weight = 0
    while len(passed) < n_trucks:
        if len(trucks) > 0 and current_weight + trucks[0] <= weight:
            t = trucks.popleft()
            passing.append(t)
            current_weight += t
            j += 1

        passing_sec[:j+1] = map(lambda x: x+1, passing_sec[:j+1])

        if passing_sec[i] == bridge_length:
            current_weight -= passing[0]
            passed.append(passing[0])
            passing = passing[1:]
            i += 1

    return passing_sec[0] + 1


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
