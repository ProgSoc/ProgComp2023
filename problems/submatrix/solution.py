def find_largest_square_submatrix(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])

    # Create a dynamic programming matrix to store the sizes of square submatrices
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_size = 0
    max_pos_i = 0
    max_pos_j = 0

    # Iterate over the matrix and update dp matrix
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == 1:
                # Update the size of the square submatrix based on neighboring values
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                # max_size = max(max_size, dp[i][j])
                if max_size < dp[i][j]:
                    max_size = dp[i][j]
                    max_pos_i = i
                    max_pos_j = j

    i_pos = max_pos_i - max_size
    j_pos = max_pos_j - max_size
    return ((i_pos, j_pos), max_size)

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