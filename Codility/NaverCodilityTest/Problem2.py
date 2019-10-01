"""
messages split
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, K):
    words = S.split(' ')
    n_words = len(words)
    for word in words:
        if len(word) > K:
            return -1

    cnt = 0
    start = 0
    end = 1
    # sms = []
    while end <= n_words:
        sent_words = words[start:end]
        sent = ' '.join(sent_words)
        if len(sent) > K:
            # sms.append(sent_words[:-1])
            cnt += 1
            start = end - 1
            end = start + 1
        else:
            end += 1
    # sms.append(words[start:end])    # remainder
    # print(sms)
    return cnt + 1


# print(solution('SMS messages are really short', K=12))
print(solution('SMS messages are really short', K=10))