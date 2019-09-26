"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo
무선 충전
"""
NOMOVE = (0, 0)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

PERSON1_START = (1, 1)
PERSON2_START = (10, 10)

MAP_SIZE = (11, 11)

UDLR = (UP, DOWN, LEFT, RIGHT)   # Up Down Left Right
MOVE = {0: NOMOVE, 1: UP, 2: RIGHT, 3: DOWN, 4: LEFT}


def move2location(start, moves):
    x_cur, y_cur = start
    loc = [(x_cur, y_cur)]
    for m in moves:
        x_cur += MOVE[m][0]
        y_cur += MOVE[m][1]
        loc.append((x_cur, y_cur))
    return loc


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        # 이동시간 m, 충전기 개수 a
        m, a = list(map(int, input().rstrip().split(' ')))
        person1 = list(map(int, input().rstrip().split(' ')))
        person2 = list(map(int, input().rstrip().split(' ')))

        if len(person1) != m or len(person2) != m:
            raise ValueError('len(person1) = %d,  len(person2) = %d,  m = %d'
                             % (len(person1), len(person2), m))
        chargers = []
        for _ in range(a):
            x, y, c, p = list(map(int, input().rstrip().split(' ')))
            chargers.append({'X': x, 'Y': y, 'C': c, 'P': p})

        print(person1)
        print(move2location(PERSON1_START, person1))
        print(person2)
        print(move2location(PERSON2_START, person2))
        print(chargers)
        break


if __name__ == '__main__':
    main()