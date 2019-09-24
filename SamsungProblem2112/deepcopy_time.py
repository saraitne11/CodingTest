from copy import deepcopy
import time


def zeros_list(n: int, m: int) -> list:
    row = [0 for _ in range(n)]
    mtx = [row[:] for _ in range(m)]
    # mtx = [deepcopy(row) for _ in range(m)]
    # mtx = [row for _ in range(m)]     모든 row가 같은 주소를 참조하게 되서 mtx[i][j]만 수정해도 mtx[i][:]가 바뀜
    return mtx


a = zeros_list(13, 20)


s = time.time()
for i in range(10):
    b = deepcopy(a)
print(time.time() - s)
