import input
from collections import defaultdict

def make_lists(string):
    list_1 = []
    list_2 = []
    lines = string.split("\n")
    for line in lines:
        split_line = line.split("   ")
        list_1.append(int(split_line[0]))
        list_2.append(int(split_line[1]))
    return (list_1, list_2)

def part_1():
    list_1, list_2 = make_lists(input.lists)
    list_1.sort()
    list_2.sort()
    sum = 0
    for i in range(len(list_1)):
        sum += abs(list_1[i] - list_2[i])
    return sum

def part_2():
    list_1, list_2 = make_lists(input.lists)
    num_to_count = defaultdict(int) 
    for num in list_2:
        num_to_count[num] += 1
    
    sum = 0
    for num in list_1:
        sum += num * num_to_count[num]
    return sum

print(part_1())
print(part_2())