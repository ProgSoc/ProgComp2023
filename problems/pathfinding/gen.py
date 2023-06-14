import numpy as np
import random
from collections import deque


def create_maze(size):
    shape = ((size * 2) + 1, (size * 2) + 1)
    maze = np.ones(shape, dtype=bool)  # Create a filled grid
    r, c = (
        1,
        1,
    )  # Choose a random starting cell
    maze[r, c] = False

    stack = [(r, c)]
    while stack:
        r, c = stack[-1]  # Get the last cell
        options = [  # Create a list of possible moves
            (r - 2, c),
            (r + 2, c),
            (r, c - 2),
            (r, c + 2),
        ]
        random.shuffle(options)  # Randomize the moves
        for dr, dc in options:
            if dr > 0 and dr < shape[0] and dc > 0 and dc < shape[1] and maze[dr, dc]:
                # If the move is valid and the cell is not visited, move to it
                stack.append((dr, dc))
                maze[dr, dc] = False  # Mark the cell as visited
                maze[(r + dr) // 2, (c + dc) // 2] = False  # Remove the wall
                break
        else:
            # If there are no valid moves, backtrack
            stack.pop()

    maze[0, 1] = False  # Remove the entrance
    maze[-1, -2] = False  # Remove the exit

    return maze


def print_maze(size):
    maze = create_maze(size)
    for row in maze:
        for cell in row:
            if cell:  # If the cell is a wall, print '#'
                print("##", end="")
            else:  # If the cell is a path, print a whitespace
                print("  ", end="")
        print()  # Print a newline at the end of each row


def solve_maze(maze):
    rows, cols = maze.shape
    start = (0, 1)  # start position
    goal = (rows - 1, cols - 2)  # goal position

    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        for dx, dy, direction in [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols) and not maze[nx, ny]:
                if (nx, ny) == goal:
                    return path + [direction]
                elif (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [direction]))
                    visited.add((nx, ny))

    return []  # return empty list if no path found


def draw_maze(size):
    maze = create_maze(size)
    solved = solve_maze(maze)
    from PIL import Image, ImageDraw

    img = Image.new("RGB", ((size * 2 + 1) * 20, (size * 2 + 1) * 20), color="white")
    draw = ImageDraw.Draw(img)

    for i in range(size * 2 + 1):
        for j in range(size * 2 + 1):
            if maze[j, i]:
                draw.rectangle(
                    [(i * 20, j * 20), ((i + 1) * 20, (j + 1) * 20)],
                    fill="black",
                    outline="black",
                )

    x = 1
    y = 0

    for i in solved:
        old_x = x
        old_y = y

        if i == "U":
            y -= 1
        elif i == "D":
            y += 1
        elif i == "L":
            x -= 1
        elif i == "R":
            x += 1
        draw.line(
            [(old_x * 20 + 10, old_y * 20 + 10), (x * 20 + 10, y * 20 + 10)],
            fill="red",
            width=5,
        )

    img.save("maze.png")
    print("".join(solved))


draw_maze(3)
