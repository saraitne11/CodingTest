"""
Counting Elements

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    # 66점
    # Detected time complexity: O(N**2)
    min_val = 1
    while True:
        if min_val in A:
            min_val += 1
        else:
            return min_val


def solution2(A):
    # 100점
    # Detected time complexity: O(N) or O(N * log(N))
    checker = dict()
    for a in A:
        if a not in checker:
            checker[a] = True
    min_val = 1
    while True:
        if min_val not in checker:
            return min_val
        else:
            min_val += 1


print(solution2([1, 3, 6, 4, 1, 2]))
print(solution2([1, 2, 3]))
print(solution2([-1, -3]))
