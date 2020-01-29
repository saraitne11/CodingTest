# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3


def conv(number, base):
    T = "412"
    i, j = divmod(number, base)

    if i == 0:
        return T[j]
    else:
        return conv(i, base) + T[j]


def solution(n):
    answer = ''
    a = conv(8, 3)
    print(a)
    return answer


if __name__ == '__main__':
    solution(0)