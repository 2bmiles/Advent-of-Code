import input
from collections import defaultdict

def parse_instructions(instructions):
    lines = instructions.split("\n")
    instruction_list = []
    for line in lines:
        action = ''
        line = line.split(" ")
        if line[0] == "turn":
            line.pop(0)
        action = line[0]
        coord_1 = line[1].split(",")
        coord_2 = line[3].split(",")
        instruction_list.append((action, int(coord_1[0]), int(coord_1[1]), int(coord_2[0]) + 1, int(coord_2[1]) + 1))
        # adding one makes it work for exclusive endpoints (in a for loop)
        # 1 and 3 are x coords
        # 2 and 4 are y coords
    return instruction_list

def part_1():
    instructions = parse_instructions(input.instructions)
    on_lights = set()
    for op in instructions:
        if op[0] == "on":
            for i in range(op[1], op[3]):
                for j in range(op[2], op[4]):
                    on_lights.add((i, j))
        elif op[0] == "off":
            for i in range(op[1], op[3]):
                for j in range(op[2], op[4]):
                    if (i, j) in on_lights:
                        on_lights.remove((i, j))
        elif op[0] == "toggle":
            for i in range(op[1], op[3]):
                for j in range(op[2], op[4]):
                    if (i, j) in on_lights:
                        on_lights.remove((i, j))
                    else:
                        on_lights.add((i, j))
    return len(on_lights)

def part_2():
    instructions = parse_instructions(input.instructions)
    on_lights = defaultdict(int)
    for op in instructions:
        if op[0] == "on":
            for i in range(op[1], op[3]):
                for j in range(op[2], op[4]):
                    on_lights[(i, j)] += 1
        elif op[0] == "off":
            for i in range(op[1], op[3]):
                for j in range(op[2], op[4]):
                    on_lights[(i, j)] -= 1
                    if on_lights[(i, j)] < 0:
                        on_lights[(i, j)] = 0
        elif op[0] == "toggle":
            for i in range(op[1], op[3]):
                for j in range(op[2], op[4]):
                    on_lights[(i, j)] += 2
    sum = 0
    for brightness in on_lights.values():
        sum += brightness
    return sum

print(part_2())