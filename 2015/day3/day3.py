import input
from collections import defaultdict

def part_1():
    house_to_presents = defaultdict(int)
    house_to_presents[(0, 0)] = 1
    s_location = (0, 0)
    for direction in input.directions:
        match direction:
            case "^":
                s_location = (s_location[0], s_location[1] + 1)
            case "v":
                s_location = (s_location[0], s_location[1] - 1)
            case "<":
                s_location = (s_location[0] - 1, s_location[1])
            case ">":
                s_location = (s_location[0] + 1, s_location[1])
        house_to_presents[s_location] += 1    
    sum = 0
    for presents in house_to_presents.values():
        if presents >= 1:
            sum += 1
    return sum

def part_2():
    house_to_presents = defaultdict(int)
    house_to_presents[(0, 0)] = 2
    s_location = (0, 0)
    rd_location = (0, 0)
    santa_moving = True
    for direction in input.directions:
        match direction:
            case "^" if santa_moving:
                s_location = (s_location[0], s_location[1] + 1)
            case "v" if santa_moving:
                s_location = (s_location[0], s_location[1] - 1)
            case "<" if santa_moving:
                s_location = (s_location[0] - 1, s_location[1])
            case ">" if santa_moving:
                s_location = (s_location[0] + 1, s_location[1])
            case "^" if not santa_moving:
                rd_location = (rd_location[0], rd_location[1] + 1)
            case "v" if not santa_moving:
                rd_location = (rd_location[0], rd_location[1] - 1)
            case "<" if not santa_moving:
                rd_location = (rd_location[0] - 1, rd_location[1])
            case ">" if not santa_moving:
                rd_location = (rd_location[0] + 1, rd_location[1])
        if santa_moving:
            house_to_presents[s_location] += 1
        else:
            house_to_presents[rd_location] += 1
        santa_moving = not santa_moving
    sum = 0
    for presents in house_to_presents.values():
        if presents >= 1:
            sum += 1
    return sum

print(part_1())
print(part_2())