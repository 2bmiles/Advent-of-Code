import input

def part_1():
    number_codes = input.directions.split("\n")
    numbers = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    code = []
    row = 1
    col = 1
    for number in number_codes:
        for dir in number:
            match dir:
                case "U":
                    row -= 1
                    if row < 0:
                        row = 0
                case "D":
                    row += 1
                    if row > 2:
                        row = 2
                case "R":
                    col += 1
                    if col > 2:
                        col = 2
                case "L":
                    col -= 1
                    if col < 0:
                        col = 0
            print(row, col, numbers[row][col])
        code.append(str(numbers[row][col]))
    return "".join(code)

def part_2():
    number_codes = input.directions.split("\n")
    numbers = [
        ["", "", 1, "", ""],
        ["", 2, 3, 4, ""],
        [5, 6, 7, 8, 9],
        ["", "A", "B", "C", ""],
        ["", "", "D", "", ""]
    ]
    code = []
    row = 2
    col = 0
    for number in number_codes:
        for dir in number:
            match dir:
                case "U":
                    row -= 1
                    if row < 0 or numbers[row][col] == "":
                        row += 1
                case "D":
                    row += 1
                    if row > 4 or numbers[row][col] == "":
                        row -= 1
                case "R":
                    col += 1
                    if col > 4 or numbers[row][col] == "":
                        col -= 1
                case "L":
                    col -= 1
                    if col < 0 or numbers[row][col] == "":
                        col += 1
            print(row, col, numbers[row][col])
        code.append(str(numbers[row][col]))
    return "".join(code)

print(part_2())