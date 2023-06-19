def find_largest_square_submatrix(matrix):
    # Your code goes here
    return ((x, y), max_size)

def parse_matrix():
    size = int(input())
    matrix = []

    for _ in range(size):
        line = input()
        if not line:  # Stop reading if an empty line is encountered
            break

        matrix.append([int(x) for x in line.split(" ")])

    return matrix

answer = find_largest_square_submatrix(parse_matrix())
print(answer[1])
print(str(answer[0][0]) + " " + str(answer[0][1]))