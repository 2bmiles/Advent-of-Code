import input

def surface_area(dims):
    l, w, h = dims
    return h * (2 * l + 2 * w) + 2 * (l * w)

def split_dimensions(dims):
    prism_list = dims.split("\n")
    dimensions = []
    for prism in prism_list:
        split_dims = prism.split("x")
        dimensions.append((int(split_dims[0]), int(split_dims[1]), int(split_dims[2])))
    return dimensions

def part_1():
    prisms = split_dimensions(input.dims)
    sum = 0
    for prism in prisms:
        sum += surface_area(prism)
        sum += (sorted(prism)[0] * sorted(prism)[1])
    return sum

def part_2():
    prisms = split_dimensions(input.dims)
    sum = 0
    for prism in prisms:
        sum += 2 * sorted(prism)[0] + 2 * sorted(prism)[1]
        sum += prism[0] * prism[1] * prism[2]
    return sum

print(part_1())
print(part_2())