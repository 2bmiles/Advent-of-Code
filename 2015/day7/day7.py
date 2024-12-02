import input
from collections import defaultdict

def parse_instructions(instructions):
    lines = instructions.split("\n")
    operations = []
    for line in lines:
        operation = line.split(" ")
        operations.append((operation[1])) # operation, source 1, source 2, destination