from collections import deque


def solve_maze(maze: list[list[bool]]) -> list[str]:
    # Your code goes here
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
