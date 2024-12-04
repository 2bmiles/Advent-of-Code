import input
import re

mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"

def part_1():
    matches = re.findall(mul_regex, input.program)
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
    return sum

def part_2():
    regex = mul_regex + r"|(do\(\))|(don't\(\))"
    matches = re.findall(regex, input.program)
    sum = 0
    enabled = True
    for match in matches:
        if match[2] != '':
            enabled = True
        elif match[3] != '':
            enabled = False
        else:
            if enabled:
                sum += int(match[0]) * int(match[1])
    return sum

print(part_2())