import input

def part_1():
    up_count = 0
    down_count = 0
    for char in input.instructions:
        if char == "(":
            up_count += 1
        else:
            down_count += 1
    return up_count - down_count

def part_2():
    floor = 0
    for i in range(len(input.instructions)):
        if input.instructions[i] == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i + 1

print(part_1())
print(part_2())