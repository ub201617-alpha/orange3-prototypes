import numpy
initial_matrix = [[0, 5, 9, 9, 8],
                  [5, 0, 10, 10, 9],
                  [9, 10, 0, 8, 7],
                  [9,	10,	8, 0, 3],
                  [8, 9, 7, 3, 0]]
print("Initial matrix:\n",initial_matrix)

n = len(initial_matrix)
q_matrix = numpy.zeros(shape=(n, n))

for i in range(0,n):
    for j in range(0,n):
        if i != j:
            q = (n - 2) * initial_matrix[i][j] - sum(initial_matrix[i]) - sum(initial_matrix[j])
            q_matrix[i][j] = q
print("Q matrix:\n", q_matrix)
min_x, min_y = numpy.unravel_index(q_matrix.argmin(), q_matrix.shape)
print("Joining index ", min_x, " and ", min_y)
fu = (0.5 * initial_matrix[min_x][min_y] + 1 / (2 * (n - 2)) * (sum(initial_matrix[min_x]) - sum(initial_matrix[min_y])))
gu = initial_matrix[min_x][min_y] - fu

new_matrix = numpy.zeros(shape=(n - 1, n - 1))
old_indexes = list(range(0,n))
old_indexes.remove(min_x)
old_indexes.remove(min_y)
for i in range(0,len(old_indexes)):
    for j in range(0,len(old_indexes)):
        if i != j:
            new_matrix[i + 1][j + 1] = initial_matrix[old_indexes[i]][old_indexes[j]]

for i in range(0,len(old_indexes)):
    d = 0.5 * (initial_matrix[min_x][old_indexes[i]] + initial_matrix[min_y][old_indexes[i]] - initial_matrix[min_x][min_y])
    new_matrix[0][i + 1] = d
    new_matrix[i + 1][0] = d
print("Final matrix: \n", new_matrix)


