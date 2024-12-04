import input

def parse_triangles(triangles):
    triangle_list = triangles.split("\n")
    side_lengths = []
    for triangle in triangle_list:
        current_side_lengths = []
        for side in triangle.split(" "):
            if side.isnumeric():
                current_side_lengths.append(int(side))
        side_lengths.append(current_side_lengths)
    return side_lengths

def part_1():
    triangles = parse_triangles(input.triangles)
    possible_triangle_count = 0
    for triangle in triangles:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            possible_triangle_count += 1
    return possible_triangle_count


print(part_1())