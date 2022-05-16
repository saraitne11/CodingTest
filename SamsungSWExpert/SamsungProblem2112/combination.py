from itertools import combinations, product
from pprint import pprint


def combination(arr, r):
    # 1.
    arr = sorted(arr)
    output = []

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            output.append(chosen[:])
            return

        # 3.
        # start = arr.index(chosen[-1]) + 1 if chosen else 0
        if chosen:
            start = arr.index(chosen[-1]) + 1
        else:
            start = 0

        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()

    generate([])
    print(output)


aa = [1, 2, 3, 4, 5]
bb = ['A', 'B']

medicine = list(product(bb, repeat=3))
floor = list(combinations(aa, 3))

print(medicine)
print(floor)

for f in floor:
    for m in medicine:
        print(f, m)
