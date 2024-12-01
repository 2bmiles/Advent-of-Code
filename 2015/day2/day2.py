import input

def surface_area(l, w, h):
    return h * (2 * l + 2 * w) + 2 * (l * w)

def split_dimensions(dims):
    prism_list = dims.split("\n")
    dimensions = []
    for prism in prism_list:
        split_dims = prism.split("x")
        dimensions.append((split_dims[0], split_dims[1], split_dims[2]))
    return dimensions

def part_1():
    

print(split_dimensions(input.dims))