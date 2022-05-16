# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3
from collections import deque


def one_diff(word1, word2):
    cnt = 0
    for a, b in zip(word1, word2):
        if a != b:
            cnt += 1
        if cnt > 1:
            break
    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0

    visit = []
    queue = deque([(begin, 0)])

    while queue:
        node, level = queue.popleft()

        if node == target:
            answer = level
            break

        if node not in visit:
            visit.append(node)
            adj = list(filter(lambda x: one_diff(node, x), words))
            adj = list(map(lambda x: (x, level + 1), adj))
            queue.extend(adj)

    return answer


if __name__ == '__main__':
    print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
