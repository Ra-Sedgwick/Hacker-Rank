def array_left_rotation(array, numbers, rotations):

    # Case 0, rotations = 0
    if rotations == 0:
        return array

    for i in range(numbers - 1):
        tmp = array.pop(0)
        array.append(tmp)
    
    return array


def rotate_slice(array, rotation):
    if rotation > len(array):
        rotation -= len(array)

    return array[rotation:] + array[:rotation]


# Get input
numbers, rotations = map(int, input().strip().split(' '))
array = list(map(int, input().strip().split(' ')))
result = rotate_slice(array, rotations)
print(*result, sep=' ')
