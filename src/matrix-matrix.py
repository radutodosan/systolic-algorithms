def initialisation():
    A = [
        [1, 2, 1, 3],
        [1, -1, 2, -2],
        [4, 3, 2, 1]
    ]
    B = [
        [1, 1, 1],
        [2, 1, -1],
        [3, 2, -1],
        [-2, 3, 5]
    ]

    ROWS = len(A)
    COLS = len(B[0])

    return A, B, ROWS, COLS

def initialise_processes():
    return [[{
        'c': 0,
        'ain': None,
        'aout': None,
        'bin': None,
        'bout': None
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
            prces[i][j]['ain'] = (prces[i][j + 1]['aout'] if j < cols - 1 else
                                  a[i][index] if index < len(a[i]) else 0)
            prces[i][j]['bin'] = (prces[i + 1][j]['bout'] if i < rows - 1 else
                                  b[index][j] if index < len(b) else 0)

    # Execute the algorithm and update the register (c) and outputs
    for i in range(rows):
        for j in range(cols):
            prces[i][j]['c'] += prces[i][j]['ain'] * prces[i][j]['bin'] if prces[i][j]['ain'] and prces[i][j]['bin'] else 0
            prces[i][j]['aout'] = prces[i][j]['ain'] if prces[i][j]['ain'] else 0
            prces[i][j]['bout'] = prces[i][j]['bin'] if prces[i][j]['bin'] else 0

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
    while progression < steps:
        input_index, processes = step(input_index, processes)
        for row in processes:
            print(row)
        print("")
        progression += 1
