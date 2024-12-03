import input

def parse_directions(dirs):
    split_dirs = dirs.split(", ")
    dirs_list = []
    for dir in split_dirs:
        dirs_list.append((dir[0], int(dir[1:])))
    return dirs_list

def part_1():
    dirs = parse_directions(input.directions)
    """
    1: North
    2: East
    3: South
    4: West
    """
    facing = 1
    x_offset = 0
    y_offset = 0
    for dir in dirs:
        match dir[0]:
            case "L":
                facing -= 1
                if facing == 0:
                    facing = 4
            case "R":
                facing += 1
                if facing == 5:
                    facing = 1
        match facing:
            case 1:
                y_offset += dir[1]
            case 2:
                x_offset += dir[1]
            case 3:
                y_offset -= dir[1]
            case 4:
                x_offset -= dir[1]
    return abs(x_offset) + abs(y_offset)

def part_2():
    dirs = parse_directions(input.directions)
    facing = 1
    """
    1: North
    2: East
    3: South
    4: West
    """
    points_visited = {(0, 0)}
    location = (0, 0)
    for dir in dirs:
        match dir[0]:
            case "L":
                facing -= 1
                if facing == 0:
                    facing = 4
            case "R":
                facing += 1
                if facing == 5:
                    facing = 1
        for i in range(dir[1]):
            match facing:
                case 1:
                    location = (location[0], location[1] + 1)
                case 2:
                    location = (location[0] + 1, location[1])
                case 3:
                    location = (location[0], location[1] - 1)
                case 4:
                    location = (location[0] - 1, location[1])
            print(dir, location)
            if location in points_visited:
                return abs(location[0]) + abs(location[1])
            points_visited.add(location)

print(part_2())