# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
from math import ceil


def solution(progresses, speeds):
    answer = []
    prog_speed = list(zip(progresses, speeds))

    while prog_speed:
        prog_speed = list(map(lambda x: (x[0]+x[1], x[1]), prog_speed))

        if prog_speed[0][0] >= 100:
            dist = [prog_speed[0]]
            for i in range(1, len(prog_speed)):
                if prog_speed[i][0] < 100:
                    break
                else:
                    dist.append(prog_speed[i])

            answer.append(len(dist))
            for d in dist:
                prog_speed.remove(d)

    return answer


if __name__ == '__main__':
    print(solution([93,30,55], [1,30,5]))