"""
파이썬 SW문제해결 응용_구현 - 05 백트래킹
5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
"""


def dfs(n, mtx):
    min_cost = 15*99

    def search(cost, visited):
        nonlocal min_cost
        nonlocal n
        # print(cost, visited)
        if len(visited) == n:
            if cost < min_cost:
                min_cost = cost
                # print(visited)
                return
        else:
            row = len(visited)
            for i in range(n):
                if i not in visited:
                    new_cost = cost + mtx[row][i]
                    if new_cost < min_cost:
                        search(new_cost, visited + [i])

    for _i in range(n):
        search(mtx[0][_i], [_i])
    return min_cost


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        n = int(input().rstrip())
        mtx = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
        print('#%d %d' % (t+1, dfs(n, mtx)))


if __name__ == '__main__':
    main()
