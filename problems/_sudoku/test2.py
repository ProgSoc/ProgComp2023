import random

# num_to_hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g"]
num_to_hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
hex_to_num = {v: i for i, v in enumerate(num_to_hex)}


size = 9
subsize = 3

parsed = [[0 for c in range(size)] for c in range(size)]


def iter_all_states_influencing(states: list[list[int]], x: int, y: int):
    for i in range(size):
        if i != x:
            yield states[i][y]

    for j in range(size):
        if j != y:
            yield states[x][j]

    x0 = x // subsize * subsize
    y0 = y // subsize * subsize

    for i in range(x0, x0 + subsize):
        for j in range(y0, y0 + subsize):
            if i != x and j != y:
                yield states[i][j]

    if x == y:
        for i in range(size):
            if i != x:
                yield states[i][i]

    if x == size - y - 1:
        for i in range(size):
            if i != x:
                yield states[i][size - i - 1]


def clone_states(states: list[list[int]]) -> list[list[int]]:
    return [[v for v in line] for line in states]


def get_allowed_collapse_states(states: list[list[int]], x: int, y: int):
    influencing = set(iter_all_states_influencing(states, x, y))
    return [n for n in range(1, size + 1) if n not in influencing]


def is_solved_state(states: list[list[int]]) -> bool:
    for x in range(size):
        for y in range(size):
            if states[x][y] == 0:
                return False

    return True


def try_collapse_board(states: list[list[int]]) -> bool:
    for x in range(size):
        for y in range(size):
            can_collapse_to = get_allowed_collapse_states(states, x, y)
            if len(can_collapse_to) == 0:
                return False

    for collapse_amount in range(1, size + 1):
        for x in range(size):
            for y in range(size):
                if states[x][y] != 0:
                    continue

                can_collapse_to = get_allowed_collapse_states(
                    states,
                    x,
                    y,
                )

                if len(can_collapse_to) != collapse_amount:
                    continue

                random.shuffle(can_collapse_to)

                for v in can_collapse_to:
                    states[x][y] = v

                    succeeded = try_collapse_board(states)
                    if succeeded:
                        return True

                    states[x][y] = 0

    return True


def remove_random_values(states: list[list[int]]):
    for x0 in range(size // subsize):
        for y0 in range(size // subsize):
            coords = []
            for x in range(x0 * subsize, (x0 + 1) * subsize):
                for y in range(y0 * subsize, (y0 + 1) * subsize):
                    coords.append((x, y))

            random.shuffle(coords)
            coords = coords[:2]

            for x, y in coords:
                states[x][y] = 0


def iter_possible_states_to_collapse(states: list[list[list[int]]]) -> bool:
    min_length = min(len(s) for line in states for s in line if len(s) > 1)

    for x in range(size):
        for y in range(size):
            if len(states[x][y]) == min_length:
                yield (x, y)


def pretty_print_problem(problem: list[list[int]]):
    # Draw them with a border and with groups of 3x3
    for i in range(size):
        if i % subsize == 0:
            print(("+-" + "--" * subsize) * (size // subsize) + "+")
        for j in range(size):
            if j % subsize == 0:
                print("| ", end="")
            print(num_to_hex[problem[i][j]], end=" ")
        print("|")
    print(("+-" + "--" * subsize) * (size // subsize) + "+")


def print_problem(problem: list[list[int]]):
    for i in range(size):
        for j in range(size):
            print(num_to_hex[problem[i][j]], end=" ")
        print()


pretty_print_problem(parsed)
success = try_collapse_board(parsed)

print("Success:", success)
pretty_print_problem(parsed)
print_problem(parsed)

print()

remove_random_values(parsed)
print_problem(parsed)
