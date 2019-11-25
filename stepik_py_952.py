# creating empty matrix
matrix = []

# adding elements to matrix
while True:
    line = input()
    if line == 'end':
        break
    matrix.append([int(i) for i in line.split()])

# checking matrix size
n_size = len(matrix)
m_size = len(matrix[0])

# creating new same size matrix with all elements are zeros
new = [[0] * m_size for i in range(n_size)]

if n_size == 1 and m_size == 1:
    for i in range(n_size):
        for j in range(m_size):
            new[i][j] = matrix[i][j] + matrix[i][j] + matrix[i][j] + matrix[i][j]
elif n_size == 1:
    for i in range(n_size):
        for j in range(m_size):
            if j == m_size - 1:
                j -= m_size
            new[i][j] = matrix[i][j] + matrix[i][j] + matrix[i][j - 1] + matrix[i][j + 1]
elif m_size == 1:
    for i in range(n_size):
        for j in range(m_size):
            if i == n_size - 1:
                i -= n_size
            new[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j] + matrix[i][j]
else:
    x, y = 0, 0
    for i in range(n_size):
        x = i
        if i == n_size - 1:
            x = i - n_size
        for j in range(m_size):
            y = j
            if j == m_size - 1:
                y = j - m_size
            new[i][j] = matrix[x - 1][y] + matrix[x + 1][y] + matrix[x][y - 1] + matrix[x][y + 1]

for i in new:
    for j in i:
        print(j, end=" ")
    print()
