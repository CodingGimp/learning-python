def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target was not found.')

numbers = list(range(1, 10))

result = linear_search(numbers, 6)
verify(result)