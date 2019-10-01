"""
순열
"""


def get_permutation(_set, n=None):
    if n is None:
        n = len(_set)
    p = []

    def search(visit, remain, cnt):
        if cnt == n:
            p.append(visit)
            return
        else:
            for i in range(len(remain)):
                new_remain = remain.copy()
                new_visited = visit + [new_remain.pop(i)]
                search(new_visited, new_remain, cnt+1)

    search([], _set, 0)
    return p


def main():
    import time

    # my_set = ['A', 'B', 'C', 'D']
    my_set = list(range(10))

    s = time.time()
    my_permu = get_permutation(my_set)
    # print(my_permu)
    print(len(my_permu))
    print(time.time() - s)

    s = time.time()
    from itertools import permutations
    print(len(list(permutations(my_set))))
    print(time.time() - s)


if __name__ == '__main__':
    main()
