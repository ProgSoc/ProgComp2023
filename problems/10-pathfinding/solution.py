from collections import deque


def solve_maze(maze: list[list[bool]]) -> list[str]:
    size = len(maze)
    start = (0, 1)  # start position
    goal = (size - 1, size - 2)  # goal position

    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        for dx, dy, direction in [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < size and 0 <= ny < size) and not maze[nx][ny]:
                if (nx, ny) == goal:
                    return path + [direction]
                elif (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [direction]))
                    visited.add((nx, ny))

    return []


def parse_maze():
    size = int(input())
    maze = []

    for i in range(size):
        line = input()
        if not line:  # Stop reading if an empty line is encountered
            break
        row = []
        for i in range(0, len(line), 2):
            cell = line[i]
            if cell == "#":
                row.append(True)
            elif cell == " ":
                row.append(False)
        maze.append(row)

    return maze


maze = parse_maze()
solved = solve_maze(maze)
print("".join(solved))
