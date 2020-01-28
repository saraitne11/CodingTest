def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = 0
    j = len(people) - 1
    while True:
        if people[i] + people[j] > limit:
            i += 1
            answer += 1
        else:
            i += 1
            j -= 1
            answer += 1
        if i >= j:
            if i == j:
                answer += 1
            break
    return answer
