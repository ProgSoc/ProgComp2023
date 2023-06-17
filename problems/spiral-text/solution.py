def print_spiral(s):
    import math

    # Calculate the size of the matrix
    n = math.ceil(math.sqrt(len(s)))

    # Initialize the matrix
    matrix = [[" "] * n for _ in range(n)]

    # Calculate the boundaries
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    # Initialize the string index
    index = 0

    while True:
        # Print the top row
        for i in range(left, right + 1):
            if index >= len(s):
                break

            matrix[top][i] = s[index]
            index += 1
        top += 1
        if not (top <= bottom):
            break

        # Print the right column
        for i in range(top, bottom + 1):
            if index >= len(s):
                break

            matrix[i][right] = s[index]
            index += 1
        right -= 1
        if not (left <= right):
            break

        # Print the bottom row
        for i in range(right, left - 1, -1):
            if index >= len(s):
                break

            matrix[bottom][i] = s[index]
            index += 1
        bottom -= 1
        if not (top <= bottom):
            break

        # Print the left column
        for i in range(bottom, top - 1, -1):
            if index >= len(s):
                break

            matrix[i][left] = s[index]
            index += 1
        left += 1
        if not (left <= right):
            break

        if index >= len(s):
            break

    # Print the matrix
    for row in matrix:
        print(" ".join(row))


s = input()
print_spiral(s)
