"""
Counting Elements

You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""
import time
import random


def solution(N, A):
    # 66 점 (Time out)
    # Detected time complexity: O(N*M)
    counters = [0 for _ in range(N)]
    max_val = 0
    for a in A:
        a = a - 1
        if a >= N:
            counters = [max_val for _ in range(N)]
        else:
            counters[a] += 1
            if max_val < counters[a]:
                max_val = counters[a]
        # print(counters)
    return counters


def solution2(N, A):
    # 100 점
    # Detected time complexity: O(N + M)
    counters = [0 for _ in range(N)]
    current_max = 0
    done_max = 0
    for a in A:
        a = a - 1
        if a >= N:
            # counters = [max_val for _ in range(N)]
            done_max = current_max
        else:
            if counters[a] < done_max:
                counters[a] = done_max
            counters[a] += 1
            if current_max < counters[a]:
                current_max = counters[a]
            # print(counters)
    if done_max > 0:
        for i in range(N):
            if counters[i] < done_max:
                counters[i] = done_max
    return counters


def get_random_list(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]


s = time.time()
print(solution(100000, get_random_list(10000000, 1, 100001)))
print(time.time() - s)
s = time.time()
print(solution2(100000, get_random_list(10000000, 1, 100001)))
print(time.time() - s)


print(solution2(5, [3, 4, 4, 6, 1, 4, 4]))

