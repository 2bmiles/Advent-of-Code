import input

def parse_puzzle(puzzle):
    lines = puzzle.split("\n")
    split_puzzle = []
    for line in lines:
        current_line = []
        for char in line:
            current_line.append(char)
        split_puzzle.append(current_line)
    return split_puzzle

def get_element_at(index, array):
    x_coord, y_coord = index
    if x_coord < 0 or y_coord < 0:
        return None
    if len(array) > y_coord:
        if len(array[y_coord]) > x_coord:
            return array[y_coord][x_coord]
    return None

def check_xmas(x_index, puzzle, direction, reverse = False):
    """
    vertical: 1
    horizontal: 2
    diagonal up: 3
    diagonal down: 4
    """
    result = []
    match reverse:
        case True:
            multiplier = -1
        case False:
            multiplier = 1
    for i in range(4):
        i *= multiplier
        match direction:
            case 1: # vertical
                result.append(get_element_at((x_index[0], x_index[1] + i), puzzle))
            case 2: # horizontal
                result.append(get_element_at((x_index[0] + i, x_index[1]), puzzle))
            case 3: # diagonal up
                result.append(get_element_at((x_index[0] + i, x_index[1] - i), puzzle))
            case 4: # diagonal down
                result.append(get_element_at((x_index[0] + i, x_index[1] + i), puzzle))
    return result == ["X", "M", "A", "S"]

def check_x_mas(a_index, puzzle):
    upper_left = get_element_at((a_index[0] - 1, a_index[1] - 1), puzzle)
    lower_left = get_element_at((a_index[0] - 1, a_index[1] + 1), puzzle)
    upper_right = get_element_at((a_index[0] + 1, a_index[1] - 1), puzzle)
    lower_right = get_element_at((a_index[0] + 1, a_index[1] + 1), puzzle)
    corners = [upper_left, lower_left, upper_right, lower_right]
    if None in corners or sorted(corners) != ["M", "M", "S", "S"]:
        return False
    return upper_left != lower_right

def part_1():
    puzzle = parse_puzzle(input.puzzle)
    xmas_count = 0
    x_indices = []
    for i, line in enumerate(puzzle):
        for j, char in enumerate(line):
            if char == "X":
                x_indices.append((j, i))
    for x_index in x_indices:
        is_reverse = False
        for _ in range(2):
            for i in range(1, 5):
                if check_xmas(x_index, puzzle, i, is_reverse):
                    xmas_count += 1
            is_reverse = True
    return xmas_count

def part_2():
    puzzle = parse_puzzle(input.puzzle)
    x_mas_count = 0
    a_indices = []
    for i, line in enumerate(puzzle):
        for j, char in enumerate(line):
            if char == "A":
                a_indices.append((j, i))
    for a_index in a_indices:
        if check_x_mas(a_index, puzzle):
            x_mas_count += 1
    return x_mas_count

print(part_2())