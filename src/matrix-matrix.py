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


def apply_step(index):
    # Propagate the input
    for i in range(rows):
        for j in range(cols):
            processes[i][j]['a_in'] = (processes[i][j + 1]['a_out'] if j < cols - 1
                                       else a[i][index] if index < len(a[i]) else None)
            processes[i][j]['b_in'] = (processes[i + 1][j]['b_out'] if i < rows - 1
                                       else b[index][j] if index < len(b) else None)

    # Execute the algorithm and update the register (v) and outputs
    for i in range(rows):
        for j in range(cols):
            processes[i][j]['v'] += processes[i][j]['a_in'] * processes[i][j]['b_in'] \
                                                                if processes[i][j]['a_in'] and processes[i][j]['b_in'] \
                                                                else 0
            processes[i][j]['a_out'] = processes[i][j]['a_in']
            processes[i][j]['b_out'] = processes[i][j]['b_in']

    index += 1

    return index


if __name__ == '__main__':
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

    rows = len(A)
    cols = len(B[0])

    # Apply delays and transpose as needed
    a = add_delays(A)
    b = transpose(add_delays(transpose(B)))

    print("A:")
    for r in a:
        print(r)
    print("\nB:")
    for r in b:
        print(r)

    print()

    # Initialize processes with dictionaries
    processes = initialise_processes()

    # Execute algorithm
    steps = rows * cols
    step_index = 0
    progression = 1
    while progression <= steps:
        step_index = apply_step(step_index)
        print("Step:", progression)
        for row in processes:
            print(row)
        print("")
        progression += 1

    print("Result:")
    for row in processes:
        row_values = [prc['v'] for prc in row]
        print(row_values)
