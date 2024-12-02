import input

def part_1():
    strings = input.strings.split("\n")
    good_strings = []
    vowels = "aeiou"
    bad_strs = ["ab", "cd", "pq", "xy"]
    for string in strings:
        vowel_count = 0
        has_double_letter = False
        last_letter = ""    
        for char in string:
            if char in vowels:
                vowel_count += 1
            if char == last_letter:
                has_double_letter = True
            last_letter = char
        contains_bad_str = False
        for str in bad_strs:
            if str in string:
                contains_bad_str = True
        if vowel_count >= 3 and has_double_letter and not contains_bad_str:
            good_strings.append(string)
    return len(good_strings)

def part_2():
    strings = input.strings.split("\n")
    good_strings = []
    for string in strings:
        has_two_pairs = False
        has_letter_between = False
        prev_letter = ""
        prev_prev_letter = ""
        for i in range(len(string)):
            pair = string[i:i+2]
            if pair in string[i+2:]:
                has_two_pairs = True
            letter = string[i]
            if letter == prev_prev_letter:
                has_letter_between = True
            prev_prev_letter = prev_letter
            prev_letter = letter
        if has_two_pairs and has_letter_between:
            good_strings.append(string)
    return len(good_strings)

print(part_1())
print(part_2())