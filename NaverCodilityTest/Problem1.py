"""
saddle point
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def get_column(matrix, c):
    # x에 한 행 씩 들어가고 각 행의 column c 의 값을 가져와서 리스트로
    return list(map(lambda x: x[c], matrix))


def solution(A):
    n = len(A)
    m = len(A[0])
    cnt = 0

    for i in range(1, n-1):
        for j in range(1, m-1):
            row_values = [A[i][j-1], A[i][j], A[i][j+1]]
            row_min = min(row_values)
            row_max = max(row_values)

            col_values = [A[i-1][j], A[i][j], A[i+1][j]]
            col_min = min(col_values)
            col_max = max(col_values)

            if A[i][j] == row_min and A[i][j] == col_max:
                # print(i, j, A[i][j])
                cnt += 1
            elif A[i][j] == row_max and A[i][j] == col_min:
                # print(i, j, A[i][j])
                cnt += 1
            else:
                pass
    return cnt
