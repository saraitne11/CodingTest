# https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3


def solution(arrangement):
    cnt = 0
    bar = 0
    arrangement = arrangement.replace('()', '0')

    for a in arrangement:
        if a == '(':
            cnt += 1
            bar += 1
        elif a == ')':
            bar -= 1
        elif a == '0':
            cnt += bar
        else:
            return -1
    return cnt


if __name__ == '__main__':
    print(solution('()(((()())(())()))(())'))
