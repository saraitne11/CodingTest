"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo
무선 충전
"""
NOMOVE = (0, 0)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

PERSON1_START = (0, 0)
PERSON2_START = (9, 9)

MOVE = {0: NOMOVE, 1: UP, 2: RIGHT, 3: DOWN, 4: LEFT}


def move2location(start, moves):
    x_cur, y_cur = start
    loc = [(x_cur, y_cur)]
    for m in moves:
        x_cur += MOVE[m][0]
        y_cur += MOVE[m][1]
        loc.append((x_cur, y_cur))
    return loc


def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def get_available(position, chargers):
    avail = []
    for c in chargers:
        d = distance(position, c['XY'])
        if c['C'] >= d:
            avail.append(c)
    return avail


def search(p1_chargers, p2_chargers):
    p1_max = 0
    p2_max = 0
    total_max = 0
    for p1 in p1_chargers:
        for p2 in p2_chargers:
            if p1['XY'] == p2['XY']:
                p1_power = p1['P'] // 2
                p2_power = p2['P'] // 2
            else:
                p1_power = p1['P']
                p2_power = p2['P']

            if total_max < (p1_power + p2_power):
                total_max = p1_power + p2_power
                p1_max = p1_power
                p2_max = p2_power
    return p1_max, p2_max


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        # 이동시간 m, 충전기 개수 a
        move, num_charger = list(map(int, input().rstrip().split(' ')))
        person1 = list(map(int, input().rstrip().split(' ')))
        person2 = list(map(int, input().rstrip().split(' ')))

        chargers = []
        for _ in range(num_charger):
            x, y, c, p = list(map(int, input().rstrip().split(' ')))
            chargers.append({'XY': (x-1, y-1), 'C': c, 'P': p})

        p1_move = move2location(PERSON1_START, person1)
        p2_move = move2location(PERSON2_START, person2)

        # print(person1)
        # print(move2location(PERSON1_START, person1))
        # print(person2)
        # print(move2location(PERSON2_START, person2))
        # print(chargers)

        total_power = []

        for p1_m, p2_m in zip(p1_move, p2_move):
            p1_chargers = get_available(p1_m, chargers)
            p2_chargers = get_available(p2_m, chargers)
            if len(p1_chargers) >= 1 and len(p2_chargers) >= 1:
                # 만약 충전가능한 충전기가 각각 1개 씩 이상이라면,
                # 충전기 조합들 중 가장 최댓값을 찾아오는 로직으로
                total_power.append(search(p1_chargers, p2_chargers))
            else:
                if len(p1_chargers) == 0:
                    # 가능한 충전기가 없으면 0
                    p1 = 0
                else:
                    # p1의 가능한 충전기 중에 최댓값
                    p1 = max(list(map(lambda charger: charger['P'], p1_chargers)))
                if len(p2_chargers) == 0:
                    # 가능한 충전기가 없으면 0
                    p2 = 0
                else:
                    # p2의 가능한 충전기 중에 최댓값
                    p2 = max(list(map(lambda charger: charger['P'], p2_chargers)))
                total_power.append((p1, p2))
        # print(total_power)
        # print(len(total_power))
        # print(len(p1_move))
        # print(len(p2_move))
        p1_total = sum(list(map(lambda item: item[0], total_power)))
        p2_total = sum(list(map(lambda item: item[1], total_power)))
        final = p1_total + p2_total
        print('#%d %d' % (t+1, final))
    return


if __name__ == '__main__':
    main()
