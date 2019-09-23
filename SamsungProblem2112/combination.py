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
    # print(output)


combination([1, 2, 3, 4, 5], 2)
