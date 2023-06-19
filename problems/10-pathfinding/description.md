# Pathfinding

You are writing a pathfinding algorithm to choose the shortest path from point A to point B. In this case, point A is coordinate (1, 0) and point B is (N-2, N-1) where N is the size of the grid.

You start with a 2d boolean array of size N x N. True represents a wall, false represents a path. You can only move up, down, left, or right. You cannot move diagonally. You cannot move through walls.

As a result, you'd have a list of directions Up/Down/Left/Right (U/D/L/R) that would get you from point A to point B.

For example, here is a simple maze:

![maze](_images/maze2.png)

And here's the directions recuired to get from top left to bottom right: \
`DDDRRUURRDDDDD`

Here is a larger example:

![maze](_images/maze.png)

With these being the resulting directions: \
`DDDRRUURRRRRRRRRRDDDDRRDDLLLLUULLLLUULLDDDDLLUULLDDDDDDRRRRRRRRRRRRDDLLDDLLLLLLUULLLLDDDDDDRRUURRRRDDRRRRUURRUURRRRDDLLDDRRRRD`

## Input format

The first line contains a number `N` which is the size of the grid.

The next `N` lines contain `N*2` characters each, which are either `  ` or `##`. `  ` represents a path, `##` represents a wall.

## Output format

Output the directions required to get from point A to point B (U/D/L/R).
