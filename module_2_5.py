def get_matrix (n, m , value):
    matrix = []
    for row in range(n):
        matrix.append([])
        for colon in range(m):
            matrix[row].append(value)
    return matrix

result1 = get_matrix(3, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(5, 2, 13)
print(result1)
print(result2)
print(result3)
