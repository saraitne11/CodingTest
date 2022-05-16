"""
부분집합
"""


def get_subset(_set):
    n = len(_set)
    _subset = []

    def search(a, k):
        if k == n:
            temp = []
            for i in range(n):
                if a[i] == 1:
                    temp.append(_set[i])
            _subset.append(temp)
            return
        else:
            a[k] = 0
            search(a[:], k+1)
            a[k] = 1
            search(a[:], k+1)
            return

    aa = [0 for _ in range(n)]
    search(aa, 0)

    return _subset


def main():

    import time
    s = time.time()

    my_set = ['A', 'B', 'C']
    # my_set = list(range(20))
    my_subset = get_subset(my_set)
    print(my_subset)
    print(len(my_subset))

    print(time.time() - s)


if __name__ == '__main__':
    main()
