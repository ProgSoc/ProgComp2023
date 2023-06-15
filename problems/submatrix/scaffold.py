def binary_submatrix(image):
    # Your solution goes here
    pass


def parse_matrix():
    size = int(input())
    matrix = []

    for _ in range(size):
        line = input()
        if not line:
            break

        matrix.append([int(x) for x in line.split(" ")])

    return matrix

binary_submatrix(parse_matrix())
