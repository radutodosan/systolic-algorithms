
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


def add_delays_to_back(matrix):
    for index, row in enumerate(matrix):
        for _ in range(len(matrix) - index - 1):
            row.insert(0, None)
    return matrix


def initialize_processes(matrix_length):
    return [{
        'v': 0,
        'a_in': None,
        'a_out': None,
        'u_in': None,
        'u_out': None
    } for _ in range(matrix_length)]


def step(index, prces, matrix):

    # propagate the inputs
    for i in range(len(prces)):
        prces[i]['a_in'] = matrix[i][index] if index < len(matrix[i]) else 0
        prces[i]['u_in'] = prces[i + 1]['u_out'] if i < len(prces) - 1 else (u[index] if index < len(u) else 0)

    # execute the algorithm and update the register (v) and the outputs
    for i in range(len(prces)):
        prces[i]['v'] += prces[i]['a_in'] * prces[i]['u_in']    if prces[i]['a_in'] and prces[i]['u_in'] else 0
        prces[i]['a_out'] = prces[i]['a_in']    if prces[i]['a_in'] else 0
        prces[i]['u_out'] = prces[i]['u_in']    if prces[i]['u_in'] else 0

    index += 1

    return index, prces


if __name__ == '__main__':
    A, u, rows, cols = initialisation()

    A = add_delays_to_back(A)

    print_matrix_array(A, u)

    input_index = 0
    processes = initialize_processes(len(A))

    steps = len(A[len(A) - 1]) * (len(A) - 1)
    progression = 1
    while progression < steps:
        input_index, processes = step(input_index, processes, A)
        print("\nStep", progression, ":", processes)
        progression += 1
