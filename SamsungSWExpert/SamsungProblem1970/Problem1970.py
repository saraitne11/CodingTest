"""
쉬운 거스름돈
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq
"""

CURRENCY = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


def dfs_backtracking(money):

    min_coins = 100000
    solution_coins = []

    def search(remain, coins, idx):
        nonlocal min_coins
        nonlocal solution_coins

        new_coins = coins + [CURRENCY[idx]]
        new_remain = remain - CURRENCY[idx]
        if len(new_coins) < min_coins:
            if new_remain == 0:
                min_coins = len(new_coins)
                solution_coins = new_coins
                return
            elif new_remain < 0:
                search(remain, coins[:], idx+1)
            elif new_remain > 0:
                search(new_remain, new_coins, idx)
        else:
            return
        # print(min_coins, remain, coins)

    search(money, [], 0)

    cnt = [0 for _ in CURRENCY]
    for coin in solution_coins:
        cnt[CURRENCY.index(coin)] += 1

    return cnt


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        money = int(input().rstrip())
        money = money//10 * 10      # 1단위 제거
        cnt_coins = dfs_backtracking(money)
        print('#%d' % (t+1))
        for c in cnt_coins:
            print('%d' % c, end=' ')
        print()


if __name__ == '__main__':
    main()
