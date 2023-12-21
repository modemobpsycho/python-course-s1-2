def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    lst = []
    for i in range(size):
        lst.append([0] * size)
    for i in range(size):
        for j in range(size):
            if i == j:
                lst[i][j] = j + 1
            elif i < j:
                lst[i][j] = up_fill
            elif i > j:
                lst[i][j] = down_fill
    return lst
