def initialisation():
    a_init = [
        [1, 2, 1, 3],
        [1, -1, 2, -2],
        [4, 3, 2, 1]
    ]
    b_init = [
        [1, 1, 1],
        [2, 1, -1],
        [3, 2, -1],
        [-2, 3, 5]
    ]

    rows_init = len(a_init)
    cols_init = len(b_init[0])

    return a_init, b_init, rows_init, cols_init

def initialise_processes():
    return [[{
        'v': 0,
        'a_in': None,
        'a_out': None,
        'b_in': None,
        'b_out': None
    }
        for _ in range(cols)]
    for _ in range(rows)]


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def add_delays(matrix):
    for i, ROW in enumerate(matrix):
        # add None to beginning
        for _ in range(len(matrix) - i - 1):
            ROW.insert(0, None)
        # append None
        for _ in range(i):
            ROW.append(None)
    return matrix


def step(index, prces):
    """Perform one step of computation."""

    # Propagate the input
    for i in range(rows):
        for j in range(cols):
            prces[i][j]['a_in'] = (prces[i][j + 1]['a_out'] if j < cols - 1 else
                                  a[i][index] if index < len(a[i]) else 0)
            prces[i][j]['b_in'] = (prces[i + 1][j]['b_out'] if i < rows - 1 else
                                  b[index][j] if index < len(b) else 0)

    # Execute the algorithm and update the register (v) and outputs
    for i in range(rows):
        for j in range(cols):
            prces[i][j]['v'] += prces[i][j]['a_in'] * prces[i][j]['b_in'] if prces[i][j]['a_in'] and prces[i][j]['b_in'] else 0
            prces[i][j]['a_out'] = prces[i][j]['a_in'] if prces[i][j]['a_in'] else 0
            prces[i][j]['b_out'] = prces[i][j]['b_in'] if prces[i][j]['b_in'] else 0

    index += 1

    return index, prces


if __name__ == '__main__':
    A, B, rows, cols = initialisation()

    # Apply delays and transpose as needed
    a = add_delays(A)
    b = transpose(add_delays(transpose(B)))

    # Initialize processes with dictionaries
    processes = initialise_processes()

    input_index = 0

    steps = rows * cols
    progression = 1
    while progression <= steps:
        input_index, processes = step(input_index, processes)
        print("Step:", progression)
        for row in processes:
            print(row)
        print("")
        progression += 1
