def rec_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list))//2

        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return rec_binary_search(list[mid+1:], target)
            else:
                return rec_binary_search(list[:mid], target)

def verify(result):
    if result is not None:
        print('Target found: ', result)
    else:
        print('Target was not found.')

numbers = list(range(1, 10))

result = rec_binary_search(numbers, 12)
verify(result)

result = rec_binary_search(numbers, 3)
verify(result)
