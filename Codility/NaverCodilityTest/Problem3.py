# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque

# CALL_RM = 0


def is_sorted(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True


def rm_char(s, i):
    # global CALL_RM
    # CALL_RM += 1
    return s[:i] + s[i+1:]


def solution(S):
    if is_sorted(S):
        return 0

    cnt = 1
    queue = deque()
    visited = []
    for i in range(len(S)):
        s = rm_char(S, i)
        if is_sorted(s):
            # print(queue)
            # print(s)
            return cnt
        else:
            if s not in visited:
                visited.append(s)
                queue.append((s, cnt))

    while queue:
        s, c = queue.popleft()
        for i in range(len(s)):
            new_c = c + 1
            new_s = rm_char(s, i)
            if is_sorted(new_s):
                # print(queue)
                # print(new_s)
                return new_c
            else:
                if new_s not in visited:
                    visited.append(new_s)
                    queue.append((new_s, new_c))

    return -999


print(solution('dkfaajhskccudhv'))
# print(CALL_RM)
