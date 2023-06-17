def iter_all_states_influencing(states: list[list[int]], x: int, y: int):
    for i in range(9):
        if i != x:
            yield states[i][y]

    for j in range(9):
        if j != y:
            yield states[x][j]

    x0 = x // 3 * 3
    y0 = y // 3 * 3

    for i in range(x0, x0 + 3):
        for j in range(y0, y0 + 3):
            if i != x and j != y:
                yield states[i][j]

    # if x == y:
    #     for i in range(9):
    #         if i != x:
    #             yield states[i][i]

    # if x == 9 - y - 1:
    #     for i in range(9):
    #         if i != x:
    #             yield states[i][9 - i - 1]


def clone_states(states: list[list[int]]) -> list[list[int]]:
    return [[v for v in line] for line in states]


def get_allowed_collapse_states(states: list[list[int]], x: int, y: int):
    influencing = set(iter_all_states_influencing(states, x, y))
    return [n for n in range(1, 10) if n not in influencing]


def is_solved_state(states: list[list[int]]) -> bool:
    for x in range(9):
        for y in range(9):
            if states[x][y] == 0:
                return False

    return True


def try_collapse_board(states: list[list[int]]) -> bool:
    for x in range(9):
        for y in range(9):
            can_collapse_to = get_allowed_collapse_states(states, x, y)
            if len(can_collapse_to) == 0:
                return False

    for collapse_amount in range(1, 10):
        for x in range(9):
            for y in range(9):
                if states[x][y] != 0:
                    continue

                can_collapse_to = get_allowed_collapse_states(
                    states,
                    x,
                    y,
                )

                if len(can_collapse_to) != collapse_amount:
                    continue

                for v in can_collapse_to:
                    states[x][y] = v

                    succeeded = try_collapse_board(states)
                    if succeeded:
                        return True

                    states[x][y] = 0

    if not is_solved_state(states):
        return False

    return True


def iter_possible_states_to_collapse(states: list[list[list[int]]]) -> bool:
    min_length = min(len(s) for line in states for s in line if len(s) > 1)

    for x in range(9):
        for y in range(9):
            if len(states[x][y]) == min_length:
                yield (x, y)


def print_problem(problem: list[list[int]]):
    for i in range(9):
        for j in range(9):
            print(problem[i][j], end=" ")
        print()


def parse_problem() -> list[list[int]]:
    problem = []
    for i in range(9):
        line = input().split(" ")
        problem.append([int(v) for v in line])

    return problem


parsed = parse_problem()
solved = try_collapse_board(parsed)
if solved:
    print_problem(parsed)
else:
    print("No solution")