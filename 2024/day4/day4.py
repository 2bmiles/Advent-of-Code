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
    if len(array) > y_coord:
        if len(array[y_coord]) > x_coord:
            return array[y_coord][x_coord]
    return None

def check(x_index, puzzle, direction, reverse = False):
    result = []
    
    match reverse:
        case True:
            for i in range(4):
                match direction:
                    case "vertical":
                        result.append(get_element_at((x_index[0], x_index[1] - i), puzzle))
                    case "horizontal":
                        result.append(get_element_at((x_index[0] - i, x_index[1]), puzzle))
                    case "diagonal up":
                        result.append(get_element_at((x_index[0] - i, x_index[1] + i), puzzle))
        case False:
            for i in range(4):
                match direction:
                    case "vertical":
                        result.append(get_element_at((x_index[0], x_index[1] + i), puzzle))
                    case "horizontal":
                        result.append(get_element_at((x_index[0] + i, x_index[1]), puzzle))
                    case "diagonal up":
                        result.append(get_element_at((x_index[0] + i, x_index[1] - i), puzzle))
    return result == ["X", "M", "A", "S"]

def part_1():
    puzzle = parse_puzzle(input.puzzle)
    xmas_count = 0
    x_indices = []
    for i, line in enumerate(puzzle):
        for j, char in enumerate(line):
            if char == "X":
                x_indices.append((j, i))

#print(part_1())
print(check((9, 3), parse_puzzle(input.puzzle), "diagonal down"))