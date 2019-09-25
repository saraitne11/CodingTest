"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
보물상자 비밀번호
"""


def shift(_list, d):
    return _list[-d:] + _list[:-d]


def split_hex(hex_seq: str, n):
    s = []
    for i in range(0, len(hex_seq), n):
        s.append(hex_seq[i:i+n])
    return s


def main():
    test_cases = int(input().rstrip())
    for t in range(test_cases):
        n, k = list(map(int, input().rstrip().split(' ')))
        hex_seq = input().rstrip()
        side_len = n//4
        # print(n, k)
        # print(n, k, num_hex)
        # print(split_hex(num_hex))
        nums = []
        for _ in range(side_len):
            nums.extend(list(map(lambda x: int(x, 16), split_hex(hex_seq, side_len))))
            # nums.extend(list(split_hex(hex_seq, side_len)))
            hex_seq = shift(hex_seq, 1)
        nums = list(set(nums))
        nums.sort(reverse=True)
        print('#%d %d' % (t+1, nums[k-1]))


if __name__ == '__main__':
    main()
