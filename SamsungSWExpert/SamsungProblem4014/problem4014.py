"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH
활주로 건설
"""
from pprint import pprint


def get_column(matrix, i):
    return list(map(lambda x: x[i], matrix))    # x는 matrix의 각 행


def check(line, x):
    i = 1
    n = len(line)
    temp = line[:]                  # 원본 복사
    slope = [0 for _ in temp]
    while i < n:
        if temp[i] == temp[i-1]:    # 현재랑 이전이랑 높이 같은 경우
            i += 1
        else:
            dif = temp[i] - temp[i-1]
            if abs(dif) > 1:    # 높이 차이가 2 이상 일 경우 활주로 건설 불가
                return 0
            elif dif == 1:      # 현재가 이전보다 1 높을 경우
                if i < x:       # 이전 블럭들이 경사로보다 짧음
                    return 0
                else:
                    height = temp[i-1]
                    for j in range(i-x, i-1):                       # temp[i-1] 값이 x만큼 연속 되는지?
                        if temp[j] != height or slope[j] == 1:      # 이미 경사로 설치 됐는지?
                            return 0
                    slope[i-x:i] = [1 for _ in range(x)]        # 경사로 설치했으면 표시
                    i += 1
            elif dif == -1:     # 현재가 이전보다 1 낮을 경우
                if i+x > n:     # 남은 블럭들이 경사로 보다 짧음
                    return 0
                else:
                    height = temp[i]
                    for j in range(i+1, i+x):
                        if temp[j] != height:
                            return 0
                    slope[i:i+x] = [1 for _ in range(x)]        # 경사로 설치했으면 표시
                    i = i + x
    return 1


def main():
    test_cases = int(input())
    for t in range(test_cases):
        n, x = list(map(int, input().rstrip().split(' ')))
        ground = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]

        # print(n, x)
        # pprint(ground)
        cnt = 0
        for i in range(n):
            cnt += check(ground[i], x)                  # row check
            # print('row %d %d' % (i, check(ground[i], x)))
            cnt += check(get_column(ground, i), x)      # column check
            # print('column %d %d' % (i, check(get_column(ground, i), x)))

        print('#%d %d' % (t+1, cnt))

    # print(check([3, 3, 3, 2, 2, 1], 2))


if __name__ == "__main__":
    main()
