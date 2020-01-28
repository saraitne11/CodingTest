# https://programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    n = len(prices)
    answer = [0 for _ in prices]

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            # print(i, j)
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer[i] = cnt

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))
