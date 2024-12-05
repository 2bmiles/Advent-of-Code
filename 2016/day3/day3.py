import input

def parse_triangles_part_1(triangles):
    triangle_list = triangles.split("\n")
    side_lengths = []
    for triangle in triangle_list:
        current_side_lengths = []
        for side in triangle.split(" "):
            if side.isnumeric():
                current_side_lengths.append(int(side))
        side_lengths.append(current_side_lengths)
    return side_lengths

def parse_triangles_part_2(triangles):
    lines = triangles.split("\n")
    list_1 = []
    list_2 = []
    list_3 = []
    for line in lines:
        current_side = 1
        for side in line.split(" "):
            if side.isnumeric():
                match current_side:
                    case 1:
                        list_1.append(int(side))
                    case 2:
                        list_2.append(int(side))
                    case 3:
                        list_3.append(int(side))
                current_side += 1
    list_1.extend(list_2)
    list_1.extend(list_3)
    return list_1

def part_1():
    triangles = parse_triangles_part_1(input.triangles)
    valid_triangle_count = 0
    for triangle in triangles:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            valid_triangle_count += 1
    return valid_triangle_count

def part_2():
    number_list = parse_triangles_part_2(input.triangles)
    valid_triangle_count = 0
    for i in range(len(number_list) // 3):
        sides = sorted([number_list[i * 3], number_list[i * 3 + 1], number_list[i * 3 + 2]])
        if sides[0] + sides[1] > sides[2]:
            valid_triangle_count += 1
    return valid_triangle_count

print(part_2())