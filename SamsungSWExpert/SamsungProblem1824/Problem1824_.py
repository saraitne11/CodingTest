"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4yLUiKDUoDFAUx&categoryId=AV4yLUiKDUoDFAUx&categoryType=CODE
1824. 혁진이의 프로그램 검증
"""
from random import shuffle

LEFT = '<'
RIGHT = '>'
UP = '^'
DOWN = 'v'
UBAR = '_'
VBAR = '|'
QUE = '?'
DOT = '.'
AT = '@'
PLUS = '+'
MINUS = '-'

INTS = '0123456789'
MOVES_LIST = [UP, DOWN, RIGHT, LEFT]
MOVES = {DOWN: (1, 0), UP: (-1, 0), RIGHT: (0, 1), LEFT: (0, -1)}


def check_endpoint(programs):
    n = len(programs)
    m = len(programs[0])

    at_i, at_j = (-1, -1)

    for i in range(n):
        for j in range(m):
            if programs[i][j] == AT:
                at_i, at_j = i, j
                break
        if at_i >= 0 or at_j >= 0:
            break

    if at_i < 0 and at_j < 0:
        return False

    # @의 주위 1칸 씩만 연결되는지 확인
    arbitrary = QUE + DOT + PLUS + MINUS + INTS
    for move, didj in MOVES.items():
        di, dj = didj
        new_i, new_j = update_location(at_i, at_j, di, dj, n, m)
        code = programs[new_i][new_j]

        if code in arbitrary:
            return True
        elif move == UP:
            if code in DOWN + VBAR + arbitrary:
                return True
        elif move == DOWN:
            if code in UP + VBAR + arbitrary:
                return True
        elif move == LEFT:
            if code in RIGHT + UBAR + arbitrary:
                return True
        elif move == RIGHT:
            if code in LEFT + UBAR + arbitrary:
                return True
        else:
            pass
    return False


def update_location(i, j, di, dj, n, m):
    new_i = i + di
    if new_i < 0:
        new_i = n - 1
    elif new_i >= n:
        new_i = 0
    else:
        pass

    new_j = j + dj
    if new_j < 0:
        new_j = m - 1
    elif new_j >= m:
        new_j = 0
    else:
        pass

    return new_i, new_j


def dfs(program, n, m):

    if not check_endpoint(program):
        return 'NO'

    result = False
    call_cnt = 0

    def search(current, visited):
        nonlocal call_cnt
        nonlocal result
        call_cnt += 1

        if result:         # 이미 @에 당도한 노드가 있다면 탐색 종료
            return
        i, j, v, di, dj = current
        if current in visited:
            return
        else:
            new_visited = visited + [current]
            new_i, new_j = update_location(i, j, di, dj, n, m)
            code = program[new_i][new_j]

            print(call_cnt, code, current)
            if call_cnt >= 10000:
                from pprint import pprint
                pprint(program, width=len(str(list(program[0]))) + 3)
                import sys
                sys.exit(0)

            if code == AT:              # '@'
                result = True
                return

            elif code in MOVES_LIST:    # '>' or '<' or '^' or 'v'
                new_di, new_dj = MOVES[code]
                new_current = [new_i, new_j, v, new_di, new_dj]
                search(new_current, new_visited)

            elif code == UBAR:          # '_'
                if v == 0:
                    new_di, new_dj = MOVES[RIGHT]
                else:
                    new_di, new_dj = MOVES[LEFT]
                new_current = [new_i, new_j, v, new_di, new_dj]
                search(new_current, new_visited)

            elif code == VBAR:          # '|'
                if v == 0:
                    new_di, new_dj = MOVES[DOWN]
                else:
                    new_di, new_dj = MOVES[UP]
                new_current = [new_i, new_j, v, new_di, new_dj]
                search(new_current, new_visited)

            elif code == QUE:           # '?'
                temp = list(MOVES.values())
                shuffle(temp)
                for new_di, new_dj in temp:
                    new_current = [new_i, new_j, v, new_di, new_dj]
                    search(new_current, new_visited)

            elif code == DOT:           # '.'
                new_current = [new_i, new_j, v, di, dj]
                search(new_current, new_visited)

            elif code in INTS:          # in '0123456789'
                new_current = [new_i, new_j, int(code), di, dj]
                search(new_current, new_visited)

            elif code == PLUS:          # '+'
                new_v = v + 1
                if new_v > 15:
                    new_v = 0
                new_current = [new_i, new_j, new_v, di, dj]
                search(new_current, new_visited)

            elif code == MINUS:         # '-'
                new_v = v - 1
                if new_v < 0:
                    new_v = 15
                new_current = [new_i, new_j, new_v, di, dj]
                search(new_current, new_visited)

            else:
                raise ValueError('%s %s' % (code, [new_i, new_j, v, di, dj]))

    start_i, start_j = (0, 0)
    start_v = 0
    start_di, start_dj = RIGHT
    search([start_i, start_j, start_v, start_di, start_dj], [])

    # print(result)
    if result:
        return 'YES'
    else:
        return 'NO'


def main():
    test_cases = int(input())
    for t in range(test_cases):
        r, c = list(map(int, input().split(' ')))
        program = [list(input().rstrip()) for _ in range(r)]
        if t+1 == 51:
            from pprint import pprint
            pprint(program, width=len(str(list(program[0])))+3)
            print('#%d %s' % (t+1, dfs(program, r, c)))


if __name__ == '__main__':
    main()
