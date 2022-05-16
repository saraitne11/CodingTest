"""
조합
"""


def get_combination(_set, r=None):
    n = len(_set)
    if r is None:
        r = len(_set)
    c = []

    def search(visit, nn, rr):
        if rr == 0:
            c.append(visit)
            return
        elif nn < rr:
            return
        else:
            search(visit, nn-1, rr)
            search(visit + [_set[nn-1]], nn-1, rr-1)

    search([], n, r)
    return c


def main():
    import time

    # my_set = ['A', 'B', 'C']
    my_set = list(range(30))

    s = time.time()
    my_combi = get_combination(my_set, 4)
    # print(my_combi)
    print(len(my_combi))
    print(time.time() - s)

    # s = time.time()
    # from itertools import permutations
    # print(len(list(permutations(my_set))))
    # print(time.time() - s)


if __name__ == '__main__':
    main()
