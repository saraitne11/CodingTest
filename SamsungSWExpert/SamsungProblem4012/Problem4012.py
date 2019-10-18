"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE
4012. [모의 SW 역량테스트] 요리사
"""


def get_synergy(mtx, foods):
    v = 0
    for i in foods:
        for j in foods:
            if i != j:
                v += mtx[i][j]
    return v


def solution(mtx, n):
    nn = n//2
    combis = []

    def search(visited, s):
        if len(visited) == nn:
            set_a = visited
            set_b = list(range(n))
            for k in set_a:
                set_b.remove(k)
            return combis.append([set_a, set_b])
        else:
            for i in range(s, n):
                if i not in visited:
                    search(visited + [i], i+1)

    search([0], 1)

    values = []
    for set_a, set_b in combis:
        va = get_synergy(mtx, set_a)
        vb = get_synergy(mtx, set_b)
        values.append(abs(va-vb))

    return min(values)


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        n = int(input().rstrip())
        mtx = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
        print('#%d %d' % (t+1, solution(mtx, n)))


if __name__ == '__main__':
    main()
