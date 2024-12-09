import input

def get_element_at(index, array):
    x_coord, y_coord = index
    if x_coord < 0 or y_coord < 0:
        return None
    if len(array) > y_coord:
        if len(array[y_coord]) > x_coord:
            return array[y_coord][x_coord]
    return None

def find_index(array, value):
    for i, row in enumerate(array):
        if value in row:
            return row.index(value), i
    return None

def parse_map(map):
    lines = map.split("\n")
    split_map = []
    for line in lines:
        current_line = []
        current_line.extend(line)
        split_map.append(current_line)
    return split_map

def turn_guard(current_facing):
    if current_facing == 4:
        return 1
    return current_facing + 1

def part_1():
    map = parse_map(input.map)
    guard_location = find_index(map, "^")
    seen_locations = {guard_location}
    guard_facing = 1
    # 1: North
    # 2: East
    # 3: South
    # 4: West
    while True:
        previous_location = guard_location
        match guard_facing:
            case 1:
                guard_location = (guard_location[0], guard_location[1] - 1)
            case 2:
                guard_location = (guard_location[0] + 1, guard_location[1])
            case 3:
                guard_location = (guard_location[0], guard_location[1] + 1)
            case 4:
                guard_location = (guard_location[0] - 1, guard_location[1])
        match get_element_at(guard_location, map):
            case "." | "^":
                seen_locations.add(guard_location)
            case "#":
                guard_location = previous_location
                guard_facing = turn_guard(guard_facing)
            case None:
                return len(seen_locations)
print(part_1())