
def initialisation():
    matrix = [
        [1, 2, 1, 3],
        [1, -1, 2, -2],
        [4, 3, 2, 1]
    ]
    array = [1, 2, 3, 4]

    rows = len(matrix)
    cols = len(matrix[0])

    return matrix, array, rows, cols

def print_matrix_array(matrix, array):
    print("A: ")
    for row in matrix:
        print(row)

    print("\nu:")

    print(array)

def add_delays(matrix):
    for i in range(1, len(matrix)):  # start from the second row
        matrix[i] = [None] * i + matrix[i]
    return matrix

if __name__ == '__main__':
    A, u, rows, cols = initialisation()

    A = add_delays(A)

    print_matrix_array(A, u)
