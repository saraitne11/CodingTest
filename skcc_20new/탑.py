# https://programmers.co.kr/learn/courses/30/lessons/42588?language=python3


def solution(heights):
    rx = [0 for _ in heights]

    while heights:
        right = heights.pop()
        for idx in range(len(heights)-1, -1, -1):
            if heights[idx] > right:
                rx[len(heights)] = idx + 1
                break
    return rx


if __name__ == '__main__':
    print(solution([3,9,9,3,5,7,2]))