def solution(numbers, target):
    cnt = [0]

    def search(c_num, c_val):
        if len(c_num) == 0:
            if c_val == target:
                cnt[0] += 1
                return
        else:
            v = c_num.pop(0)
            search(c_num[:], c_val + v)
            search(c_num[:], c_val - v)

    search(numbers, 0)

    return cnt[0]