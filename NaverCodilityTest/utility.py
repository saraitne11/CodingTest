
def is_in_matrix(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False


def get_column(matrix, c):
    # x에 한 행 씩 들어가고 각 행의 column c 의 값을 가져와서 리스트로
    return list(map(lambda x: x[c], matrix))


def zeros_list(n: int, m: int) -> list:
    """
    :param n: number of row
    :param m: number of column
    :return: zeros list
    """
    row = [0 for _ in range(m)]
    mtx = [row[:] for _ in range(n)]
    # mtx = [deepcopy(row) for _ in range(m)]
    # mtx = [row for _ in range(m)]     모든 row가 같은 주소를 참조하게 되서 mtx[i][j]만 수정해도 mtx[i][:]가 바뀜
    return mtx
