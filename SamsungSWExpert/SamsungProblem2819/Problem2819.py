"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE
2819. 격자판의 숫자 이어 붙이기
"""

SIZE = 4
N_VISIT = 7
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_matrix(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False


def dfs(grid):
    numbers = []

    def search(ci, cj, n, visited):
        if n == 7:
            num = int(''.join(visited))
            if num not in numbers:
                numbers.append(num)
            return
        else:
            for di, dj in MOVES:
                newi = ci + di
                newj = cj + dj
                if in_matrix(newi, newj, SIZE, SIZE):
                    new_visited = visited + [grid[newi][newj]]
                    search(newi, newj, n+1, new_visited)

    for i in range(SIZE):
        for j in range(SIZE):
            search(i, j, 1, [grid[i][j]])

    return len(numbers)


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        grid = [list(input().rstrip().split(' ')) for _ in range(SIZE)]
        print('#%d %d' % (t+1, dfs(grid)))
    return


if __name__ == '__main__':
    main()