def print_matrix_array(matrix, array):
    print("A: ")
    for row in matrix:
        print(row)

    print("\nu:")

    print(array)


def add_delays_to_front(matrix):
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


def apply_step(index):
    # propagate the inputs
    for i in range(len(processes)):
        processes[i]['a_in'] = A[i][index] if index < len(A[i]) else None
        processes[i]['u_in'] = processes[i + 1]['u_out'] if i < len(processes) - 1 else (u[index] if index < len(u)
                                                                                         else None)

    # execute the algorithm and update the register (v) and the outputs
    for i in range(len(processes)):
        processes[i]['v'] += processes[i]['a_in'] * processes[i]['u_in'] \
                                                        if processes[i]['a_in'] and processes[i]['u_in'] else 0

        processes[i]['a_out'] = processes[i]['a_in']
        processes[i]['u_out'] = processes[i]['u_in']

    index += 1
    return index


if __name__ == '__main__':
    A = [
        [1, 2, 1, 3],
        [1, -1, 2, -2],
        [4, 3, 2, 1]
    ]
    u = [1, 2, 3, 4]

    rows = len(A)
    cols = len(A[0])

    # Apply delays
    A = add_delays_to_back(A)

    print_matrix_array(A, u)

    # Initialize processes with dictionaries
    processes = initialize_processes(len(A))

    # Execute algorithm
    steps = cols + rows
    step_index = 0
    progression = 1
    while progression <= steps:
        step_index = apply_step(step_index)
        print("\nStep", progression, ":", processes)
        progression += 1

    print("\nResult:")
    for i in range(rows):
        print(f"P{i + 1}: {processes[i]['v']}")